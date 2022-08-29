email = input("Enter the email address: ").strip()

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

result = (f"Username: '{username}'Domain: '{domain}'")
print(result)