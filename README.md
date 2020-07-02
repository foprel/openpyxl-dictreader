# openpyxl-dictreader

## Description
A module that maps the information in each row in an [openpyxl](https://github.com/chronossc/openpyxl) worksheet to a dict whose keys are given by the optional fieldnames parameter, similar to Python's native [csv.DictReader](https://docs.python.org/3/library/csv.html#csv.DictReader).

## Installing
```python
pip install openpyxl-dictreader
```

## Examples
Input:
```python
import openpyxl_dictreader

reader = openpyxl_dictreader.DictReader("names.xlsx", "Sheet1")
for row in reader:
    print(row["First Name"], row["Last Name"])
```

Output:
```
Boris Johnson
Donald Trump
Mark Rutte
```

## load_workbook keyword arguments
The openpyxl load_workbook method takes several optional keyword arguments. These can be passed into the openpyxl_dictreader.DictReader constructor as keyword arguments:

```python
reader = openpyxl_dictreader.DictReader("names.xlsx", "Sheet1", read_only=False, keep_vba=False, data_only=False, keep_links=True)
```

## Acknowledgements
* [openpyxl](https://github.com/chronossc/openpyxl)
* [csv](https://docs.python.org/3/library/csv.html#csv.DictReader)

