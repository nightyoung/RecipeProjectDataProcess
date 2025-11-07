import json

from rich.console import Console
from pdb import set_trace as pst

console = Console()

with open("recipe_corpus_full.json", "r") as infile:
    for line in infile:
        console.print(json.loads(line))
        pst()

