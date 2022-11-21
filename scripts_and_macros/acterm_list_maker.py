import json
import argparse
import logging
from json import JSONDecodeError
import os
from chardet import detect

logging.basicConfig(filename='acterm_list_maker.log', encoding='utf-8', level=logging.INFO, style='{', datefmt='%Y-%m-%d %H:%M:%S', format='{asctime} {levelname} {filename}:{lineno}: {message}')

def get_encoding_type(path):
    with open(path, 'rb') as f:
        rawdata = f.read()
    logging.info(f"File {path} encoded with {detect(rawdata)['encoding']}")
    return detect(rawdata)['encoding']

def encode_file(path, source_encoding):
    try:
        with open(path, 'r', encoding=source_encoding) as f, open("temp.txt", 'w', encoding='utf-8') as e:
            text = f.read()
            e.write(text)

        os.remove(path)
        os.rename("temp.txt", path)
        logging.info(f"File decoded from {source_encoding} to utf-8")
    except UnicodeDecodeError:
        logging.exception('Decode Error')
    except UnicodeEncodeError:
        logging.exception('Encode Error')

def read_dic(path):
    try:
        with open(path, encoding='utf-8') as file:
            data = json.load(file)
        return data

    except FileNotFoundError:
        logging.error(f"File {path} not found in the directory")

    except JSONDecodeError:
        logging.exception(f"Dic file {path} contains formating error, missing commas or quotes")


def read_file(path):

    try:
        with open(path, encoding='utf-8') as file:
            data = [line.rstrip() for line in file.readlines()]
        return data

    except FileNotFoundError:
        logging.error("File not found in the directory")


def get_definition(dicts, input_file, format_flag):
    terms_list = read_file(input_file)

    result = []
    for dic in dicts:
        dic_data = read_dic(dic)
        if dic_data:
            i = 0
            while i < len(terms_list):
                logging.info(f"Dic file: {dic}, term is {terms_list[i]}")
                logging.debug(f"Current dic content: {list(d for d in dic_data)}")
                logging.debug("Using in: true" if terms_list[i] in list(d for d in dic_data) else "Using in: false")
                logging.debug("Using any: true" if any(terms_list[i] in d for d in dic_data) else "Using any: false")

                if terms_list[i] in list(d for d in dic_data):
                    if format_flag == "gd":
                        result.append(f"| {terms_list[i]} | --- | {dic_data[terms_list[i]]} |")
                    elif format_flag == "mkdocs":
                        result.append(f"*[{terms_list[i]}]: {dic_data[terms_list[i]]}")

                    del terms_list[i]
                else:
                    i += 1
        else:
            logging.error(f"Could not parse dictionary {dic} file!")

    for t in terms_list:
        result.append(f"| {t} | --- |  |")

    result = list(set(result))
    result.sort()
    return result


def write_file(result, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        for line in result:
            f.write(f"{line}\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Definition table builder",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input", type=str, default="abbreviations.txt",
                        help="Path to file with terms, each term on new line")
    parser.add_argument("-d", "--dics", type=str, default="acronyms/common.dic,acronyms/ml.dic",
                        help="Path to output file")
    parser.add_argument("-o", "--output", type=str, default="abbreviations.md",
                        help="Path to output file")
    parser.add_argument("-f", "--format", type=str, default="gd",
                        help="Format for output file: gd - gostdown, mkdocs - mkdocs")
    args = vars(parser.parse_args())

    logging.info(f"******** New acterm task started ********")
    logging.info(f"Input: {args['input']}, dics: {args['dics'].split(',')}")

    source_encoding = get_encoding_type(args["input"])
    if source_encoding != "utf-8":
        encode_file(args["input"], source_encoding)

    list_of_dics = args["dics"].split(",")
    write_file(get_definition(list_of_dics, args["input"],args["format"]), args["output"])
