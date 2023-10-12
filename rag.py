from lamini_index.directory_loader import DirectoryLoader
from lamini_index.lamini_index import LaminiIndex
from lamini_index.query_engine import QueryEngine

loader = DirectoryLoader("data")
index = LaminiIndex(loader)
engine = QueryEngine(index)

answer = engine.answer_question("Who won the case above about dana and wells fargo?")
print("\n============ LLM Response ============\n")
print(answer)