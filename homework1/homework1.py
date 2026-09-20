# 1. Привести к целому типу -1.6, 2.99
a = -1.6
b = 2.99

print(int(a))
print(int(b))

# 2. Заменить символ "#" на символ "/" в строке: www.my_site.com#about
site = 'www.my_site.com#about'
new_site = site.replace ("#" , "/")

print(new_site)

# 3. Напишите программу, которая добавляет "ing" к слову "stroka"
word = 'stroka'
new_word = word + 'ing'

print(new_word)

# 4. В строке "Ivanou Ivan" поменяйте местами слова: "Ivanou Ivan" => "Ivan Ivanou"
name = 'Ivanou Ivan'
replace = name.replace ('Ivanou Ivan', 'Ivan Ivanou')

print(replace)

# 5. Напишите программу, которая удаляет пробел в начале и в конце строки
title = ' Мальчик в полосатой пижаме '

print(title.strip())

# 6. Создайте словарь, связав его с переменной school, и наполните его данными
school = {
    "1а": 22,
    "1б": 25,
    "2в": 21,
    "3г": 26,
    "4а": 28,
    "5в": 21,
    "6б": 22,
    "7б": 24,
    "8а": 25,
    "9а": 28,
}

print(school)

# 7. Создайте список и извлеките из него с помощью среза второй элемент
colours = ["red", "blue", "white", "yellow"]

print(colours [1:2])

# 8. Вывести, входит ли строка1 в строку2
word1 = 'employ'
word2 = 'employment'

print(word1 in word2)

# 9. Вывести нужные символы
x = "My name is Agent Smith"

print(x[1])  # y
print(x[3:16:3])  # nesgt