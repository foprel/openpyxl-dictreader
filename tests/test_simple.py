import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import dictreader

reader = dictreader.DictReader("test_simple.xlsx", worksheet="Sheet1")

for row in reader:
    name = row["Name"]
    age = row["Age"]
    country = row["Country"]
    print(f"Name: {name}, Age: {age}, Country: {country}")