
import os

import logging

logger = logging.getLogger(__name__)

class DirectoryLoader:
    def __init__(self, directory):
        self.directory = directory
        self.split_size = 512
        self.step_size = 128

    def load(self):
        # load all of the files in the directory recursively as text into a list of strings
        # return the list of strings
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                with open(os.path.join(root, file), 'r') as f:
                    logger.info("Loading file: %s", os.path.join(root, file))
                    yield f.read()

    def get_splits(self):
        # return a list of strings, each a substring of the text with length self.split_size
        # the last element of the list may be shorter than self.split_size
        for text in self.load():
            for i in range(0, len(text), self.step_size):
                max_size = min(self.split_size, len(text) - i)
                yield text[i:i+max_size]

    def get_split_batches(self, batch_size):
        # A generator that yields batches of splits
        # Each batch is a list of strings, each a substring of the text with length self.split_size
        # the last element of the list may be shorter than self.split_size
        splits = []
        for split in self.get_splits():
            splits.append(split)
            if len(splits) == batch_size:
                yield splits
                splits = []

        if len(splits) > 0:
            yield splits



