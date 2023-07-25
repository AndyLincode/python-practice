import re

text = "hello, heabo, hecdo, he56o, helloooooo"

print(re.findall(r"he[abcl][a-d]o", text))  # ['heabo', 'hecdo']

print(re.findall(r"he..o", text))
# ['hello', 'heabo', 'hecdo', 'he56o', 'hello']

# ?????@???.??
regex = r"\b[A-Za-z0-9._-]+@+[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"


def check_email(email):
    if re.fullmatch(regex, email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not valid.")


email1 = "andy@mail.com"
email2 = "lin1_11-1@mail.com"
email3 = "XD.com"

check_email(email1)  # andy@mail.com is a valid email address.
check_email(email2)  # lin1_11-1@mail.com is a valid email address.
check_email(email3)  # XD.com is not valid.
