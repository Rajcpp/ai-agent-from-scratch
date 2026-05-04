from config import tools_functions
from core.fake_llm import llm as fake_llm
from core.input_handler import get_user_command


def main():
    while True:
        response: dict = fake_llm(get_user_command())
        if response is None:
            continue
        action = response["action"]
        parameters = response["parameters"]
        if action in tools_functions:
            result = tools_functions[action](**parameters)
            print(f"Result: {result}")
        elif action == "FINISH":
            print("Finishing the session. Goodbye!")
            break
        else:
            print("Error: Unsupported action.")
        print("-" * 40)
        print("llm response:", response)
        print("-" * 40)
        print("tool_response:", result)
        print("-" * 40)


if __name__ == "__main__":
    main()
