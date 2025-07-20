import pymupdf4llm
from pathlib import Path
from environs import env

env.read_env()
REFERENCES_DIR = env.str("REFERENCES_DIR")
PDFS_DIR = env.str("PDFS_DIR")

def extraction_process(pdfs):
    output_dir = Path(REFERENCES_DIR).expanduser()
    if not output_dir.exists():
            output_dir.mkdir(parents=True, exist_ok=True)
    
    for pdf in pdfs:
        md_text = pymupdf4llm.to_markdown(str(pdf))
        output_file = output_dir / f'{pdf.stem}.md'
        output_file.write_text(md_text, encoding='utf-8')
        print(f"Extracted: {pdf.name} -> {output_file.name}")

def main():
    subjects_path = Path(REFERENCES_DIR).expanduser()
    pdf_files_generator = subjects_path.glob('*.pdf')

    pdf_files = list()

    print("Generating the PosixPath for files in Subjects Directory...")
    for file in pdf_files_generator:
        pdf_files.append(file)
    
    print(f"Files in Subjects: {', '.join(file.name for file in pdf_files)}")
    print("Initiating Extraction of Text...")
    extraction_process(pdf_files)


if __name__ == '__main__':
    main()