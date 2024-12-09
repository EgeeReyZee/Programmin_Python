mesCount = int(input('Введите количество сообщений: '))
QuestAns = str(input('Введите порядок вопрос/ответов: ')).upper()

questions = 0
answers = 0
if QuestAns[0] == 'Q' and mesCount == len(QuestAns):
    for i in QuestAns:
        if i == "Q":
            questions += 1
        elif i == "A":
            answers += 1
    if questions > answers:
        print('-')
    elif answers >= questions:
        print('+')
else:
    print('-')