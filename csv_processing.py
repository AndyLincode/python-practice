import csv

with open('file.csv', newline='', encoding='utf-8') as f:
    csv_data = csv.reader(f)
    for row in csv_data:
        # print(row)
        # ['id', 'name', 'year of birth']
        # ['1', 'albert einstein', '1879']
        # ['2', 'isaac newton', '1643']
        # ['3', 'marie curie', '1867']
        # ['4', 'galilée', '1564']
        print(row[1].title())
        # Name
        # Albert Einstein
        # Isaac Newton
        # Marie Curie
        # Galilée
