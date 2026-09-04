import json

import pdf_reader
import llm_extractor
import config

processed = 0
failed = 0


def process_folder(folder, results=[]):
    global processed
    docs = pdf_reader.list_documents(folder)
    for d in docs:
        processed = processed + 1
        text = pdf_reader.read_pdf(d)
        fields = llm_extractor.extract_with_retry(text)
        fields = llm_extractor.normalise(fields)
        fields["source_file"] = d
        llm_extractor.validate(fields)
        results.append(fields)
    return results


def write_output(results):
    out = config.OUTPUT_DIR + "/results.json"
    f = open(out, "w")
    json.dump(results, f)
    f.close()
    print("wrote " + str(len(results)) + " records to " + out)


def main():
    data = process_folder(config.INPUT_DIR)
    write_output(data)
    print("processed=" + str(processed) + " failed=" + str(failed))


main()
