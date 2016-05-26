import os
import re


def parse_directory(dirname, label):
    """
    Parses an entire directory of text files, making a list entry for each
    file. For use if everything in a directory is the same class.

    Params:
        dirname (str): Full path to a directory
        label (str): The label of all the documents in directory dirname
    """
    records = []
    d = dirname.encode('unicode_escape')
    for f in os.listdir(d):
        path = os.path.join(d, f)
        if os.path.isfile(path):
            records.append(parse_file(f, path, label))
    return records


def parse_file(fname, path, label):
    """
    Parses a single file f into a record with text and a set of words.

    Params:
        f (str): Full path to a file
        label (str): The label of the document in file f
    """
    record = {'class': label}
    f = open(path, 'r')
    record['attribute'] = extract_words(f)
    record['name'] = fname.decode("utf-8")
    return record


def extract_words(f):
    """
    Takes a string f of words and parses them into a list of words.
    """
    text = []
    try:
        for line in f:
            text += re.sub("[^\w]", " ", line).split()
    except UnicodeDecodeError:
        pass
    return set(text)
