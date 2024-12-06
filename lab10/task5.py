with open('C:/Users/619/Desktop/СибГУТИ/Информатика/lab10/task5file.txt', 'r') as f5:
    lines = f5.readlines()
    middle = len(lines) // 2
    new_string = str(input("Введите строку: "))
    lines.insert(middle, new_string+'\n')
with open('C:/Users/619/Desktop/СибГУТИ/Информатика/lab10/task5file.txt', 'w') as f5:    
    f5.writelines(lines)