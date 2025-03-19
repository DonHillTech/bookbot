def get_num_words(content):
    return len(content.split())

def get_book_text(file_path):
    file_content = ""
    with open(file_path) as file:
        print(f"Analyzing book found at {file_path}...")
        file_content = file.read()
    return file_content

def get_character_counts(content):
    dict = {}
    words = content.split()
    for word in words:
        for char in word.lower():
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
    return dict

def organize_dict(dict):
    s_list = sorted(dict, key=lambda item: dict[item], reverse=True)
    for item in s_list:
        print(f"{item}: {dict[item]}")
