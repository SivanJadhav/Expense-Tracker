import json

def load_json(file_name: str):
    # Try to open the file
    try:
        with open(file_name, "r") as file:
            return json.load(file)

    # Handle FileNotFounError: where file does not exist
    except FileNotFoundError:
        print("File was not found.")
        return []

    # Handle JSONDecodeError: where file exists but cannot be decoded
    except json.JSONDecodeError:
        print("File cannot be decoded; invalid JSON data.")
        return []
        
    # Handle PermissionError: where file exists but we don't have permission
    except PermissionError:
        print("Not enough permissions to access file.")
        return []

    # Handle OSError: any operating system error
    except OSError:
        print("Opearting System error.")
        return []


def save_json(file_name: str, data: list[dict], indent: int):
    # Try to open the file
    try:
        with open(file_name, "w") as file:
            json.dump(data, file, indent=indent)
            return 0

    # Handle FileNotFounError: where file does not exist
    except FileNotFoundError:
        print("File was not found.")

    # Handle JSONDecodeError: where file exists but cannot be decoded
    except json.JSONDecodeError:
        print("File cannot be decoded; invalid JSON data.")

    # Handle PermissionError: where file exists but we don't have permission
    except PermissionError:
        print("Not enough permissions to access file.")

    # Handle OSError: any operating system error
    except OSError:
        print("Opearting System error.")
