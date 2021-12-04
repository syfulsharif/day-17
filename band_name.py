# 1. Create a greeting for your program
print("Hello! Welcome to the Band Name Generator Program!\n")
# 2. Ask the user for the city that they grew up in
city = input("Enter the city name you grew up in: \n")
# 3. Ask the user for the name of a pet.
pet = input("Enter the name of your pet you used to have when you were a kid: \n")
# 4. Combine th name of their city and pet and show them their band name.
band_name = city.capitalize() + pet.capitalize()
# 5. Make sure the input cursor shows on a new line
print(band_name)
