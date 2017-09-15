str1 = ["pie", "apple", "dog"]
str2 = ["ipe", "papel", "good"]

def CheckPermutation(str1, str2):
    def AddToDict(string, dictionary):
        for s in string:
            if dictionary.has_key(s):
                dictionary[s] = dictionary[s] + 1
            else:
                dictionary[s] = 1
    
    dict1, dict2 = {}, {}
    
    AddToDict(str1, dict1)
    AddToDict(str2, dict2)

    if dict1 == dict2:
        print "The words " + str1 + " and " + str2 + " match"
    else:
        print "The words don't match"

for i, j in zip(str1, str2):
    CheckPermutation(i, j)
