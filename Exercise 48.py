while True:

  try:  
  
    user_year = int(input("Please input a year: "))

    conv = user_year % 12

    if conv == 0:
      print("Monkey")
    elif conv == 1:
      print("Rooster")
    elif conv == 2:
      print("Dog")
    elif conv == 3:
      print("Pig")
    elif conv == 4:
      print("Rat")
    elif conv == 5:
      print("Ox")
    elif conv == 6:
      print("Tiger")
    elif conv == 7:
      print("Hare")
    elif conv == 8:
      print("Dragon")
    elif conv == 9:
      print("Snake")
    elif conv == 10:
      print("Horse")
    elif conv == 11:
      print("Sheep")

  except:
    print("How did you even get this message, did you type a word?")
