monthConversions = {
  "Jan": "January",
  "Feb": "February",
  "Mar": "March",
  "Apr": "April",
  "Ma": "May",
  "Jun": "June",
  "Jul": "July",
  "Aug": "August",
  "Sep": "September",
  "Oct": "October",
  "Nov": "November",
  "Dec": "December"
}

print(monthConversions["Aug"])
print(monthConversions.get("Nov"))
print(monthConversions.get("Month", "not a valid key"))
