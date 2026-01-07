from stats import words_number
from stats import get_book_text
from stats import sorted_list

text=get_book_text("./books/frankenstein.txt")
words=words_number(text)
list= sorted_list()
print(list)

print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")


print(f"Found {words} total words")

print("--------- Character Count -------")
for i in list:
    if i["char"].isalpha():
        print(i["char"], i["num"])
    else:
        continue