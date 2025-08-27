with open('books/frankenstein.txt') as f:
    file_contents=f.read()

def get_num_words():
    num_words=len(file_contents.split())
    return num_words

def get_char_count():
    char_count={}
    for i in file_contents:
        i=i.lower()
        try:
            char_count[i]+=1
        except:
            char_count[i]=1
    return print(char_count)
