def main():
    with open('books/frankenstein.txt', 'r') as f:
        text = f.read()
        word = text.split()
        print(str(len(word)) +' number of words')

    soup_count = {}
    word_lower = text.lower()
    for letter in word_lower:
        if letter not in soup_count:
            soup_count[letter] = 1
        else:
            soup_count[letter] += 1
    soup_count = sorted(soup_count.items())
    soup_count = dict(soup_count)

    list_o_dict = []
    for key, value in soup_count.items():
        if key.isalpha():
            list_o_dict.append({'char':key, 'num': value})
    for dic in list_o_dict:
        print(f"The {dic['char']} character was found {dic['num']} times")



main()