# contacts = {
#     "Anna": "093-123-45-67",
#     "Ivan": "050-888-99-00",
#     "Olha": "097-777-33-22"
# }
# contacts["Taras"] = "063-000-11-22"
# print(contacts)
# del contacts["Ivan"]
# print(contacts)
# print("contacts:")
# for name in contacts.keys():
#     print(name)
# print("contacts:")
# for number in contacts.values():
#     print(number)
# print("Do we have Katya's number?")
# if "Katya" in contacts:
#     print("Yes we have her number")
# if not "Katya" in contacts:
#     print("No we don't have her number")


# grades = {
#     "math": 88,
#     "physics": 75,
#     "english": 93,
#     "history": 59
# }
# def best_grade(grades):
#     highest_grade_value = max(grades.values())
#     for subject, grade in grades.items():
#         if grade == highest_grade_value:
#             highest_grade_subject = subject
#             break
#     print(f"Highest_grade_subject: {highest_grade_subject}")


# best_grade(grades)


# grades = {
#     "math": 88,
#     "physics": 75,
#     "english": 93,
#     "history": 59
# }
# total = sum(grades.values())
# average = total / len(grades)
# print(f"Average grade: {average}")


# grades = {
#     "math": 88,
#     "physics": 75,
#     "english": 93,
#     "history": 59
# }
# massive = []
# for subject, grade in grades.items():
#  if grade > 80:
#     massive.append(subject)

# print(massive)


# transactions = [
#     ("Anna", 200),
#     ("Ivan", -50),
#     ("Anna", 100),
#     ("Olha", 500),
#     ("Ivan", 150),
#     ("Olha", -100),
# ]
# array = {}
# for name, amount in transactions:
#     array[name] = array.get(name, 0) + amount

# balances = dict(array)



transactions = [
    ("Anna", 200),
    ("Ivan", -50),
    ("Anna", 100),
    ("Olha", 500),
    ("Ivan", 150),
    ("Olha", -100),
]
# array = {}
# for name, amount in transactions:
#     array[name] = array.get(name, 0) + amount

# balances = array

# def best_grade(grades):
#     highest_grade_value = max(grades.values())
#     for subject, grade in grades.items():
#         if grade == highest_grade_value:
#             highest_grade_subject = subject
#             break
#     print(f"Highest_grade_subject: {highest_grade_subject}")


# best_grade(balances)


# transactions = [
#     ("Anna", 200),
#     ("Ivan", -50),
#     ("Anna", 100),
#     ("Olha", 500),
#     ("Ivan", 150),
#     ("Olha", -100),
# ]

# balances = []
# for name, amount in transactions:
#     if amount < 0:
#         balances.append(name)
    

# print(balances)



# text = "hello world hello again hello world test world"
# text.count("hello")
# print(text.count("hello"))
# text.count("world")
# print(text.count("world"))
# text.count("again")
# print(text.count("again"))
# text.count("test")
# print(text.count("test"))

# text = "hello world hello again hello world test world"


# array = {}
# for word in text.split():
#     array[word] = text.count(word)

# print(array)

student = {
    "name": "Anna",
    "age": 20,
    "courses": ["math", "physics", "english"]
}

import json

y = json.dumps(student)

print(y)

# ------------------------------

wy = json.loads(y)

print(wy)


wy["courses"].append("history")

print(wy)

