if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    score = student_marks[query_name]

    if query_name in student_marks:
        print("{0:.02f}".format(sum(score)/len(score)))
