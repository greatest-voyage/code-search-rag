import os

from src.storage.schema import Symbol
from src.utils.language import detect_language
from tree_sitter import QueryCursor, Parser

class TreeSitterChunker:
    def chunk_repo(self, repo_path: str):
        all_symbols = []
        # print("repo_path:", repo_path)

        for root, _, files in os.walk(repo_path):
            # print("root:", root)
            for f in files:
                path = os.path.join(root, f)
                symbols = self.chunk_file(path)
                if symbols:
                    all_symbols.extend(symbols)

        return all_symbols

    def chunk_file(self, file_path):
        details = detect_language(file_path)
        # print(f"details: {details}")
        # print(f"file_path: {file_path}")
        if not details:
            print(f"lang not found {file_path}")
            return None

        lang_obj = details["obj"]
        parser = Parser(lang_obj)
        if not parser:
            print('parser not found')
            return None

        with open(file_path, "rb") as f:
            code_bytes = f.read()
        # print(code_bytes)
        tree = parser.parse(code_bytes)
        query = lang_obj.query(details["query"])
        cursor = QueryCursor(query)
        captures = cursor.matches(tree.root_node)

        # print(f"root {root}")

        symbols = []

        for pattern_index, match in captures:
            # print("Invoked")
            # In modern tree-sitter, match is a dict where keys are tag names
            # and values are LISTS of nodes (because a pattern can have multiple captures)
            if "name" in match and "body" in match:
                name_node = match["name"][0]
                body_node = match["body"][0]

                name = code_bytes[name_node.start_byte:name_node.end_byte].decode("utf-8")
                body = code_bytes[body_node.start_byte:body_node.end_byte].decode("utf-8")

                # print(name, body)

                symbols.append(Symbol(
                    code = body,
                    file = file_path,
                    language = details["lang"],
                    name = name
                ))

        return symbols
