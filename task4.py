'''100% complete'''

menu = [
        ["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10], 
        ["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8], 
        ["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6] ]
def restraurant(): 
        print("Что пожелаете? menu/[название блюда]/add [название блюда] [Ингредиенты] [цена]/change [название блюда] [новая цена]/found [название блюда]")
        command = str(input())
        if command == "menu":
            for i in range(len(menu)):
                print(menu[i][0])
        elif command == "add":
            new_dish = str(input("Введите название нового блюда: "))
            ingredients = str(input("Введите ингредиенты через запятую: "))
            price = int(input("Введите цену блюда: "))
            new_dish_menu = []
            new_dish_menu.append(new_dish)
            new_dish_menu.append(ingredients.split(","))
            new_dish_menu.append(price)
            menu.append(new_dish_menu)
        elif command == "change":
            dish_name = str(input("Введите название блюда: "))
            price = int(input("Введите новую цену: "))
            for i in range(len(menu)):
                if menu[i][0] == dish_name:
                    menu[i][2] = price
        elif command == "found":
            dish_name = str(input("Введите название блюда: "))
            for i in range(len(menu)):
                if menu[i][0] == dish_name:
                    print(menu[i])
        restart = str(input("Что-нибудь ещё? y/n ")).lower()
        if restart == "y":
            restraurant()
        elif restart == "n":
            print("Хорошего дня <3")
            return 0
restraurant()