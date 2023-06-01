# Сушинський Ігор
# Лабораторна робота №4
# Словники

from tabulate import tabulate

my_dict = {
    "water": "вода",
    "coffee": "кава",
    "tea": "чай",
    "beer": "пиво",
    "vodka": "водка",
    "horilka": "горілка",
    "champagne": "шампанське",
    "tequila": "текіла",
    "vine": "вино",
    "cognac": "коньяк"
}

# Перевірка на наявність слова в словнику
word = input("Будь ласка, введіть слово: ")
translation = my_dict.get(word, "НЕВІДОМЕ СЛОВО")
print(translation)

# Додавання користувацького слова до словника
choice = input("Бажаєте додати нове слово до словника? Y/N\n")
while choice.lower() == 'y':
    key = input("Введіть ключ: ")
    value = input("Введіть відповідне значення: ")
    my_dict[key] = value
    choice = input("Бажаєте додати нове слово до словника? Y/N\n")

table = [["Ключ", "Значення"]] + [[key, value] for key, value in my_dict.items()]
print(tabulate(table, tablefmt="grid"))
