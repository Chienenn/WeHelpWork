# Task 1 )
print("-----Task1-----")


def find_and_print(messages):
    olderThan17 = ""

    for name, message in messages.items():
        if (
            "18 years old" in message
            or "legal age" in message
            or "vote" in message
            or "college student" in message
        ):
            olderThan17 += name + ", "

    olderThan17 = olderThan17[:-2]
    print(olderThan17)


messages = {
    "Bob": "My name is Bob. I'm 18 years old.",
    "Mary": "Hello, glad to meet you.",
    "Copper": "I'm a college student. Nice to meet you.",
    "Leslie": "I am of legal age in Taiwan.",
    "Vivian": "I will vote for Donald Trump next week",
    "Jenny": "Good morning.",
}

find_and_print(messages)


# Task 2)
print("-----Task2-----")
# bonus rules :   The bonus is calculated as Salary * Performance * Role.
# 1.performance : a) Above average * 0.3
#                 b) AbortControllerverage * 0.2
#                 c) Below average * 0.1

# 2.role        : a) Engineer and Sales * 0.2
#                 b) CEO * 0.5


def calculate_sum_of_bonus(data):
    bonusSum = 0

    for employee in data["employees"]:
        salary = employee["salary"]

        if isinstance(salary, str):
            if "USD" in salary:
                salary = int(salary.replace("USD", "")) * 30
            else:
                salary = int(salary.replace(",", ""))

        performance = employee["performance"]
        role = employee["role"]

        bonus = 0
        if performance == "above average":
            bonus = salary * 0.3
        elif performance == "average":
            bonus = salary * 0.2
        elif performance == "below average":
            bonus = salary * 0.1

        if role == "Engineer" or role == "Sales":
            bonus *= 0.2
        elif role == "CEO":
            bonus *= 0.5

        bonusSum += bonus

    print("Sum of Bonus :", round(bonusSum), "NTD")


calculate_sum_of_bonus(
    {
        "employees": [
            {
                "name": "John",
                "salary": "1000USD",
                "performance": "above average",
                "role": "Engineer",
            },
            {"name": "Bob", "salary": 60000, "performance": "average", "role": "CEO"},
            {
                "name": "Jenny",
                "salary": "50,000",
                "performance": "below average",
                "role": "Sales",
            },
        ]
    }
)

# Task 3)
print("-----Task3-----")


def func(*data):
    middle_name_counts = {}
    unique_middle_name = ""

    for name in data:
        name_array = list(name)

        middle_name_index = len(name_array) // 2
        middle_name = name_array[middle_name_index]

        if middle_name in middle_name_counts:
            middle_name_counts[middle_name] += 1
        else:
            middle_name_counts[middle_name] = 1

    for name in data:
        name_array = list(name)

        middle_name_index = len(name_array) // 2
        middle_name = name_array[middle_name_index]

        if middle_name_counts[middle_name] == 1:
            unique_middle_name = name
            break

    if unique_middle_name != "":
        print(unique_middle_name)
    else:
        print("沒有")


func("彭大牆", "王明雅", "吳明")
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花")
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")


# Task 4)
print("-----Task4-----")


def get_number(index):
    if index <= 0:
        return 0

    number = 0

    for i in range(1, index + 1):
        if i % 2 == 1:
            number += 4
        else:
            number -= 1

    return number


print(get_number(1))  # 印出 4
print(get_number(5))  # 印出 10
print(get_number(10))  # 印出 15


# Task 5)
print("-----Task5-----")


def find_index_of_car(seats, status, x):
    answer = -1
    for i in range(len(seats)):
        if status[i] == 1 and seats[i] >= x:
            if answer == -1:
                answer = i
            elif seats[i] < seats[answer]:
                answer = i
    return answer


print(find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2))  # print 4
print(find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4))  # print -1
print(find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4))  # print 2
