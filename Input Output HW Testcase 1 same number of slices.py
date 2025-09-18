#Input_Output_HW_Pizza_Order.py
print(" A family of 4 wants to order pizza. Each pizza has 8 slices.")
print('Enter how many slices of pizza each person will eat.')
s1 = int(input("Person 1 slices:  "))
s2 = int(input("Peson 2 slices: "))
s3 = int(input("Person 3 slices: "))
s4 = int(input("Person 4 slices: "))

#Each user input is added together to form the total slices.
#Divide the total number of slices by 8 to get the number of pizzas needed.
total_slices = s1 + s2 + s3 + s4
pizzas_needed = total_slices // 8

if total_slices % 8 !=0:
      pizzas_needed = pizzas_needed + 1

leftover = pizzas_needed * 8 - total_slices
#prints the total number of slices, how many whole pizzas are needed and the leftovers.
print(f"Total number of slices:{total_slices}")
print(f"Total number of whole pizzas: {pizzas_needed}")
print(f"Number of slices leftover after everyone eats: {leftover}")
      
