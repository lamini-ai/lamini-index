
from lamini_index.directory_loader import DirectoryLoader
from lamini_index.lamini_index import LaminiIndex

import argparse

import logging

def main():

    parser = argparse.ArgumentParser(description='Build index for a given corpus')
    parser.add_argument('--corpus', default="data", help='path to the corpus')
    parser.add_argument('--index', help='path to the index')
    args = parser.parse_args()

    # Enable logging
    logging.basicConfig(level=logging.INFO)

    print('Building index for corpus: %s' % args.corpus)
    print('Index will be saved to: %s' % args.index)

    loader = DirectoryLoader(args.corpus)
    index = LaminiIndex(loader)
    index.save_index(args.index)

main()

