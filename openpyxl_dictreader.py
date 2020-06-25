from openpyxl import load_workbook


def reader(iterator):
    total = [[col.value for col in row] for row in iterator]
    for row in total:
        yield row


class DictReader:

    def __init__(self, filename, fieldnames=None, worksheet=None, restval=None, restkey=None, *args, **kwargs):
        self.wb = load_workbook(filename)
        self.ws = self.wb[worksheet]
        self.reader = reader(self.ws)
        self._fieldnames = fieldnames
        self.restkey = restkey
        self.restval = restval
        self.line_num = 0

    @property
    def fieldnames(self):
        if self._fieldnames is None:
            try:
                self._fieldnames = next(self.reader)
            except StopIteration:
                pass
        self.line_num += 1
        return self._fieldnames

    @fieldnames.setter
    def fieldnames(self, value):
        self._fieldnames = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.line_num == 0:
            self.fieldnames
        row = next(self.reader)
        self.line_num += 1

        while row == []:
            row = next(iter(self.ws_list))
        d = dict(zip(self.fieldnames, row))
        lf = len(self.fieldnames)
        lr = len(row)
        if lf < lr:
            d[self.restkey] = row[lf:]
        elif lf > lr:
            for key in self.fieldnames[lr:]:
                d[key] = self.restval
        return d
