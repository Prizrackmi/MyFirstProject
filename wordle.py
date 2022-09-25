class Unlocal:
    x = 'y'
    hidden_word = ()



def random_word():
    import random
    with open(r"wordle_dict.txt", 'r') as hidden_w:
        # for line in hidden_w:
        lines = hidden_w.readlines()
        # rand_word()
        random_line = random.choice(lines) if lines else None
        random_line = random_line.rstrip('\n')
        if len(random_line) == 5:
            Unlocal.hidden_word = random_line.lower()
            # TEST
            # print(Unlocal.hidden_word )
        else:
            print("pfuhepbnt ckjdfhm")



def wordle_func():
    '''

    :return: None
    '''


    word = input("Угадайте слово из пяти букв:\n")
    while len(word) != 5:
        print("ошибка, слово из 5 букв")
        word = input()
    else:
        if word == Unlocal.hidden_word:
            print("Поздравляем! Вы угадали!\n повторить? (y/n)")
            random_word()
            Unlocal.x = input("continie y/n")
            while Unlocal.x.lower() == 'y':
                wordle_func()
            else:
                Unlocal.x = 'n'
                # print('Game over. \n Thank you, bye :) ')
            return

        else:
            # цикл поиска "коров"
            res_0 = '0' if word[0] in Unlocal.hidden_word else '-'
            # for letter in hidden_word:
            #     if letter == word[0]:
            #         res_0 = "0"
            res_1 = '0' if word[1] in Unlocal.hidden_word else '-'
            res_2 = '0' if word[2] in Unlocal.hidden_word else '-'
            res_3 = '0' if word[3] in Unlocal.hidden_word else '-'
            res_4 = '0' if word[4] in Unlocal.hidden_word else '-'

            #         цикл "быков"

            if word[0] == Unlocal.hidden_word[0]:
                    res_0 = "+"
            if word[1] == Unlocal.hidden_word[1]:
                    res_1 = "+"
            if word[2] == Unlocal.hidden_word[2]:
                    res_2 = "+"
            if word[3] == Unlocal.hidden_word[3]:
                    res_3 = "+"
            if word[4] == Unlocal.hidden_word[4]:
                res_4 = "+"
            print(res_0 + res_1 + res_2 + res_3 + res_4)
    wordle_func()




print("Правила:\n - такой буквы нет\n + буква на своем мете \n 0 - буква не на своем месте")
random_word()

while Unlocal.x == 'y':
        wordle_func()

print('Game over. \n Thank you, bye :) ')