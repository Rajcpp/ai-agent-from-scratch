import pathlib


def create_file(file_path, content=""):
    try:
        path = pathlib.Path(file_path)

        # Create directories + file
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)

        if content:
            with open(path, "w") as f:
                f.write(content)

        file_name = path.name

        # print(f"File '{file_name}' created successfully at: {file_path}")

        return {
            "status": "success",
            "file_name": file_name,
            "message": f"File '{file_name}' created at {file_path}",
        }

    except Exception as e:
        print(f"Error creating file: {e}")
        return {"status": "error", "message": f"Error creating file: {e}"}
