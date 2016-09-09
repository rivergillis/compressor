s = "aabbbbbbbbcdefffffffjjjjjjjjjjjjjj      jjjjj 1110000000101011111 jjjjjjjjjjjjjjjjjjjjjjjjjjiil"
counter = []
counter.append([]) # the first list will hold the character
counter.append([]) # the second list will hold the number of times it apears in a row

char_index = -1
counter[1].append(0)
prevc = ''
for i in s:
    if prevc != i:
        char_index += 1
        counter[0].append(i)
        counter[1].append(0)
    counter[1][char_index] += 1
    prevc = i

# create compressed string
compressed = ""
for i,c in enumerate(counter[0]):
    # no point in compressing for two or less repeats
    if counter[1][i] > 2:
        compressed += (c + str(counter[1][i]))
    else:
        compressed += c*int(counter[1][i])
print(counter)
print(s)

print(compressed)
