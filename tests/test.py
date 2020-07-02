import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import openpyxl_dictreader

reader = openpyxl_dictreader.DictReader("names.xlsx", "Sheet1")
for row in reader:
    print(row["First Name"], row["Last Name"])