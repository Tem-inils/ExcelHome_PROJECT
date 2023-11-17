import os

folder_path = r'D:\google table\2023 Electrics & Electronics'

items = os.listdir(folder_path)

for item in items:
    print(item)