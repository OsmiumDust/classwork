while True:
  try:

    size1 = int(input("How many 1 liter or less bottles do you have: "))
    size2 = int(input("How many more than 1 liter bottles do you have: "))

    value = (size1 * 0.1) + (size2 * 0.25)

    value =  ("%.2f" % value)

    print(f"Your bottle totals comes up to ${value}. \nThank you for recycling.")
    break

  except:
    print("We don't accept part bottles or words")
