import pathlib


def create_folder(folder_path):
    try:
        # Create the folder and any necessary parent directories
        pathlib.Path(folder_path).mkdir(parents=True, exist_ok=True)
        print(f"Folder created successfully at: {folder_path}")
        return {"status": "success", "message": f"Folder created at {folder_path}"}
    except Exception as e:
        print(f"Error creating folder: {e}")
        return {"status": "error", "message": f"Error creating folder: {e}"}
