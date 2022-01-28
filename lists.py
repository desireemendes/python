places = ["Iceland", "Canada", "Honduras", "Germany", "Italy"]

#access last element
print(places[-1])

#access 2nd last element
print(places[-2])

#access element at index 1 and all elements after it
print(places[1:])

#specify range of elements 1-3, elements up to but not including 3
print(places[1:3])

#update value
places[1] = "Mexico"
print(places[1])