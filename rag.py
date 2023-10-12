from lamini_index.directory_loader import DirectoryLoader, DefaultChunker
from lamini_index.lamini_index import LaminiIndex
from lamini_index.query_engine import QueryEngine

loader = DirectoryLoader("data", chunker=DefaultChunker(split_size=100, step_size=15))
index = LaminiIndex(loader)
engine = QueryEngine(index)

answer = engine.answer_question("What does RDNA stand for?")
print("\n============ LLM Response ============\n")
print(answer)