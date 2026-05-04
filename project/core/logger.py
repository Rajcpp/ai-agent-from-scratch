import os

from loguru import logger

os.makedirs("logs", exist_ok=True)
logger.remove()
logger.add("logs/app.log", level="INFO", format="{time} | {level} | {message}")
logger.add(
    "logs/debug.log",
    level="DEBUG",
    format="{time} | {level} | {extra[source]} | {message}",
)

llm_logger = logger.bind(source="LLM")
tool_logger = logger.bind(source="TOOL")
memory_logger = logger.bind(source="MEMORY")
