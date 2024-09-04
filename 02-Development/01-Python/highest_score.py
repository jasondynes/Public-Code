# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# high_score = max(student_scores)
for n in range(0, len(student_scores)):
    if n != len(student_scores)- 1:
        if student_scores[n] > student_scores[n + 1]:
            swap = student_scores[n + 1]
            student_scores[n + 1] = student_scores[n]
            student_scores[n] = swap
high_score = student_scores[-1]
print(f"The highest score in the class is: {high_score}")



