s = "aabbbbbbbbcdefffffffjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjiil"
counter = []
counter.append([]) # the first list will hold the character
counter.append([]) # the second list will hold the number of times it apears in a row

char_index = -1
counter[1].append(0)
prevc = ''
for i in s:
    print("prevc: " + prevc + "i: " + i)
    if prevc != i:
        char_index += 1
        print("char_index: " + str(char_index))
        counter[0].append(i)
        print(counter[0])
        counter[1].append(0)
        print(counter[1])
    counter[1][char_index] += 1
    prevc = i

print(counter)
print(s)
