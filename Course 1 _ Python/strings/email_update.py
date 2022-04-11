

import email
from time import process_time_ns


def update(email , new_domain , old_domain):

    if "@" + old_domain in email: 
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    else:
        return email



email1 = "moeez@tesla.com"
email2 = "jackob@tesla.com"
email3 = "tracy@infosys.com"

print("old email1: " + email1)
print("old email2: " + email2)
print("old email3: " + email3)

print("\n")
print("New emails after calling the function are as follows:")
print("\n")

print(update(email1 , "gmail.com" , "tesla.com"))
print(update(email2 , "gmail.com" , "tesla.com"))
print(update(email3 , "gmail.com" , "infosys.com"))
