from multiprocessing.sharedctypes import Value


try:
  number = int(input("Enter a number: "))
  print(number)
except:
  print("Invalid input")

  #can put error type with except, like except ValueError:
  #should define specific error and not just "except"
  # try:
  #   answer = 10/0
  # except ZeroDivisionError as err:
  #   print(err)