# Install lamini-index

```bash
pip install lamini
```

```bash
git clone git@github.com:lamini-ai/lamini-index.git
```

```bash
cd lamini-index
```

# Answer questions using a Lamini Index

```python
from lamini_index.directory_loader import DirectoryLoader
from lamini_index.lamini_index import LaminiIndex
from lamini_index.query_engine import QueryEngine

loader = DirectoryLoader("data")
index = LaminiIndex(loader)
engine = QueryEngine(index)

answer = engine.answer_question("Who won the case above?")

```

```
The court ruled in favor of Dana and Linda Phillabaum, the defendants and appellees,
in the foreclosure action brought against them by Wells Fargo.
```
