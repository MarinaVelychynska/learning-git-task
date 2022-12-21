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

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = [number**3 for number in numbers]
print(results)

for i in range(5, 0, -1):
  print("*" * i)
