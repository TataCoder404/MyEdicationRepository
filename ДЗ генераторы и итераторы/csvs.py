import csv


class CSVreader:
    def __init__(self, file_name, n):
        self.file_name = file_name
        self.n = n
        self.cur = 0
        self.reader = None
        self.file = None

    def __iter__(self):
        self.file = open(self.file_name, "r")
        self.reader = csv.DictReader(self.file)
        return self

    def __next__(self):
        try:
            self.cur += 1
            if self.cur > self.n:
                raise StopIteration
            row = next(self.reader)
            return row
        except StopIteration:
            self.reader = None
            self.file.close()
            raise StopIteration


reader = CSVreader("pizza_v1.csv", 7)
for i in reader:
    print(i)

print(reader.file.closed)
