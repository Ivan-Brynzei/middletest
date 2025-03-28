def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {file_path} not found!")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""
