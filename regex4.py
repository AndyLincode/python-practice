import re
import os

result = []


def search(st):
    r = re.findall(r"\d{3}-\d{3}-\d{4}", st)
    if r:
        for number in r:
            result.append(number)


for folder, sub_folders, files in os.walk("Employee"):
    for f in files:
        with open(os.path.join(folder, f), encoding="utf8") as my_file:
            text = my_file.read()
            search(text)

print(result)
# ['741-776-5632', '874-965-7544', '969-741-6350', '808-765-3211', '754-658-9650', '740-665-7400', '740-850-9666', '785-968-8500', '888-741-6360']
