from io import StringIO
from sys import stdout


class Tee:
    def __init__(self, output=stdout):
        self.buf = StringIO()
        self.output = output

    def appendln(self, param):
        if self.output is not None:
            print(param, file=self.output)
        self.buf.write(param + "\n")

    def __str__(self):
        return self.buf.getvalue()
