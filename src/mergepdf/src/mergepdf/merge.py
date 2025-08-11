import pikepdf
from pathlib import Path
import sys

def main():
    project_root = Path(__file__).resolve().parent.parent.parent
    pdf_dir = project_root / "pdfs"
    converted_pdf_dir = project_root / "converted"

    if not pdf_dir.exists():
        print(f"Error: {pdf_dir} not found.")
        sys.exit(1)

    # Prompt for metadata
    title = input("Enter PDF title: ").strip()
    author = input("Enter PDF author: ").strip()

    # Recursively find all PDFs, sort by (parent folder, filename)
    pdf_files = sorted(
        pdf_dir.rglob("*.pdf"),
        key=lambda p: (str(p.parent).lower(), p.name.lower())
    )

    if not pdf_files:
        print("Error: No PDF files found in directory.")
        sys.exit(1)

    merged_pdf = pikepdf.Pdf.new()

    for pdf_path in pdf_files:
        print(f"Processing: {pdf_path}")
        try:
            src = pikepdf.Pdf.open(pdf_path)
            merged_pdf.pages.extend(src.pages)
        except Exception as e:
            print(f"Warning: Could not process {pdf_path}: {e}")

    if len(merged_pdf.pages) == 0:
        print("Error: No valid PDF pages found to merge.")
        sys.exit(1)

    if title:
        merged_pdf.docinfo["/Title"] = title
    if author:
        merged_pdf.docinfo["/Author"] = author

    output_path = converted_pdf_dir / f"{author} - {title}.pdf"
    merged_pdf.save(output_path)
    print(f"Merged PDF saved as {output_path}")

if __name__ == "__main__":
    main()
