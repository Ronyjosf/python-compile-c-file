import os
import fileinput
import subprocess
import unittest


class FileCompiler:
    def __init__(self, filename):
        self.filename = filename

    @staticmethod
    def check_if_empty_none(val):
        if val is None or val == "":
            raise Exception("Sorry, value can't be none or empty")

    def replace(self, old_value, new_value):
        # given old value is correct, we check for new value only.
        # self.check_if_empty_none(old_value)
        self.check_if_empty_none(new_value)

        with fileinput.FileInput(self.filename, inplace=True) as file:
            for line in file:
                print(line.replace(old_value, new_value), end='')

    def compile(self):
        cmd = ['gcc', self.filename, '-o', 'output']
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stderr:
            print('Error:', stderr.decode())
        else:
            print('Compilation successful')

# [rony] normally tests go on a different file
class TestFileCompiler(unittest.TestCase):
    def setUp(self):
        self.filename = 'main.c'
        self.file = FileCompiler(self.filename)

    def test_replace_helper(self, old_value, new_value):
        self.file.replace(old_value, new_value)
        with open(self.filename) as f:
            content = f.read()
            self.assertIn(new_value, content)

    def test_replace(self):
        old_value = '100'
        new_value = '200'
        self.test_replace_helper(old_value, new_value)

    def test_replace_none(self):
        old_value = '100'
        new_value = ''
        self.test_replace_helper(old_value, new_value)

    def test_compile(self):
        self.file.compile()
        self.assertTrue(os.path.exists('output'))

    # comment out, since tearDown is only for testing
    # def tearDown(self):
    #     # os.remove('test_main.c')
    #     os.remove('output')


if __name__ == '__main__':
    unittest.main()


def main():
    filename = 'main.c'
    old_value = '100'
    new_value = '200'
    file = FileCompiler(filename)

    file.replace(old_value, new_value)

    file.compile()

    # Run the output executable
    os.system('./output')


if __name__ == '__main__':
    main()
