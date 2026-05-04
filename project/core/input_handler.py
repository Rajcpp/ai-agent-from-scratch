from config import tools, tools_inputs
from core.validator import convert_value


def get_user_command() -> dict | None:
    action = input("Enter the action you want to perform (e.g., calculate): ")

    if action == "FINISH":
        return {"action": "FINISH", "parameters": {}}

    if action not in tools:
        print("Error: Unsupported action.")
        return None

    parameters = {}

    for param in tools_inputs[action]:
        value = input(f"Enter value for {param} (or leave blank to skip): ")
        converted_value = convert_value(value, tools_inputs[action][param])
        if value:
            parameters[param] = converted_value

    command = {"action": action, "parameters": parameters}
    return command
