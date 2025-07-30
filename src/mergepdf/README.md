# Merge PDF

* This script combines a bunch of PDFs into one PDF file, complete with table of contents.
* This motivation for this script came from combining one-page RPG games from [itch.io](https://itch.io)

```bash
# Install dependencies in isolated environment
poetry install

# Place PDFs in mergepdf/pdfs/
# Edit mergepdf/pdfs/pdf_list.json to match file names & TOC titles

# Run
poetry run mergepdf
```
