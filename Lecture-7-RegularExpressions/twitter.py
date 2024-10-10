import re

url = input("URL: ").strip()

#Explaination at 1:59hrs at CS50P - Regular Expressions Lecture
matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(1))