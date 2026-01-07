import sys

def get_book_text(path):
    with open(path) as text:
        file_contents=text.read()
    return file_contents

def words_number(text):
    total=0
    count=text.split()
    for words in count:
        total+=1
    return total

def letter_count():
    letters_count={}
    content=get_book_text(sys.argv[1]).lower()
    for letter in content:
        if letter not in letters_count:
            letters_count[letter]=1
        else:
            letters_count[letter]=letters_count[letter]+1
        
    return letters_count

def dict_list():
    character_list=[]
    for char, num in letter_count().items():
        character_list.append({"char": char, "num": num})    
    return character_list

def sorting(items):
    return items["num"]

def sorted_list():
    final_list=sorted(dict_list(), key=sorting, reverse=True)
    return final_list





    
