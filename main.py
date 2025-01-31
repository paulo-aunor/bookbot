def main():
    book_path = "books/frankenstein.txt"
    book_content = read_file(book_path)
    word_count = count_words(book_content)
    letter_number_dict = get_character_count(book_content)
    sorted_dict = get_sorted_list(letter_number_dict)
    print("--- Begin Report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    for dict in sorted_dict:
        if not dict["char"].isalpha():
            continue
        print(f"The '{dict["char"]}' character was found {dict["num"]}")  

    print("--- End Report ---")


def read_file(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def sort_on(d):
    return d["num"]

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def get_character_count(book_content):
    letter_number = {}
    lowered_text = book_content.lower()
    for letter in lowered_text:
        if letter in letter_number:
            letter_number[letter] += 1
        else:
            letter_number[letter] = 1
    return letter_number

def get_sorted_list(letter_number_dict):
    sorted_list = []
    for char in letter_number_dict:
        sorted_list.append({"char":char, "num":letter_number_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()