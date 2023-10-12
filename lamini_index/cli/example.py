
from lamini_index.retrieval_augmented_runner import RetrievalAugmentedRunner

import logging

# Enable logging
logging.basicConfig(level=logging.INFO)

corpus = 'data'

print('Building index for corpus: %s' % corpus)

local_config = {
    "production": {
        "key": "test_token",
        "url": "http://api:8000",
    }
}

staging_config = {
    "production": {
        "key": "c4f0834ec7bbedde1822e1ae0ba2abaa9999728d",
        "url": "https://api.staging.powerml.co",
    }
}

config = {}

# Create a LaminiRagRunner object
runner = RetrievalAugmentedRunner(config=config, k=4, batch_size=512, chunk_size=256, step_size=64)

runner.load_data(corpus)

# Train the model
runner.train()

# Evaluate the model
questions = [
        "Who is Dana Phillabaum?",
        "Who is the original lender in the Wells fargo case?",
        "What is Merlin's doctrine?",
        "What is Flower's, Inc.?",
        "Who succeeded in the case involving Flower's, Inc.?",
        "Who were the attorneys in the case involving Flower's, Inc. for the sec of the dept of rev?",
        ]

for question in questions:
    print('Question: %s' % question)
    print('Answer: %s' % runner(question))

