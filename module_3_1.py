calls = 0

def count_calls ():
    global calls
    calls += 1

def string_info (string):
    abc = str(string)
    bca = (len(abc), abc.upper(), abc.lower())
    count_calls()
    return bca

def is_contains (string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('AppLLe'))
print(string_info('banana'))
print(string_info('orange'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))

print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)