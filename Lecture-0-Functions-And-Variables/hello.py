# my first Program

 # Asing users for their name.
name = input("What's your name? ")

# Remove whitespace from str and Capitalize user's name
name = name.strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Saying hello to user
print(f"hello, {first}")