from tomlkit import load, dumps
import sys

doc = load(open("pyproject.toml","r"))
doc["project"]["version"]
doc["project"]["version"] = sys.argv[1]
with open("pyproject.toml", "w") as f:
    f.write(dumps(doc))