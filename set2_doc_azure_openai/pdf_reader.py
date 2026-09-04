import os

from pypdf import PdfReader


def list_documents(folder):
    files = os.listdir(folder)
    docs = []
    for f in files:
        docs.append(folder + "\\" + f)
    return docs


def read_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text = text + page.extract_text()
    return text


def read_all(folder):
    out = {}
    for d in list_documents(folder):
        out[os.path.basename(d)] = read_pdf(d)
    return out


def save_text(text, out_path):
    f = open(out_path, "w")
    f.write(text)
    f.close()
    return out_path
