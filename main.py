def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_printout(book_path)
    words_len = get_print_words(book_text)
    letter_number_dict = get_letter_number_dict(book_text)
    letter_number_sorted_list = get_dict_list(letter_number_dict)

    print(f"***Book Report for {book_path}***")
    print(f"The number of words in this book is: {words_len}")
    
    for dict in letter_number_sorted_list:
        if not dict["char"].isalpha():
            continue
        print(f"The character {dict["char"]} appeared {dict["num"]} times!")
    
    print("***END REPORT***")

def get_book_printout(book_path):
    with open(book_path) as f:
        return f.read()

def sort_on(d):
    return d["num"]

def get_print_words(book_text):
    words_list = book_text.split()
    return len(words_list)

def get_letter_number_dict(book_text):
    letter_number = {}
    lowered_text = book_text.lower()
    
    for letter in lowered_text:
        if letter in letter_number:
            letter_number[letter] += 1
        else:
            letter_number[letter] = 1
    return letter_number

def get_dict_list(char_list):
    sorted_list = []
    for char in char_list:
        sorted_list.append({"char":char, "num":char_list[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()