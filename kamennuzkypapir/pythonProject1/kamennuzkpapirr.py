import random
again_input = 1
while again_input == 1:
    user_input = input("1. kamen:\n2.nuzky:\n3.papir:\nzadejte:")
    num = random.randint(1,3)
    pocitac = 0
    if num == 1:
        pocitac = "kamen"
    elif num == 2:
        pocitac = "nuzky"
    else:
        pocitac = "papir"
    print(f"pocitac zvolil {pocitac}")
    if int(user_input) == num:
        print("remiza")
    elif int(user_input) == 1 and num == 2 or int(user_input) == 2 and num == 3 or int(user_input) == 3 and num == 1:
        print("vyhral jsi")
    elif int(user_input) == 1 and num == 3 or int(user_input) == 2 and num == 1 or int(user_input) == 3 and num == 2:
        print("prohral jsi")
    again_input = input("pro ukoonceni zmackni \";\" pro pokracovani cokoliv jineho");
    if again_input == ";":
        again_input = 0
    else:
        again_input = 1