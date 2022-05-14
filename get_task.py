import numpy as np


def skip_comments(file):
    line = file.readline()
    while line:
        if len(line) == 0 or line[0] == '#':
            line = file.readline()
        else:
            return line


def get_task(file_name):
    with open(file_name, 'r') as file:
        a_text = skip_comments(file)
        if not a_text:
            raise Exception("No resources")
        a = np.array([float(a_i) for a_i in a_text.strip().split(' ')])

        b_text = skip_comments(file)
        if not b_text:
            raise Exception("No needs")
        b = np.array([float(b_i) for b_i in b_text.strip().split(' ')])

        c_matr = []
        for i in range(0, len(a)):
            c_text = skip_comments(file)
            if not c_text:
                raise Exception("No cost line #" + str(i))
            c_matr.append([float(c_i) for c_i in c_text.strip().split(' ')])
        return a, b, np.matrix(c_matr)
