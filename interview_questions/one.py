# A gym membership card allows entry for one week from Monday to Sunday.
# Ellis attends the gym once a day at most. You are given a list visits of length N, which represents the days Ellis visits the gym, in chronological order. What is the minimum number of gym membership cards that Ellis has to purchase?
# Write a function:
# def solution(visits)
# ?
# that, given a list visits of length N, returns the minimum number of gym membership cards that Ellis must purchase based on the order of visits specified. Days of the week in visits are represented as three-letter strings ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun").
# Examples:
# 1. For visits = ['Tue", "Sat", "Mon", "Fri], the function should return 2. In the
# first week, Ellis visits the gym on Tuesday and Saturday. In the second week, Ellis visits the gym on Monday and Friday.
# 2. For visits = ["Mon", "Mon", "Mon"], the function should return 3. Ellis visits
# the gym only on Monday each week.
# 3. For visits = ["sun", "Sat", "Fri", "Thu", "Wed", "Tue", "Mon"], the function
# You sent
# should return 7.
# Assume that:
# • N is an integer within the range [1.100);
# • the only strings in visits are: "Mon", "Tue", "Wed", "Thu", "Fri", "Sat" and/or "Sun".

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(visits):
    # Implement your solution here
    days = {"Mon": 1,
    "Tue":2,"Wed":3,"Thu":4,"Fri":5,"Sat":6,"Sun":7}
    result = 0
    for i in range(len(visits)):
        if i == 0:
            result += 1
        elif days[visits[i]]<=days[visits[i-1]]:
            result += 1
        else:
            continue
    return result