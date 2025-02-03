n = int(input("Enter number of students: "))
while n > 0:
    name = input("Enter student's name: ")
    print("Enter marks for five subjects out of 100: ")
    m1 = int(input())
    m2 = int(input())
    m3 = int(input())
    m4 = int(input())
    m5 = int(input())
    tot = m1 + m2 + m3 + m4 + m5
    per = (tot / 500) * 100
    print(f"Name: {name}")
    print(f"Total Marks: {tot}")
    print(f"Percentage: {per:.2f}%")
    if per > 90:
        print("Grade: A")
    elif per > 80:
        print("Grade: B")
    elif per > 70:
        print("Grade: C")
    elif per > 60:
        print("Grade: D")
    elif per > 35:
        print("Grade: P")
    else:
        print("Grade: F")
    n -= 1