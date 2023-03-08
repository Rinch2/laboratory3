slovo = input()
a = str(slovo)

if a.isalpha() == False:
    print("Введите другое слово! ")
    exit()

if a.find('ф') == -1:
    print("Эх, это не очень редкое слово...")
else:
    print("Ого! Это редкое слово!")