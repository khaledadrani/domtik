from pathlib import Path

import fitz


def read_pdf(file_path):
    with fitz.open(file_path) as doc:  # open document
        text = chr(12).join([page.get_text() for page in doc])
    return {
        "text": text,
        "file_path": file_path
    }


def post_process_single_record(record, dest, min_length=None):
    if min_length and len(record["text"]) < min_length:
        print(record["file_path"], "too short for length ", min_length)

    path = Path(record['file_path'])

    final_file_name = path.stem

    with open(Path(dest) / str(final_file_name + ".txt"), "w") as f:
        f.write(record["text"])
