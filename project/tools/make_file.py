import pathlib


def create_file(file_path, content=""):
    try:
        # Create the file and any necessary parent directories
        pathlib.Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        pathlib.Path(file_path).touch(exist_ok=True)
        if content:
            with open(file_path, "w") as f:
                f.write(content)
        print(f"File created successfully at: {file_path}")
        return {"status": "success", "message": f"File created at {file_path}"}
    except Exception as e:
        print(f"Error creating file: {e}")
        return {"status": "error", "message": f"Error creating file: {e}"}
