monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
     "May": "May",
     6: "June"
}

print(monthConversion["Mar"])
print(monthConversion.get( 6 , "Not a valid key"))
