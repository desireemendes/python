mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

#grab key and value in dictionary
for key, value in mydict.items():
  print(key, value)

#while loops
i = 1
while i <= 10:
  print(i)
  i += 1

#for loops
for letter in "Giraffe Academy":
  print(letter)

friends = ["Jim", "Kerry", "Kevin"]
for friend in friends:
  print(friend)

#get length of array
print(len(friends))

#prints 0-9
for index in range(10):
  print(index)

#prints 3-9
for index in range(3, 10):
  print(index)


for index in range(5):
  if index == 0:
    print("1st iteration")
  else:
    print("not 1st")

def raise_to_power(base_num, pow_num):
  result = 1
  #loop through "pow_num" of times
  for index in range(pow_num):
    result = result * base_num
  return result

print(raise_to_power(3, 4))