def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(5, 'Sea')
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [7, 'Python', False]
values_dict = {'a': 'number', 'b': 5, 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 2)