
from lamini_index.lamini_index import LaminiIndex
from lamini_index.query_engine import QueryEngine

import argparse

import logging

def main():
    parser = argparse.ArgumentParser("Answer a question using Lamini Index")

    parser.add_argument("--index", type=str, default="models", help="Path to the index")
    parser.add_argument("--question", type=str, required=True, help="Question to answer")

    args = parser.parse_args()

    # Enable logging
    logging.basicConfig(level=logging.INFO)

    index = LaminiIndex.load_index(args.index)

    engine = QueryEngine(index)

    answer = engine.answer_question(args.question)

    print(f"The answer to the question: '{args.question}'")
    print(f"is: '{answer}'")

main()

