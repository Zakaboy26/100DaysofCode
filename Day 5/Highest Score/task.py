student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
#print(range(1, 10))

#total_examscore = sum(student_scores) allows u to add numbers, even items in lists
#print(total_examscore)

#We could do the same manually too in a primitive manner:
#sum = 0
#for score in student_scores:
#    sum += score #starts from zero, but accumulates by adding each score
#print(sum) #outputs the correct sum

#primitive way of doing max method:
max_score = student_scores[0]
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)