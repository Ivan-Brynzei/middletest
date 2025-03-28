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

def top_frequent_words(freq_dict, top_n=10):
    sorted_words = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:top_n]

def save_results(top_words, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for word, count in top_words:
                file.write(f"{word}-{count}\n")
        print(f"Results saved to {output_file}")
    except Exception as e:
        print(f"Error writing to file: {e}")

def process_file(input_file, output_file):
    text = read_text_file(input_file)
    if not text:
        return
    
    word_freq = word_frequency(text)
    top_words = top_frequent_words(word_freq)
    save_results(top_words, output_file)

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    process_file(input_file, output_file)