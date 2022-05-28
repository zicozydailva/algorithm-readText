def read_file_content(filename):
    file = open(filename, 'r')

    read = file.readlines()

    # list
    lists =[]

    for lines in read:
        lists.append(lines.strip())

    cont = ""
    for sentance in lists:
        if sentance == lists[:-1]:
            cont += sentance
        else:
            cont += sentance + ' '

    return cont 

def count_words():
    text = read_file_content("story.txt")

    # dictionary
    Dic = {}

    words = text.split()

    for word in words:

        Dic[word] = words.count(word)
    
    return Dic

print(count_words().items()) #Done