[![PyPI - Python](https://img.shields.io/badge/python-v3.8+-blue.svg)](https://pypi.org/project/pylineage/)
[![PyPI - PyPi](https://img.shields.io/pypi/v/pylineage)](https://pypi.org/project/pylineage/)
[![PyPI - License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/jasperpaalman/pylineage/blob/master/LICENSE)

# pylineage
This package provides simple tools for parsing and visualizing your .sql scripts.

## Installation

The package is distributed through PyPI, and can be installed with

```bash
pip install pylineage
```

In order to create a lineage graph you should also install and add [Graphviz](https://graphviz.org/download/) to your Path. 

## SQL Parser

Individual basic .sql scripts can be parsed by running

```python
from pylineage import SqlParser

parser = SqlParser()
query = """

SELECT column1
     , column2 AS c2
FROM my_table t
WHERE column1 = 1

"""

parsed = parser.parse(query)
```

The output looks as follows

```python
>>> parsed

{
  "select": [{ "content": "column1" }, { "content": "column2", "alias": "c2" }],
  "from": { "content": "my_table", "alias": "t" },
  "where": ["column1 = 1"]
}
```

Currently the parser supports the clauses

| Clause           |
|------------------|
| SELECT           |
| FROM             |
| LEFT JOIN        |
| LEFT OUTER JOIN  |
| RIGHT JOIN       |
| RIGHT OUTER JOIN |
| FULL JOIN        |
| FULL OUTER JOIN  |
| JOIN             |
| INNER JOIN       |
| WHERE            |
| QUALIFY          |
| GROUP BY         |
| ORDER BY         |
| HAVING           |
## Lineage Graph

Based on the SQL parser, a lineage graph can be constructed. 
We start off with the main constructor:

```python

from pylineage import LineageGraph

lineage_graph = LineageGraph()
```

Subsequently, there are two options of adding SQL scripts: (1) as individual input strings or (2) as directory.

```python

lineage_graph.extend_graph_from_input_string("CREATE TABLE my_view AS SELECT column1 FROM my_table")

lineage_graph.extend_graph_from_directory("/data")

```

The graph can be cleared at any time by running

```python
lineage_graph.clear_graph()
```

One purpose of parsing and visualizing is to obtain execution order. This can be obtained by running

```python
lineage_graph.get_execution_order()
```

**NOTE**</br>
Any inner query that is not a part of a source clause (FROM / JOIN) is not included as a node in the graph. As such, statements like the one below are not taken into account.

```sql
...
WHERE column not in (
  SELECT column
  FROM table2
)
```

Finally the Lineage Graph can be accessed by directly checking

```python
lineage_graph.graph
```

or by running it in interactive mode:

```python
lineage_graph.serve_graph()
```

The interactive mode offers convenient highlighting and dragging capabilities.

<img src="images/interactive_graph.gif" width="80%"/>