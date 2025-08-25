def word_count(file_contents):
    words = file_contents.split()
    return len(words)


def char_count(file_contents):
    fin_char_count = {}
    lowered = file_contents.lower()
    for letter in lowered:
        if letter in "abcdefghijklmnopqrstuvwxyz.,!?;:\"'()[]{}":
            fin_char_count[letter] = fin_char_count.get(letter, 0) + 1
    return fin_char_count
def sort_char_count(fin_char_count):
    char_list = []
    for key,value in fin_char_count.items():
        list_dict = {"char": key, "num": value}
        char_list.append(list_dict)
    char_list.sort(key=lambda x: x["num"], reverse=True)    
    return char_list



   