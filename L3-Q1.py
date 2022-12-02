# foobar:~/fuel-injection-perfection worm2031$ cat readme.txt 
# Fuel Injection Perfection
# =========================

# Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for the LAMBCHOP doomsday device. 
# It's a great chance for you to get a closer look at the LAMBCHOP -- and maybe sneak in a bit of sabotage while you're at it -- so you took the job gladly. 

# Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time.
#  However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time. 

# The fuel control mechanisms have three operations: 

# 1) Add one fuel pellet
# 2) Remove one fuel pellet
# 3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this 
# to happen if there is an even number of pellets)

# Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. 
# The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

# For example:
# solution(4) returns 2: 4 -> 2 -> 1
# solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
# Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. 
# However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time. 

# The fuel control mechanisms have three operations: 

# 1) Add one fuel pellet
# 2) Remove one fuel pellet
# 3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow 
# this to happen if there is an even number of pellets)

# Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. 
# The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

# For example:
# solution(4) returns 2: 4 -> 2 -> 1
# solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

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
# solution.solution('15')
# Output:
#     5

# Input:
# solution.solution('4')
# Output:
#     2

# -- Java cases --
# Input:
# Solution.solution('4')
# Output:
#     2

# Input:
# Solution.solution('15')
# Output:
#     5

# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. 
# If your solution passes the test cases, it will be removed from your home folder.


# =============================== SOLUTION =======================================

#def solution(n):
    # n = int(n)
    # max_n = n
    # answer = [i + 1 for i in range(2 * max_n)]
    # queue = [i + 1 for i in range(n)]
    # answer[n] = 0
    # while queue:
    #     n = queue[-1]
    #     print(n)
    #     if n == 1:
    #         break
    #     queue.pop()
    #     if n + 1 < 2 * max_n and answer[n] + 1 < answer[n + 1]:
    #         print("adding")
    #         answer[n + 1] = answer[n] + 1
    #         queue.append(n + 1)
    #     elif n - 1 > 0 and answer[n] + 1 < answer[n - 1]:
    #         print("subbing")
    #         answer[n - 1] = answer[n] + 1
    #         queue.append(n - 1)
    #     elif n % 2 == 0 and answer[n] + 1 < answer[int(n/2)]:
    #         print("even")
    #         answer[int(n/2)] = answer[n] + 1
    #         queue.append(int(n/2))
    #     print("length = ", len(queue))
    # print("ANSWER ========", answer)
    # return answer[1]

    # ===========================================================

    # count = 0
    # n = int(n)
    # while n > 1:
    #     if n % 2 == 0:             # bitmask: *0
    #         n = n // 2
    #     elif n == 3 or n % 4 == 1: # bitmask: 01
    #         n = n - 1
    #     else:                      # bitmask: 11
    #         n = n + 1
    #     count += 1
    # return count

    # ===========================================================

def solution(n):
    n = int(n)
    if (n == 1):
        return 0
    elif (n % 2 == 0):
        return 1 + solution(n / 2)
    else:
        return 1 + min(solution(n - 1),
    solution(n + 1))

if __name__ == "__main__":
    assert(solution('4') == 2)
    assert(solution('15') == 5)
    assert(solution('20') == 5)
    assert(solution('762') == 12)
    assert(solution('28') == 6)
    assert(solution('13') == 5)
    assert(solution('10') == 4)
    assert(solution('1') == 0)
    assert(solution('2') == 1)
    print(solution('327402397402398470392740912374203947'))


# def solution(n):
#     n = int(n)
#     count = 0
#     num = 0
#     step_list = []
#     if n == 1:
#         return 0
#     while num != 1:
#         if count == 0:
#             num = n
#         if num % 2 != 0:
#             num = find_min_cost(num)
#             count += 1
#             step_list.append(num)
#             continue
#         num /= 2
#         num = int(num)
#         step_list.append(num)
#         count += 1

#     return count

# def find_min_cost(num):
#     add_count = calc(num + 1)
#     sub_count = calc(num - 1)
#     if add_count < sub_count:
#         return num + 1
#     return num - 1

# def calc(num):
#     count = 0
#     while num != 1:
#         count += 1
#         if num % 2 != 0:
#             num = find_min_cost(num)
#             count += 1
#             continue
#         num /= 2
#         num = int(num)

#     return count