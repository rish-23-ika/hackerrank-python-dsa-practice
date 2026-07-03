# HackerRank - Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # 1. Convert to a list and sort it from smallest to largest
    sorted_scores = sorted(list(set(arr)))
    
    # 2. Grab the second-to-last item (the runner-up!)
    print(sorted_scores[-2])