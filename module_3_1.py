calls = 0
def count_calls ():
    global calls
    calls += 1
    return calls


def string_info (string):
    count_calls ()
    string = (len(string), string.upper(), string.lower())
    return string



def is_contains(string, list_to_search):
    count_calls()
    string_up = string.upper()
    list_to_search = list(map(str.upper, list_to_search))
    for i in range (len(list_to_search)):
        if string_up not in list_to_search:
            return False
    return True



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)


