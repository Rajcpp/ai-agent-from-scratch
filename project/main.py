from config import tools_functions
from core.fake_llm import llm as fake_llm
from core.input_handler import get_user_command


def main():
    memory = []
    while True:
        response: dict | None = fake_llm(get_user_command())
        if response is None:
            continue

        action = response["action"]
        parameters = response["parameters"]

        if action in tools_functions:
            result = tools_functions[action](**parameters)
            # print(f"Result: {result}")

        elif action == "FINISH":
            result = "Task finished"
            memory.append({"llm_response": response, "tool_response": result})
            # print("Finishing the session. Goodbye!")
            break

        else:
            result = "Unsupported action"
            # print("Error: Unsupported action.")

        memory.append({"llm_response": response, "tool_response": result})
        memory.append({"llm_response": response, "tool_response": result})

    print(memory)


if __name__ == "__main__":
    main()
