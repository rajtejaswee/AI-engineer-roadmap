# Type hints in Python are syntactically similar to TypeScript, but with one huge difference: they don't do anything at runtime. 
# They're hints for humans, IDEs, and static checkers (like mypy or pyright). Python won't crash if you pass a string where an int is hinted — it just runs.

# Basic hints
def add(a: int, b: int) -> int:
    return a + b

# Variables can have hints too
name: str = "Raj"
age: int = 25

# Collections — note the lowercase, modern style
numbers: list[int] = [1, 2, 3]
mapping: dict[str, int] = {"apples": 5, "bananas": 3}
pair: tuple[str, int] = ("Raj", 25)

# A few common ones you'll see in AI code:
# "X or None" — written with |
def find_user(user_id: int) -> str | None:
    if user_id == 1:
        return "Raj"
    return None

# "Either of these types"
def parse(value: int | str) -> str:
    return str(value)

# "Any" — escape hatch when you genuinely don't know
from typing import Any
def log(data: Any) -> None:
    print(data)

# You'll see older code use Optional[str] and Union[int, str] from typing — same thing, just older syntax. Modern Python (3.10+) uses |. 

response = '{"name": "Raj", "age": 25, "email": "raj@example.com"}'

import json
data = json.loads(response)
print(data["name"])   # "Raj"
print(data["age"] + 5)   # 30