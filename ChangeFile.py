import fileinput


class ChangeFile:
    def __init__(self, filename, old_value, new_value):
        self.filename = filename
        self.old_value = old_value
        self.new_value = new_value

    def replace(self):
        with fileinput.FileInput(self.filename, inplace=True) as file:
            for line in file:
                print(line.replace(self.old_value, self.new_value), end='')


replacer = ChangeFile('main.c', '__VALUE__', 'just-a-test')
replacer.replace()
