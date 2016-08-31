import csv

table = """
Name | Age | Score
Alex | 3   | 8.0
Jame | 5   | 9.5
"""

table_reader = csv.DictReader(table.splitlines()[1:], delimiter='|')
for element in table_reader:
    print(element)
