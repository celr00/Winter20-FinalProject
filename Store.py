# Built By:
# Carlos Lozada 556589
# Karen Garza 611107

# Date: 12/07/2020

# Funtion to delete a dish
def eraseDish(ordersArray, priceArray, QuantitiesArray, price):
  erase = int(input("¿Qué elemento desea erase? "))
  price -= priceArray[erase - 1]
  ordersArray.remove(ordersArray[erase - 1])
  priceArray.remove(priceArray[erase - 1])
  QuantitiesArray.remove(QuantitiesArray[erase - 1])
  return price

# Function that modifies the order's quantities
def addQuantity(ordersArray, priceArray, QuantitiesArray, price):
  modify = int(input("¿Qué elemento desea modify? "))
  price -= priceArray[modify - 1]
  precioReal = priceArray[modify - 1] // QuantitiesArray[modify - 1]
  quantity = int(input("How many do you want?"))
  priceArray[modify - 1] = precioReal * quantity
  QuantitiesArray[modify - 1] = quantity
  price += priceArray[modify - 1]
  return price

# Funtion that shows the ingredients to build your own dish
def showIngredients(dish):
  print("*** INGREDIENTS ***")
  print("1) Cheese $5")
  print("2) Jelly $10")
  print("3) Caramel $20")
  print("4) Chicken $30")
  print("5) Beef $15")
  print(dish)
  num = int(input("How many ingredients do you want to add? If you don't want any ingredient type the number 6"))
  return num

# Funcion that builds a persola dish
def basicDish(order, IngredientsPrice, num):
  for i in range(num):
    if i == (num - 1) and i != 0:
      order += " and "
    ingredient = int(input("Please select the ingredient"))
    if ingredient == 1:
      order += "cheese"
      IngredientsPrice += 5
    elif ingredient == 2:
      order += "jelly"
      IngredientsPrice += 10
    elif ingredient == 3:
      order += "caramel"
      IngredientsPrice += 20
    elif ingredient == 4:
      order += "chicken"
      IngredientsPrice += 30
    elif ingredient == 5:
      order += "beef"
      IngredientsPrice += 15
    if i != (num - 1) and i != (num - 2):
      order += ", "
  cantidad = int(input("How many do you want?"))
  totalPrice = cantidad * IngredientsPrice
  return cantidad, order, totalPrice

# Function that deploys the customer's order
def deployWholeOrder(orderArray, priceArray, quantityArray, price):
  for i in range(len(orderArray)):
    print("{})".format(i+1), end= " ")
    print(quantityArray[i], end=" ")
    print(orderArray[i], end=" ")
    print("${}". format(priceArray[i]))
  print("Total: ${}".format(price))

# Function that deploys that day's results
def deployDayResults(totalOrderArray, totalPriceArray, quantityArray, names):
  print("-*-*-*- DAY'S RESULTS -*-*-*-")
  acum = 0
  for i in range(len(totalOrderArray)):
    print("Customer:", names[i])
    acumCustomer = 0
    for j in range(len(totalOrderArray[i])):
      print(quantityArray[i][j], end=" ")
      print(totalOrderArray[i][j], end=" ")
      print("${}".format(totalPriceArray[i][j]))
      acum += totalPriceArray[i][j]
      acumCustomer += totalPriceArray[i][j]
    print("Total of {}: ${}".format(names[i], acumCustomer))
    print("********************")
  print("Total gained today: ${}".format(acum))

# Declaration of Arrays
totalOrders = []
totalPrices = []
totalQuantities = []
names = []

# Beginning of the day
print("Please type 'END' to end the day")
name = input("Type your name: ")
while name != "END":
  # Welcome Message
  txt = "Welcome, {}!"
  print(txt.format(name))
  opc = "N"
  customerOrder = []
  quantity = []
  prices = []
  price = 0
  while opc == "N":
    # Dish Categories
    print("*** MENU ***")
    print("1) Crepe")
    print("2) Donut")
    print("3) Sandwich")
    print("4) Coffee")
    food = int(input("What do you want to order? "))
    
    # Crepes
    if food == 1:
      print("*** CREPAS ***")
      print("1) Purple Rain $110")
      print("2) Red Mango $130")
      print("3) Oreo Obsession $120")
      print("4) Choose Ingredients")
      dish = int(input("What dish would you like? "))
      if dish == 1:
        customerOrder.append("Purple Rain")
        amount = int(input("How many do you want? "))
        quantity.append(amount)
        dishPrice = amount * 110
        prices.append(dishPrice)
        price += dishPrice
      elif dish == 2:
        customerOrder.append("Red Mango")
        amount = int(input("How many do you want? "))
        quantity.append(amount)
        dishPrice = amount * 130
        prices.append(dishPrice)
        price += dishPrice
      elif dish == 3:
        customerOrder.append("Oreo Obsession")
        amount = int(input("How many do you want? "))
        quantity.append(amount)
        dishPrice = amount * 120
        prices.append(dishPrice)
        price += dishPrice
      elif dish == 4:
        elementoSolo = "6) Basic crepe $50"
        num = showIngredients(elementoSolo)
        precioIngs = 50
        if num == 6:
          customerOrder.append("Basic crepe")
          amount = int(input("How many do you want? "))
          quantity.append(amount)
          dishPrice = amount * 50
          prices.append(dishPrice)
        else:
          orden = "Crepe with "
          amount, orden, dishPrice = basicDish(orden, precioIngs, num)
          quantity.append(amount)
          customerOrder.append(orden)
          prices.append(dishPrice)
        price += dishPrice

    # Donuts
    elif food == 2:
      print("*** DONUTS ***")
      print("1) Banana Chocolate $100")
      print("2) Berries Deluxe $150")
      print("3) Choose Ingredients")
      dish = int(input("What dish would you like? "))
      if dish == 1:
        customerOrder.append("Banana Chocolate")
        amount = int(input("How many do you want? "))
        quantity.append(amount)
        dishPrice = amount * 100
        prices.append(dishPrice)
        price += dishPrice
      elif dish == 2:
        customerOrder.append("Berries Deluxe")
        amount = int(input("How many do you want? "))
        quantity.append(amount)
        dishPrice = amount * 150
        prices.append(dishPrice)
        price += dishPrice
      elif dish == 3:
        elementoSolo = "6) Basic Donut $50"
        num = showIngredients(elementoSolo)
        precioIngs = 50
        if num == 6:
          customerOrder.append("Basic Donut")
          amount = int(input("How many do you want? "))
          quantity.append(amount)
          dishPrice = amount * 50
          prices.append(dishPrice)
        else:
          orden = "Donut with "
          amount, orden, dishPrice = basicDish(orden, precioIngs, num)
          quantity.append(amount)
          customerOrder.append(orden)
          prices.append(dishPrice)
        price += dishPrice

    # Sandwich
    elif food == 3:
      print("*** SANDWICH ***")
      print("1) Chicken Sandwich $60")
      print("2) Grilled Cheese Sandwich $50")
      print("3) Club Sandwich $70")
      print("4) Choose Ingredients")
      dish = int(input("What dish would you like? "))
      if dish == 1:
        customerOrder.append("Chicken Sandwich")
        amount = int(input("How many do you want? "))
        quantity.append(amount)
        dishPrice = amount * 60
        prices.append(dishPrice)
        price += dishPrice
      elif dish == 2:
        customerOrder.append("Grilled Cheese Sandwich")
        amount = int(input("How many do you want? "))
        quantity.append(amount)
        dishPrice = amount * 50
        prices.append(dishPrice)
        price += dishPrice
      elif dish == 3:
        customerOrder.append("Club Sandwich")
        amount = int(input("How many do you want? "))
        quantity.append(amount)
        dishPrice = amount * 70
        prices.append(dishPrice)
        price += dishPrice
      elif dish == 4:
        elementoSolo = "6) Sandwich with ham $20"
        num = showIngredients(elementoSolo)
        precioIngs = 20
        if num == 6:
          customerOrder.append("Sandwich with ham")
          amount = int(input("How many do you want? "))
          quantity.append(amount)
          dishPrice = amount * 20
          prices.append(dishPrice)
        else:
          orden = "Sandwich with "
          amount, orden, dishPrice = basicDish(orden, precioIngs, num)
          quantity.append(amount)
          customerOrder.append(orden)
          prices.append(dishPrice)
        price += dishPrice

    # Coffee
    elif food == 4:
      print("*** COFFEE ***")
      print("1) Caramel Macchiato $75")
      print("2) Matcha Latte $70")
      print("3) Choose Ingredients")
      dish = int(input("What dish would you like? "))
      if dish == 1:
        customerOrder.append("Caramel Macciato")
        amount = int(input("How many do you want? "))
        quantity.append(amount)
        dishPrice = amount * 75
        prices.append(dishPrice)
        price += dishPrice
      elif dish == 2:
        customerOrder.append("Matcha Latte")
        amount = int(input("How many do you want? "))
        quantity.append(amount)
        dishPrice = amount * 70
        prices.append(dishPrice)
        price += dishPrice
      elif dish == 3:
        elementoSolo = "6) Basic Coffee $40"
        num = showIngredients(elementoSolo)
        precioIngs = 40
        if num == 6:
          customerOrder.append("Basic Coffee")
          amount = int(input("How many do you want? "))
          quantity.append(amount)
          dishPrice = amount * 40
          prices.append(dishPrice)
        else:
          orden = "Coffee with "
          amount, orden, dishPrice = basicDish(orden, precioIngs, num)
          quantity.append(amount)
          customerOrder.append(orden)
          prices.append(dishPrice)
        price += dishPrice

    # Order's Draft
    print("Until now yor order is...")
    deployWholeOrder(customerOrder, prices, quantity, price)
    opcMenu = "Y"

    # Options
    while opcMenu == "Y":
      print("What would you like to do with your order?")
      print("1) Confirm and pay")
      print("2) Erase a dish")
      print("3) Modify quantity")
      print("4) Add dish")
      menu = int(input("Choice: "))
      # Confirm
      if menu == 1:
        opcMenu = "N"
        opc = "Y"
      # Delete Dish
      if menu == 2:
        price = eraseDish(customerOrder, prices, quantity, price)
        deployWholeOrder(customerOrder, prices, quantity, price)
        opcMenu = input("Do you want to do something else? (Y/N) ")
        if opcMenu == "N":
          opc = "Y"
      # Modify quantities
      if menu == 3:
        price = addQuantity(customerOrder, prices, quantity, price)
        deployWholeOrder(customerOrder, prices, quantity, price)
        opcMenu = input("Do you want to do something else? (Y/N) ")
        if opcMenu == "N":
          opc = "Y"
      # Add more dishes
      if menu == 4:
        opcMenu = "N"
        opc = "N"

  # Final Order
  print(name,"'s order: ")
  deployWholeOrder(customerOrder, prices, quantity, price)
  print("Have a nice day!")
  totalOrders.append(customerOrder)
  totalPrices.append(prices)
  totalQuantities.append(quantity)
  names.append(name)
  print("*************")
  print("Please type 'END' to end the day")
  name = input("Type your name: ")

# End of the day
deployDayResults(totalOrders, totalPrices, totalQuantities, names)
