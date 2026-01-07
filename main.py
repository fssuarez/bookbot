import sys
from stats import words_number
from stats import get_book_text
from stats import sorted_list

if len(sys.argv)!=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
text=get_book_text(sys.argv[1])
words=words_number(text)
list= sorted_list()

print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------")
print(f"Found {words} total words")
print("--------- Character Count -------")
for i in list:
    if i["char"].isalpha():
        print(f"{i["char"]}: {i["num"]}")
    else:
        continue