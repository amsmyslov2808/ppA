# money = 1500
# percent = 15
# years = 5

# i = 0

# while i < years:
#     money += money * percent / 100.0
#     i += 1

# print(f"получилось денег {money:.2f}")

# money = 1500
# percent = 15
# finish_money = money * 3

# years = 0

# while money < finish_money:
#     money += money * percent / 100.0
#     years += 1

# print(f"получилось денег {money:.2f}")
# print(f"прошло лет = {years}")

# money = 1500
# percent = 15
# years = 5

# for i in range(years):
#     money += money * percent / 100.0

# print(f"получилось денег {money:.2f}")

import random

for i in range(10):
    print(f"{i} - {random.randint(1,100)}")
