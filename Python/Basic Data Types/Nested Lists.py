students = []
scores = []
for _ in range(int(input())):      #add student and scores to a list as a list
    name = input()
    score = float(input())
    students.append([name, score])
           
for i in range(len(students)):     #add only scores in a new list 
    scores.append(students[i][1])
        
students.sort()                    #sort for names
scores.sort()    
second_minimum = sorted(set(scores))[1] #second minimum
    
for i in range(len(students)):     #look for second minimum scores in students
    if(students[i][1]) == second_minimum:
        print(students[i][0])
