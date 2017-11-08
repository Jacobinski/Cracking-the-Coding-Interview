# Function to compute number of 1,2,3 step combos for n steps
def TripleStep(num):
    
    # Helper function which adds memoization
    # Improvement: O(3^n) -> O(n) 
    def TripleStep_memo(num, array):
        if num < 1:
            return 0
        
        if array[num] != None:
            return array[num]

        return TripleStep_memo(num - 1, array) + TripleStep_memo(num - 2, array) + TripleStep_memo(num - 3, array)

    # +4 to ensure that we can populate the array even when num == 0
    memo = [None] * (num + 4)
    memo[0] = 0
    memo[1] = 1
    memo[2] = 2
    memo[3] = 4

    return TripleStep_memo(num, memo)

for i in range(0,9):
    print("steps="+str(i)+" combos="+str(TripleStep(i)))
