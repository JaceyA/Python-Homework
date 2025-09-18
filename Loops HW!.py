#Loops HW #2


#Starting inventory
muffins = 10
cupcakes = 10

while True:
    order = input("Would you like to buy a cupcake or muffin? (muffin/cupcake or 0 to quit): ").lower ()

    if order == "0":
        break

    elif order == "muffin":
        if muffins > 0:
            muffins -= 1
            print ("Muffin sold!")

        else:
            print ("Sorry, we are out of stock!")

    elif order == "cupcake":
        if cupcakes >0:
            cupcakes -= 1
            print ("Cupcake sold!")
        else:
            print("Sorry, we are out of stock!")

    else:
        print("Invaliad choice, please choose muffin, cupcake, or 0 to quit.")

#Final Inventory
    print(f"There are {muffins} muffins left over and {cupcakes} cupcakes left.")
              


                  
