# def describe_age(age): 
#     if age <= 12: return "You're a(n) kid"
#     elif age >= 13 and age <= 17: return "You're a(n) teenager"
#     elif age >= 18 and age <= 64: return "You're a(n) adult"
#     else: return "You're a(n) elderly"  


# def describe_age(a):
#     return "You're a(n) {'kid' if a<=12 else 'teenager' if 13<=a<=17 else 'adult' if 18 <=a<=64 else 'elderly'}"

describe_age=lambda a:f"You're a(n) {'kid' if a<13 else 'teenager' if a<18 else 'adult' if a<65 else 'elderly'}"