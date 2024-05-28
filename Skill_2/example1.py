with open("myfile.txt", "r", encoding="UTF-8") as f:
    file_data = f.readlines()
    for line in file_data:
        print(line)
