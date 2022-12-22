email = input("Whats your email? ").strip()

# if "@" in email and ".":
#     print("Valid")
# else:
#     print("Invalid")
username, domain = email.split("@")

if (username) and ("." in domain):
    print("valid")
else:
    print("Invalid")    