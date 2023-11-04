import random

def generate_random_number():
   min_value = int(input("Enter number: "))
   max_value = int(input("Enter bigger number: "))

   random_number = random.randint(min_value, max_value)
   return random_number

result = generate_random_number()
print ("Random number is: ", result)
