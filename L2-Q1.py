# foobar:~/power-hungry cat readme.txt 
# Power Hungry
# ============

# Commander Lambda's space station is HUGE. And huge space stations take a LOT of power. Huge space stations with doomsday devices take even more power. 
# To help meet the station's power needs, Commander Lambda has installed solar panels on the station's outer surface. But the station sits in the middle 
# of a quasar quantum flux field, which wreaks havoc on the solar panels. You and your team of henchmen have been assigned to repair the solar panels, 
# but you'd rather not take down all of the panels at once if you can help it, since they do help power the space station and all!

# You need to figure out which sets of panels in any given array you can take offline to repair while still maintaining the maximum amount of power output per array, 
# and to do THAT, you'll first need to figure out what the maximum output of each array actually is. Write a function solution(xs) that takes a list of integers representing 
# the power output levels of each panel in an array, and returns the maximum product of some non-empty subset of those numbers. So for example, if an array contained panels 
# with power output levels of [2, -3, 1, 0, -5], then the maximum product would be found by taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30.  
# So solution([2,-3,1,0,-5]) will be "30".

# Each array of solar panels contains at least 1 and no more than 50 panels, and each panel will have a power output level whose absolute value is no greater than 1000 
# (some panels are malfunctioning so badly that they're draining energy, but you know a trick with the panels' wave stabilizer that lets you combine two negative-output 
# panels to produce the positive output of the multiple of their power values). The final products may be very large, so give the solution as a string representation of the number.

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit Solution.java

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Python cases --
# Input:
# solution.solution([2, 0, 2, 2, 0])
# Output:
#     8

# Input:
# solution.solution([-2, -3, 4, -5])
# Output:
#     60

# -- Java cases --
# Input:
# Solution.solution({2, 0, 2, 2, 0})
# Output:
#     8

# Input:
# Solution.solution({-2, -3, 4, -5})
# Output:
#     60

# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. 
# If your solution passes the test cases, it will be removed from your home folder.

# =============================== SOLUTION =======================================

def solution(xs):
    # case only 1 num in list
    if len(xs) == 1:
        return str(xs[0])

    max_product_list = []

    # add largest num in list to max product candidates
    max_product_list.append(max(xs))

    # get product of all nums in list and add it to max product candidates
    max_product = 1
    for num in xs:
        max_product *= num
    max_product_list.append(max_product)

    # seperate pos and neg nums
    pos_list = []
    neg_list = []
    num_negs = 0
    for num in xs:
        if num > 0:
            pos_list.append(num)
        elif num < 0:
            neg_list.append(num)
            num_negs += 1

    # if <= 2 neg numbers in list it won't effect output because cancelling and largest num possible is all of them combined so return product now
    if num_negs == 0 or num_negs == 2:
        max_product = 1
        combined_list = pos_list + neg_list
        for num in combined_list:
            max_product *= num
        return str(max_product)
    
    # sort list bigggest to smallest then find num of neg numbers in list and remove smallest if uneven num so list length even 
    neg_list.sort()
    remaining = max(neg_list)
    if len(neg_list) % 2 != 0:
        remaining = neg_list[-1]
        neg_list.pop(-1)
    
    # group sorted neg list into pairs to get biggest combos possible
    newlist = [neg_list[i:i+2] for i in range(0, len(neg_list), 2)]

    # find product of each pair and add to a list for later
    neg_pair_list = []
    for neg_pairs in newlist:
        neg_pair_product = 1
        for num in neg_pairs:
            neg_pair_product *= num
        neg_pair_list.append(neg_pair_product)

    # add the remainder num taken from uneven neg list
    neg_pair_list.append(remaining)

    # add neg combo list and pos num list to find product of each number with every other number
    max_product = min(xs)
    combined_list = pos_list + neg_pair_list
    for num in combined_list:
        product = num
        max_product = 0
        for num2 in combined_list:
            if num2 != num:
                product *= num2
                if product > max_product:
                    max_product = product
        max_product_list.append(max_product)
    max_product_list.append(max_product)

    # return the max num from cadidate list
    return str(max(max_product_list))

if __name__ == "__main__":
    assert(solution([2, -3, -6, 4]) == "144")
    assert(solution([2, -3, 1, 0, -5]) == "30")
    assert(solution([2, 0, 2, 2, 0]) == "8")
    assert(solution([-2, -3, 4, -5]) == "60")
    assert(solution([2, 3]) == "6")
    assert(solution([9, 8, 2, 4, 1, 8]) == "4608")
    assert(solution([5, 9, 8, 2]) == "720")
    assert(solution([2, 5, 8]) == "80")
    assert(solution([0]) == "0") # this test case made me realise why a test was failing, i was returning 0 (int) not "0" (string)
    assert(solution([2]) == "2")
    assert(solution([-80]) == "-80")
    
# foobar:~/power-hungry verify solution.py
# Verifying solution...
# All test cases passed. Use submit solution.py to submit your solution
# foobar:~/power-hungry worm2031$ submit solution.py
# Are you sure you want to submit your solution?
# [Y]es or [N]o: Y
# Submitting solution...
# Submission: SUCCESSFUL. Completed in: 9 hrs, 38 mins, 32 secs. //MY COMMENT: I spent like 9hours debugging one failing test that was solved by casting int to str in an edge case ... doh

# Current level: 2
# Challenges left to complete level: 1

# Level 1: 100% [==========================================]
# Level 2:  50% [=====================.....................]
# Level 3:   0% [..........................................]
# Level 4:   0% [..........................................]
# Level 5:   0% [..........................................]

# Type request to request a new challenge now, or come back later.
