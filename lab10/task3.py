file6 = open('C:/Users/619/Desktop/СибГУТИ/Информатика/lab10/file6.txt', 'r')
f6 = file6.read().split()
total_words = len(f6)
e_cnt = 0
for word in f6:
    if 'e' in word:
        e_cnt += 1
print("% слов содержащих букву e = ",  e_cnt/total_words*100)