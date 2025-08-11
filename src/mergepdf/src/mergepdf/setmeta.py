import pikepdf
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

XMP_NS = {
    'x': 'adobe:ns:meta/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'dc': 'http://purl.org/dc/elements/1.1/'
}

def set_xmp_metadata(xmp_bytes, title=None, author=None):
    if xmp_bytes is None:
        # Create a minimal XMP packet if none exists
        xmp_template = '''<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
        <x:xmpmeta xmlns:x="adobe:ns:meta/">
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about=""
              xmlns:dc="http://purl.org/dc/elements/1.1/">
            </rdf:Description>
          </rdf:RDF>
        </x:xmpmeta>
        <?xpacket end='w'?>'''
        root = ET.fromstring(xmp_template)
    else:
        root = ET.fromstring(xmp_bytes)

    rdf = root.find('x:xmpmeta/rdf:RDF', XMP_NS)
    if rdf is None:
        rdf = ET.SubElement(root.find('x:xmpmeta', XMP_NS), '{%s}RDF' % XMP_NS['rdf'])

    desc = None
    for d in rdf.findall('rdf:Description', XMP_NS):
        if d.attrib.get('{%s}about' % XMP_NS['rdf'], '') == '':
            desc = d
            break
    if desc is None:
        desc = ET.SubElement(rdf, '{%s}Description' % XMP_NS['rdf'], { '{%s}about' % XMP_NS['rdf']: '' })

    # Set Title
    if title is not None:
        dc_title = desc.find('dc:title', XMP_NS)
        if dc_title is None:
            dc_title = ET.SubElement(desc, '{%s}title' % XMP_NS['dc'])
        # Clear existing children
        dc_title.clear()
        alt = ET.SubElement(dc_title, '{%s}Alt' % XMP_NS['rdf'])
        li = ET.SubElement(alt, '{%s}li' % XMP_NS['rdf'], {'xml:lang': 'x-default'})
        li.text = title

    # Set Author (dc:creator is a Seq of strings)
    if author is not None:
        dc_creator = desc.find('dc:creator', XMP_NS)
        if dc_creator is None:
            dc_creator = ET.SubElement(desc, '{%s}creator' % XMP_NS['dc'])
        dc_creator.clear()
        seq = ET.SubElement(dc_creator, '{%s}Seq' % XMP_NS['rdf'])
        li = ET.SubElement(seq, '{%s}li' % XMP_NS['rdf'])
        li.text = author

    # Return serialized XMP metadata bytes
    return ET.tostring(root, encoding='utf-8', xml_declaration=True)

def main():
    if len(sys.argv) < 2:
        print("Usage: setmeta <pdf_path>")
        sys.exit(1)

    pdf_path = Path(sys.argv[1]).resolve()

    if not pdf_path.exists():
        print(f"Error: {pdf_path} does not exist.")
        sys.exit(1)

    if pdf_path.suffix.lower() != ".pdf":
        print("Error: File must be a PDF.")
        sys.exit(1)

    title = input("Enter new title (leave blank to keep existing): ").strip()
    author = input("Enter new author (leave blank to keep existing): ").strip()
    publisher = input("Enter new publisher (leave blank to keep existing): ").strip()

    try:
        with pikepdf.open(pdf_path, allow_overwriting_input=True) as pdf:
            info = pdf.docinfo

            if title:
                info["/Title"] = title
            if author:
                info["/Author"] = author
            if publisher:
                info["/Publisher"] = publisher

            # Update XMP metadata if present or create new
            xmp_bytes = pdf.open_metadata()
            new_xmp = xmp_bytes.read_bytes() if xmp_bytes else None

            if title or author:
                updated_xmp = set_xmp_metadata(new_xmp, title=title if title else None, author=author if author else None)
                pdf.save_metadata(updated_xmp)

            pdf.save(pdf_path)

        print(f"Updated metadata for {pdf_path}")
    except Exception as e:
        print(f"Error updating PDF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
