# HackerRank - Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []
    scores = set()
    
    # 1. Read input and save names and scores
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.add(score)
        
    # 2. Sort the unique scores and grab the second item (index 1)
    sorted_scores = sorted(scores)
    second_lowest_score = sorted_scores[1]
    
    # 3. Use a standard beginner loop to look for matching students
    runner_ups = []
    for student in students:
        if student[1] == second_lowest_score:
            runner_ups.append(student[0])
            
    # 4. Sort the names alphabetically and print them
    runner_ups.sort()
    for name in runner_ups:
        print(name)