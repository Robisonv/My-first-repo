# This going to be my fist project
print("Password Generator")

from random import sample
def password_generator(long):
    lower_letters = "abcdefghijklmnopqrstwxz"
    upper_letters = lower_letters.upper()
    nums = "0123456789"
    characters = "@.*#^&"
    secuence = lower_letters + upper_letters + nums + characters
    password_combination = sample(secuence, long)
    password_save = "".join(password_combination)
    return password_save
password = password_generator(8)
print("password: ", password)