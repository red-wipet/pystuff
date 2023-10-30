height = 5 # Высота ёлочки
i = 0
while i < height:
   spaces = ' ' * (height - i - 1)
   stars = '*' * (2 * i + 1)
   print(spaces + stars)
   i += 1
