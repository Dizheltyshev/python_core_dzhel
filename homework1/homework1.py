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