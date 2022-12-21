print("Hello mentor")

print("Список покупок")

my_shopping_dict = {"пекарня": ["хліб", "булочки", "пончик"], "овочевий": ["морква", "селера", "рукола"]}
for k, v in my_shopping_dict.items():
  products = [product.title() for product in v]
  print(f"Я йду до магазину {k.title()}, і купую там такі товари {products}")
  sum_dict_values = sum((len(v) for v in my_shopping_dict.values()))
print(f"Я разом купую {sum_dict_values} товарів.")

first_list = [i for i in range(101)] 

second_list = [i for i in first_list if i % 5==0]
print(second_list)

third_list = [i **3 for i in first_list]
print(third_list)

print("Номер 1")
for i in range(1, 6):
    print(str(" * " * 10))
    print(str("  *" * 10))


print("Номер 2") 

print("Перший варіант") 
for i in range(0, 8, 2):
  stars = i + 2
  for i in range(2):
    print("*" * stars)

