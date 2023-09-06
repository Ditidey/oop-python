
from optparse import Values


d = {'!' : 1, '@' : 2, '#' : 3, '$' : 4, '%' : 5, '^': 6}

c_list = []
def create_list(d):
    for k, v in d.items():
        c_list.extend([k, v])
    return c_list

new_list = create_list(d)
print(new_list)