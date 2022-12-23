import re

url = input("URL: ").strip()

# print(url)

# username = url.replace("https://www.twitter.com/", "")
# username = url.removeprefix("https://www.twitter.com/", "")

#Substitute
# username = re.sub(r"^(https?://)?(www\.|)?twitter.com/", "", url)

# print(f"Username: {username}")

#Search

# matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)

# if matches:
#     print(f"Username:", matches.group(2))

# with walrus

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

# https://www.twitter.com/kizoshasta