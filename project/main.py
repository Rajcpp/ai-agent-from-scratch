from config import tools_functions
from core.fake_llm import llm as fake_llm
from core.input_handler import get_user_command
from core.logger import llm_logger, memory_logger, system_logger, tool_logger


def main():
    system_logger.info("started")
    memory = []
    while True:
        response: dict | None = fake_llm(get_user_command())
        llm_logger.info(response)
        if response is None:
            continue

        action = response["action"]
        parameters = response["parameters"]

        if action in tools_functions:
            result = tools_functions[action](**parameters)
            tool_logger.info(result)

        elif action == "FINISH":
            result = "Task finished"
            memory.append({"llm_response": response, "tool_response": result})
            system_logger.info("finished")
            break

        else:
            result = "Unsupported action"
            system_logger.error("action not in tools")

        memory.append({"llm_response": response, "tool_response": result})
        memory_logger.info({"llm_response": response, "tool_response": result})
    print(memory)


if __name__ == "__main__":
    main()
