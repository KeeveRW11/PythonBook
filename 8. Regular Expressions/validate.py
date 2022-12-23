#WITHOUT REGEX
# email = input("Whats your email? ").strip()

# # if "@" in email and ".":
# #     print("Valid")
# # else:
# #     print("Invalid")
# username, domain = email.split("@")

# if (username) and ("." in domain):
#     print("valid")
# else:
#     print("Invalid")    
#WITH REGEX    

import re

email = input("Whats your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")    