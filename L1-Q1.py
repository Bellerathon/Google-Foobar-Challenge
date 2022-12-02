# The cake is not a lie!
# ======================

# Commander Lambda has had an incredibly successful week: the first test of the LAMBCHOP doomsday device was completed AND Lambda set a new personal high score in Tetris. To celebrate, the Commander ordered cake for everyone -- even the lowliest of minions! But competition among minions is fierce, and if you don't cut exactly equal slices of cake for everyone you'll get in big trouble.

# The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest of the cake is uniform, the M&Ms are not: there are multiple colors, and every minion must get exactly the same sequence of M&Ms. Commander Lambda hates waste and will not tolerate any leftovers, so you also want to make sure you can serve the entire cake.

# To help you best cut the cake, you have turned the sequence of colors of the M&Ms on the cake into a string: each possible letter (between a and z) corresponds to a unique color, and the sequence of M&Ms is given clockwise (the decorations form a circle around the outer edge of the cake).

# Write a function called solution(s) that, given a non-empty string less than 200 characters in length describing the sequence of M&Ms, returns the maximum number of equal parts that can be cut from the cake without leaving any leftovers.

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
# solution.solution("abcabcabcabc")
# Output:
#     4

# Input:
# solution.solution("abccbaabccba")
# Output:
#     2

# -- Java cases --
# Input:
# Solution.solution("abcabcabcabc")
# Output:
#     4

# Input:
# Solution.solution("abccbaabccba")
# Output:
#     2

#===================== SOLUTION ============================

def solution(s):
    max = 0
    for i in range(1, len(s) + 1, 1):
        if ((s.count(s[:i]) > max) and ((len(s[:i])) * s.count(s[:i]) == len(s))):
            max = s.count(s[:i])

# if __name__ == "__main__":
#     solution("abcabcabcabc")

# ========================================

# foobar:~/the-cake-is-not-a-lie verify solution.py
# Verifying solution...
# All test cases passed. Use submit solution.py to submit your solution

#==========================================

# Submitting solution...
# You survived a week in Commander Lambda's organization, and you even managed to get yourself promoted. Hooray! Henchmen still don't have the kind of security access you'll need to take down Commander Lambda, though, so you'd better keep working. Chop chop!
# Submission: SUCCESSFUL. Completed in: 43 mins, 30 secs.









#                                                                                                      @   @@
#                                                                                                     /@% @$%@
#                                                                                                    @((%%%////@
#                                                                                                    @///@~/// @
#                                                                                                    @//@///////@
#                                                                                                   @///%@~~~~@
#                                                                                                  /@$$$$@///~~@
#                                                                                                  @   %/@%%//$//@@
#                                                                                                 @$   ////(((((/~     /%%///////@@    /$//@@/
#                                                                                                @$ //@@@((((      %@@//~~~/////@ /@$      @$/
#                                                                                               @$/( @  @((((~     %  ~~~~~~~~~///@@        @\
#                                                                                               @  /((@@@((((//         ~~~~~~~////////@      @
#                                                                                               @ ~   (((((((((           ~~~~~~~~~////@   $@
#                                                                                                @      ((((((           ~~~~~~~~~//////@$@@
#                                                                                                 @@/$                 ~~~~~~~~(~~~~////@$
#                                                                                                   //@@@%%/~          ~~~~~~((((////////@
#                                                                                                        $~          /  ~~~~(////////(($@
#                                                                                                      @$$        $$/    ~~~~((((((%%%@
#                                                                                                     $@         %      ~~(((((((%%%%%@
#                                                                                                       // / @   @ /   $$$$%%%%%%%%@
#                                                                                                       @@@@@   @////@@@@@@@@@@@@@
# Level 1 complete
# You are now on level 2
# Challenges left to complete level: 2

# Level 1: 100% [==========================================]
# Level 2:   0% [..........................................]
# Level 3:   0% [..........................................]
# Level 4:   0% [..........................................]
# Level 5:   0% [..........................................]

# Type request to request a new challenge now, or come back later.
