
rubles = int(input("RUB:\> "))
currency = input("Select: USD, EUR or CNY: ")

if currency == "USD":
   rate = 72.50
   result = rubles / rate
   print(rubles, "RUB =", result, "USD")
elif currency == "EUR":
   rate = 86.20 
   result = rubles / rate
   print(rubles, "RUB =", result, "EUR")
elif currency == "CNY":
   rate = 11.20 
   result = rubles / rate
   print(rubles, "RUB =", result, "CNY")
else:
   print("ERROR")
