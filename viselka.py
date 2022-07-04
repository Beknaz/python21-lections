import random
HANGMAN = (
"""
------
|    |
|
|
|
|
|
|
|
--------
""",
"""
------
|    |
|    O  |
|
|
|
|
|
|
--------
""",
"""
------
|    |
|    O
|   -+-
|
|
|
|
|
--------
""",
"""
------
|    |
|    O
|  /-+-/
|
|
|
|
|
--------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|
|
|
|
--------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|    |
|   |
|   |
|
--------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|    |
|   | |
|   | |
|
--------
"""
)
MAX_WRONG = 6
WORDS = ("СТОЛОВКА", "РЕСТОРАН", "ШКОЛА", "СПРАВКА", "АНЕКДОТ", "ЗАВТРАК", "БИЗНЕС", "ЛИМОНАД", "НОУТБУК", "ПЛАНШЕТ", "ДИНОЗАВР", "ИНТЕРАКТИВ", "ПИРАТ", "СИЛЬНЫЙ", "БУРАТИНО", "ВОДА", "КОСМОНАВТ", "БАНАЛЬНОСТЬ", "КРЕПКИЙ", "КЛАВИАТУРА", "ПОДОКОННИК", "КОМПЬЮТЕР", "СИЛАЧ", "ТЕЛЕФОН", "ЗМЕЯ", "КРЕСЛО", "ПОКРЫВАЛО", "ПТИЦА", "РЫБА", "ИНСТАГРАМ", "КОД", "ПИТОН")
oshibki = 6
popytki = 0
wrong = 0 
used = [] 
s=1
print("\t\tДобро пожаловать в игру 'Виселица'!")
while s==1:
    otvet = input('Хотите ли вы сыграть? Да или Нет:' )
    if otvet.lower() == 'да':
        print('вас есть всего 6 жизней')
        word = random.choice(WORDS) 
        so_far = "*" * len(word) 
        # можно указать ошибки == 0. цикл закроется если попытки закончатся. или же слово будет угадано. попытки считают по неудачным вводам. т.е. если данной буквы нет в слове.
        while wrong < MAX_WRONG and so_far != word:
            print(HANGMAN[wrong])
            print("\nВы уже предлагали следующие буквы:\n", used)
            print("\nОтгаданное вами в слове сейчас выглядит так:\n", so_far)
            guess = input("\n\nВведите букву: ").upper()
            while guess in used:
                print("Вы уже предлагали букву: ", guess)
                guess1 = input("\n\nВведите букву: ").upper()
            used.append(guess)
            if guess in word:
                print("\nДа! Буква", guess, "есть в слове!")
                new = ""
                popytki += 1
                for i in range(len(word)):
                    if guess == word[i]:
                        new += guess
                    else:
                        new += so_far[i]
                so_far = new
            else:
                print("\nК сожалению, буквы", guess, "нет в слове.")
                wrong += 1
                oshibki -= 1
                popytki += 1
                print("У вас осталок", oshibki, "жизней")
        if wrong == MAX_WRONG:
            print(HANGMAN[wrong])
            print("\nЧеловеска повесили!")
            print("Загаданное слово было", word)
            oshibki = 6
            popytki = 0
            used = []
            wrong = 0 
        else:
            print("\nВы отгадали!")
            print("\nБыло загаданно слово", word, ".")
            print('Вы использовали',popytki, 'попыток')
            oshibki = 6
            popytki = 0
            used = []
            wrong = 0 
    elif otvet.lower() == 'нет':
        print('До скорой встречи')
        break
    else:
        questions = ("ДА или НЕТ???", 
        "Ты читать не умеешь?!\nЕсли хочешь сыграть пиши - ДА\nЕсли не хочешь - НЕТ", 
        "Так ДА или НЕТ?!")
        random_q = random.choice(questions)
        print(random_q)

