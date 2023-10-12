
import os

class DefaultChunker:
    def __init__(self, split_size=512, step_size=128):
        self.split_size = split_size
        self.step_size = step_size

    def get_splits(self, data):
        # return a list of strings, each a substring of the text with length self.split_size
        # the last element of the list may be shorter than self.split_size
        for text in data:
            for i in range(0, len(text), self.step_size):
                max_size = min(self.split_size, len(text) - i)
                yield text[i:i+max_size]

class DirectoryLoader:
    def __init__(self, directory, chunker=DefaultChunker(), verbose = True):
        self.directory = directory
        self.chunker = chunker
        self.verbose = verbose

    def load(self):
        # load all of the files in the directory recursively as text into a list of strings
        # return the list of strings
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                with open(os.path.join(root, file), 'r') as f:
                    if self.verbose: print("Loading file: ", os.path.join(root, file))
                    yield f.read()
        if self.verbose: print("Done loading file(s).")

    def get_splits(self):
        return self.chunker.get_splits(self.load())

    def get_split_batches(self, batch_size):
        # A generator that yields batches of splits
        # Each batch is a list of strings, each a substring of the text with length self.split_size
        # the last element of the list may be shorter than self.split_size
        if self.verbose: print("Splitting the data..")
        splits = []
        for split in self.get_splits():
            splits.append(split)
            if len(splits) == batch_size:
                yield splits
                splits = []

        if len(splits) > 0:
            yield splits
            if self.verbose: 
                print("Data split generated.")
                print("Number of splits: ", len(splits))

    def __iter__(self):
        return self.get_split_batches(batch_size=512)


