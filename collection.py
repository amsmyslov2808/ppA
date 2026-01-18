count_mans = int(input("введите кол-во человек: "))  # 3
height_list = []

for i in range(count_mans):  # 0 1 2
    current_height = int(input(f"введите рост {i+1}-го человека: "))
    height_list.append(current_height)

print(height_list)
print(f"минимальнй рост = {min(height_list)}")
print(f"максммальнй рост = {max(height_list)}")
