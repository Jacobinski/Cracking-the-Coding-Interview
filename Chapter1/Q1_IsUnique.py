test = ["waffles", "brocoli", "tomato", "jacob", "Paint", "Drawer", "Palindrome", "Sassy"]

def unique_characters(string):
    for i, char in enumerate(string):
        substring = string[i+1:]
        if char in substring:
            print string + " has a repeating character"
            return
    print string + " has only unique characters"

for t in test:
    unique_characters(t)
