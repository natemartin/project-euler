def get_word_score(pos, word):
    total = 0
    for i in range(0,len(word)):
        total+= (ord(word[i]) - 64)
    return total * pos

with open('names.txt') as f:
    content = eval(str(f.readlines()[0].split(',')))
content.sort()
total = 0
for i in range(0, len(content)):
    total+=get_word_score(i+1, content[i].replace('\"',''))
print total
