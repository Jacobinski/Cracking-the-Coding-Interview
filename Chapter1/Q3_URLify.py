test_str = ["Hello World!", "My name is Jacob", "Test"]
test_len = [14, 22, 4]

def URLify(string, length):
    new_string = [None] * length
    string = [s for s in string]
    i = length - 1
    j = len(string) - 1
    while i >= 0:
        char = string[j]
        if char == ' ':
            new_string[i] = '0'
            new_string[i-1] = '2'
            new_string[i-2] = '%'
            i = i - 3
            j = j - 1
        else:
            new_string[i] = string[j]
            i = i - 1
            j = j - 1

    print(''.join(new_string))

for string, length in zip(test_str, test_len):
    URLify(string, length)
