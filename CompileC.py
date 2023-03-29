import subprocess


class CompileC:
    def __init__(self, filename):
        self.filename = filename

    def compile(self):
        cmd = ['gcc', self.filename, '-o', 'output']
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stderr:
            print('Error:', stderr.decode())
        else:
            print('Compilation successful')


compiler = CompileC('main.c')
compiler.compile()
