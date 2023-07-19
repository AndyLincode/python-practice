from sys import argv
# 取得command line的args

if len(argv) < 2:
    print("Please provide file name.")
else:
    file = open(argv[1])
    lines = file.read()

    lines = lines.split("\n") # a list of strings ["roses are red","sky is blue","syntax error in line 32"," "]
    word_count = 0
    letter_count = 0

    for line in lines:
        words = line.split(" ")
        word_count += len(words)
        letter_count += len(line)

    lines_count = len(lines) - 1
    print(f"The line count is {lines_count}.")
    print(f"The word count is {word_count}.")
    print(f"The letter count is {letter_count}.")
