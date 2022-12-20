print("Список покупок")
my_shopping_dict = {"пекарня": ["хліб", "булочки", "пончик"], "овочевий": ["морква", "селера", "рукола"]}
for k, v in my_shopping_dict.items():
  products = [product.title() for product in v]
  print(f"Я йду до магазину {k.title()}, і купую там такі товари {products}")
  