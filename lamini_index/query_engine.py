
from lamini import LlamaV2Runner

import logging

logger = logging.getLogger(__name__)

class QueryEngine:
    def __init__(self, index):
        self.index = index
        self.model = LlamaV2Runner()

    def answer_question(self, question):
        prompt = self._build_prompt(question)

        logger.info(f"Prompt: {prompt}")

        return self.model(prompt)

    def _build_prompt(self, question):
        most_similar = self.index.query(question, k=5)

        prompt = "\n".join(reversed(most_similar)) + "\n\n" + question

        return prompt


