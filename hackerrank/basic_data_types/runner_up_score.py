# HackerRank - Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # 1. Convert the map to a set to remove duplicate scores
    unique_scores = set(arr)
    
    # 2. Remove the absolute maximum score from the set
    unique_scores.remove(max(unique_scores))
    
    # 3. The new maximum of the remaining numbers is your runner-up!
    print(max(unique_scores))