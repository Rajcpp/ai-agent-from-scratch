from tools.calculator import calculate
from tools.make_file import create_file
from tools.make_folder import create_folder
from tools.product import get_product_info

tools = {
    "calculate": {
        "description": "Performs basic arithmetic operations (add, subtract, multiply, divide) on two numbers.",
        "parameters": {
            "operation": "The arithmetic operation to perform (add, subtract, multiply, divide).",
            "input1": "The first number.",
            "input2": "The second number.",
        },
    },
    "get_product_info": {
        "description": "Retrieves product information based on various filters such as category, price range, and name.",
        "parameters": {
            "product_id": "The unique identifier of the product (optional).",
            "category": "The category to filter products by (optional).",
            "min_price": "The minimum price to filter products by (optional).",
            "max_price": "The maximum price to filter products by (optional).",
            "name": "A substring to search for in product names (optional).",
        },
    },
}

tools_functions = {
    "calculate": calculate,
    "get_product_info": get_product_info,
    "create_file": create_file,
    "create_folder": create_folder,
}

tools_inputs = {
    "calculate": {
        "operation": str,
        "input1": float,
        "input2": float,
    },
    "get_product_info": {
        "product_id": str,
        "category": str,
        "min_price": float,
        "max_price": float,
        "name": str,
    },
    "create_file": {
        "filename": str,
        "content": str,
    },
    "create_folder": {
        "folder_name": str,
    },
}
