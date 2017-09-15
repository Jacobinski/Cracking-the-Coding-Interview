test_str = ["Hello World!", "My name is Jacob", "Test"]
test_len = [14, 22, 4]

def URLify(string, length):
    # Create the static array string
    new_string = [' '] * length
    for k, s in enumerate(string):
        new_string[k] = s

    found_first_char = False

    writer = length - 1
    reader = length - 1

    while not found_first_char:
        if new_string[reader] == ' ':
            reader -= 1
        else:
            found_first_char = 'True'

    while reader >= 0:
        char = new_string[reader]
        if char == ' ':
            new_string[writer-2:writer+1] = '%20'
            writer -= 3
            reader -= 1
        else:
            new_string[writer] = new_string[reader]
            writer -= 1
            reader -= 1

    print(''.join(new_string))

for string, length in zip(test_str, test_len):
    URLify(string, length)
