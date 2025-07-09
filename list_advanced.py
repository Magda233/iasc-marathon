# students = ["Sarah", "Anna", "Nate", "Emily", "Sebastian"]
# grades = [38, 98, 74, 82, 49]

# max_grade_index = grades.index(max(grades))
# top_student = students[max_grade_index]

# passed_students = [students[i] for i in range(len(grades)) if grades[i] > 60]

# failed_count = sum(grade < 60 for grade in grades)

# print("Найвищий бал має:", top_student)
# print("Студенти з оцінкою > 60:", passed_students)
# print("Кількість студентів, які не склали:", failed_count)
# # Anna has the best grades among the students.


# logs = ["ok", "error", "fail", "ok", "error", "warning", "ok", "fail"]
# print(logs.count("error"))
# # Error count: 2



# 

# expenses = [
#     ["Понеділок", 120],
#     ["Вівторок", 80],
#     ["Середа", 150],
#     ["Четвер", 0],
#     ["П’ятниця", 250],
#     ["Субота", 300],
#     ["Неділя", 200]
# ]
# max_day = expenses[0]
# for item in expenses:
#   if item[1] > max_day[1]: max_day = item
# total = 0
# for item in expenses:
#  total += item[1]
#  days_over_100 = []
# for item in expenses:
#   if item[1] > 100:
#    days_over_100.append(item[0])
# print("Найбільші витрати були у:", max_day[0], "-", max_day[1], "грн")
# print("Загальні витрати за тиждень:", total, "грн")
# print("Дні з витратами понад 100 грн:", (days_over_100))
# # Найбільші витрати були у: Субота - 300 грн
# # Загальні витрати за тиждень: 1100 грн
# # Дні з витратами понад 100 грн: ['Середа', 'П’ятниця', 'Субота', 'Неділя']


# products = [
#     ["яблуко", 2, 12.5],
#     ["банан", 5, 8.0],
#     ["молоко", 1, 34.0],
#     ["хліб", 2, 16.0]
# ]
# product_sum = 0
# for product in products:
#     sum = product[1] * product[2]
#     product_sum += sum
# print(product_sum)


# max_price = 0
# for product in products:
#     max_price = max(product[2], max_price)
# for product in products:
#     if product[2] == max_price:
#         print("Найдорожчий товар:", product[0])


# for product in products:
#     print("товар - ", product[0],  product[1] * product[2], "грн")

# where n is an even number
x = range(1,31)
even_list = []
for n in x:
  if n % 2 == 0:
    even_list.append(n*n)
print(even_list)

# not divided by 4
new_list = []
x = range(1,31)
for n in x:
  if n % 4 != 0:
    new_list.append(n*n)
print(new_list)

# not in list [10, 14, 18]
x = range(1,31)
not_in_list = [10, 14, 18]
new_2_list = []
for n in x:
    if n not in not_in_list:
        new_2_list.append(n*n)
print(new_2_list)
