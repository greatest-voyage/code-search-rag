import tree_sitter_python as tspy
import tree_sitter_go as tsgo
import tree_sitter_cpp as tscp
import tree_sitter_java as tsja
from tree_sitter import Language

LANG_MAP = {
    ".py": {
        "lang": "py",
        "obj": Language(tspy.language()),
        "node_types": ["function_definition", "method_definition", "class_definition"],
        "query": """
            (function_definition name: (identifier) @name) @body
            (class_definition name: (identifier) @name) @body
        """
    },
    ".go": {
        "lang": "go",
        "obj": Language(tsgo.language()),
        "node_types": ["function_declaration", "method_declaration", "class_declaration"],
        "query": """
            (function_declaration name: (identifier) @name) @body
            (method_declaration name: (field_identifier) @name) @body
        """
    }
    # ".java": {
    #     "lang": "java",
    #     "obj": Language(tsja.language()),
    #     "node_types": ["method_declaration", "class_declaration", "interface_declaration"],
    #     "query": """
    #         (function_definition name: (identifier) @name) @body
    #         (class_definition name: (identifier) @name) @body
    #     """
    # },
    # ".cpp": {
    #     "lang": "cpp",
    #     "obj": Language(tscp.language()),
    #     "node_types": ["function_definition", "method_definition", "class_definition"],
    #     "query": """
    #         (function_definition name: (identifier) @name) @body
    #         (class_definition name: (identifier) @name) @body
    #     """
    # },
}

def detect_language(file_path):
    for ext, details in LANG_MAP.items():
        if file_path.endswith(ext):
            return details
    return None

