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

def word_frequency(text):
    words = text.lower().split()
    freq_dict = {}
    
    for word in words:
        word = word.strip('.,!?():;"\'')
        if word:
            freq_dict[word] = freq_dict.get(word, 0) + 1
            
    return freq_dict
