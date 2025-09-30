marks=int(input("Enter your marks: "))

if marks>=90 and marks<=100:
    Grade= 'A'
elif marks>=70 and marks<90:
    Grade= 'B'
elif marks>=50 and marks<70:
    Grade='C'
elif marks<=0 and marks<50:
    Grade='F'
else:
    Grade='Unassigned'

print("Grade: ",Grade)