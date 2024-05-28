with open("myfile.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(line)
    f.close()
