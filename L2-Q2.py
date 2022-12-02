# Hey, I Already Did That!
# ========================

# Commander Lambda uses an automated algorithm to assign minions randomly to tasks, in order to keep minions on their toes. But you've noticed a flaw in the algorithm -- 
# it eventually loops back on itself, so that instead of assigning new minions as it iterates, it gets stuck in a cycle of values so that the same minions end up doing the 
# same tasks over and over again. You think proving this to Commander Lambda will help you make a case for your next promotion. 

# You have worked out that the algorithm has the following process: 

# 1) Start with a random minion ID n, which is a nonnegative integer of length k in base b
# 2) Define x and y as integers of length k.  x has the digits of n in descending order, and y has the digits of n in ascending order
# 3) Define z = x - y.  Add leading zeros to z to maintain length k if necessary
# 4) Assign n = z to get the next minion ID, and go back to step 2

# For example, given minion ID n = 1211, k = 4, b = 10, then x = 2111, y = 1112 and z = 2111 - 1112 = 0999. Then the next minion ID will be n = 0999 and the algorithm iterates 
# again: x = 9990, y = 0999 and z = 9990 - 0999 = 8991, and so on.

# Depending on the values of n, k (derived from n), and b, at some point the algorithm reaches a cycle, such as by reaching a constant value. For example, 
# starting with n = 210022, k = 6, b = 3, the algorithm will reach the cycle of values [210111, 122221, 102212] and it will stay in this cycle no matter how many times it continues iterating. 
# Starting with n = 1211, the routine will reach the integer 6174, and since 7641 - 1467 is 6174, it will stay as that value no matter how many times it iterates.

# Given a minion ID as a string n representing a nonnegative integer of length k in base b, where 2 <= k <= 9 and 2 <= b <= 10, write a function solution(n, b) which returns 
# the length of the ending cycle of the algorithm above starting with n. For instance, in the example above, solution(210022, 3) would return 3, since iterating on 102212 would
#  return to 210111 when done in base 3. If the algorithm reaches a constant, such as 0, then the length is 1.

# Languages
# =========

# To provide a Java solution, edit Solution.java
# To provide a Python solution, edit solution.py

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Java cases --
# Input:
# Solution.solution('210022', 3)
# Output:
#     3

# Input:
# Solution.solution('1211', 10)
# Output:
#     1

# -- Python cases --
# Input:
# solution.solution('1211', 10)
# Output:
#     1

# Input:
# solution.solution('210022', 3)
# Output:
#     3

# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. 
# If your solution passes the test cases, it will be removed from your home folder.

# =============================== SOLUTION =======================================

def solution(n, b):
    count = 0
    num = 0
    history = []
    seen_before = []
    
    while num != n:
        if count == 0:
            num = n
        n_array = []
        for letter in num:
            n_array.append(letter)
        
        # Step 1
        x = sorted(n_array, reverse=True)
        y = sorted(n_array)

        # Step 2
        zx = "".join(x)
        zy = "".join(y)

        if b != 10:
            x = convert_to_base10(zx, b)
            y = convert_to_base10(zy, b)
            z = convert_to_baseb((int(x) - int(y)), b)
        else:
            z = int(zx) - int(zy)

        z = str(z) 
        # Step 3
        if len(z) < len(num):
            while len(z) < len(num):
                z = "0" + z

        # Step 4
        num = z
        count += 1

        # If num is in history list and seen_before list then
        # there is a cycle so return length of array holding only unique 
        # numbers that began collecting when fist duplicate was found
        if num not in history:
            history.append(num)
        elif num not in seen_before:
            seen_before.append(num)
        else:
            return len(seen_before)

def convert_to_baseb(n, b):
    n = int(n)
    num = n
    remainder = n
    result = ""
    while num >= b:
        remainder = num % b
        num = num / b
        num = str(num).split(".")[0]
        num = int(num)
        result += str(remainder)
        if num < b:
            result += str(num)

    return result[::-1]

def convert_to_base10(n, b):
    result = 0
    i = len(n) - 1
    for num in n:
        result += int(num) * (b ** int(i))
        i = i - 1

    return result

if __name__ == "__main__":
    assert(solution('1211', 10) == int(1))
    assert(solution('210022', 3) == int(3))
    assert(solution('120', 10) == int(1))
    assert(solution('1', 10) == int(1))

    assert(convert_to_base10("8756", 9) == 6450)
    assert(convert_to_base10("1000000", 2) == 64)
    assert(convert_to_base10("61432", 7) == 14968)

    assert(convert_to_base10("2323", 4) == 187)
    a = convert_to_base10("2323", 4)
    assert(convert_to_base10("1321", 4) == 121)
    b = convert_to_base10("1321", 4)
    result = (int(a) - int(b))
    assert(convert_to_baseb(result, 4) == str(1002))

# foobar:~/hey-i-already-did-that worm2031$ verify solution.py
# Verifying solution...
# All test cases passed. Use submit solution.py to submit your solution
# foobar:~/hey-i-already-did-that worm2031$ submit solution.py 
# Are you sure you want to submit your solution?
# [Y]es or [N]o: Y
# Submitting solution...
# Awesome! Commander Lambda was so impressed by your efforts that you've been promoted to personal assistant. You'll be helping the Commander directly, which means you'll have access to all of Lambda's files -- including the ones on the LAMBCHOP doomsday device. This is the chance you've been waiting for. Can you use your new access to finally topple Commander Lambda's evil empire?
# Submission: SUCCESSFUL. Completed in: 4 hrs, 29 mins, 25 secs.

# Level 2 complete
# You are now on level 3
# Challenges left to complete level: 3

# Level 1: 100% [==========================================]
# Level 2: 100% [==========================================]
# Level 3:   0% [..........................................]
# Level 4:   0% [..........................................]
# Level 5:   0% [..........................................]

# To invite a friend to try a challenge, send the link below. This is a single-use code, so choose wisely.

# Type request to request a new challenge now, or come back later.