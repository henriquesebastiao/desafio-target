def reverse_str(string: str):
    inverted = ''
    for i in range(len(string) - 1, -1, -1):
        inverted += string[i]
    return inverted


string = 'Test'
print('String original:', string)
print('String invertida:', reverse_str(string))
