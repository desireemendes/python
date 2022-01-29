lucky_numbers = [3, 9, 43, 7, 21, 17, 10]
places = ["Iceland", "Canada", "Honduras", "Germany", "Italy", "Italy"]

#extend function, take list and append another list on it
places.extend(lucky_numbers)
print(places)

#append item to the end
places.append("Spain")

#insert item at index 3
places.insert(3, "England")

#remove element from list
places.remove("Canada")

#remove everything from the list
# places.clear()

#pop last item off list
places.pop()

#get index if item exists in the list
print(places.index("Honduras"))

#see how many times element appears in list
print(places.count("Italy"))

#sort list in ascending order
places.sort()
lucky_numbers.sort()
print(lucky_numbers)