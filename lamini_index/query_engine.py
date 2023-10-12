
from lamini import LlamaV2Runner

import logging

logger = logging.getLogger(__name__)

class QueryEngine:
    def __init__(self, index, verbose=True):
        self.index = index
        self.model = LlamaV2Runner()
        self.verbose = verbose

    def answer_question(self, question, top_k=5):
        if self.verbose:
            print("\n============ Input Query============\n")
            print(question)

        prompt = self._build_prompt(question, top_k)

        if self.verbose:
            print("\n============ RAG Prompt============\n")
            print(prompt)

        return self.model(prompt)

    def _build_prompt(self, question, top_k=5):
        most_similar = self.index.query(question, top_k)

        prompt = "\n".join(reversed(most_similar)) + "\n\n" + question

        if self.verbose: 
            print("\n============ Most similar documents ============\n")
            print(most_similar)
        
        return prompt


