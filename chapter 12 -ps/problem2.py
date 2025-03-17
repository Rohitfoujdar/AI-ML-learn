list = [2, 5, 8, 9, 0, 7, 8, 7, 6]

for index, item in enumerate(list):
    if (index == 2 or index == 4 or index == 6):
        print(f"The item is {item}")