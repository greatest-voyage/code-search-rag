from dataclasses import dataclass

@dataclass
class Symbol:
    code: str
    file: str
    language: str
    name: str
