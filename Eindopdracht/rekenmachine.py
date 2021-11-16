while True:

  num_1 = int(input("Voer het eerste getal in: "))
  operator = input("Voeg een operator toe: ")
  num_2 = int(input("Voer het tweede getal in: "))

  if operator == "+":
    print("Het antwoord is: " + str(num_1 + num_2))
  elif operator == "-":
    print("Het antwoord is: " + str(num_1 - num_2))
  elif operator == "*":
    print("Het antwoord is: " + str(num_1 * num_2))
  elif operator == "/":
    print("Het antwoord is: " + str(num_1 / num_2))
  else:
    print("Error.")