def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print("----- Report of Frankenstein text -----")
    count_words(file_contents)
    count_letters(file_contents)
    print("--- End Report ---")

def sort_on(dict):
    return dict["num"]

def count_words(file):
    words = file.split()
    count = 0
    for word in words:
        count +=1
    print(f"{count} words found in the document")

def count_letters(file):
    text = file.lower()
    letter_count = []
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in letters:
        count = 0
        for character in text:
            if character == letter:
                count +=1
        format = {"letter":letter, "num":count}
        letter_count.append(format)
    letter_count.sort(reverse = True, key = sort_on)
    for item in letter_count:
        char = item["letter"]
        num = item["num"]
        print(f"The letter {char} was found {num} times")

main()