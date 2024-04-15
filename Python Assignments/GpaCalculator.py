b = int(input('Enter Your Bangla Subject Marks: '))
e = int(input('Enter Your English Subject Marks: '))
m = int(input('Enter Your Math Subject Marks: '))
s = int(input('Enter Your Science Subject Marks: '))


avg = (b + e + m + s) / 4

if avg <= 40:
    grade = "F"
elif 41 <= avg <= 60:
    grade = "D"
elif 61 <= avg <= 70:
    grade = "C"
elif 71 <= avg <= 80:
    grade = "B"
elif 81 <= avg <= 90:
    grade = "A"
else:
    grade = "A+"

print("Your Grade:", grade)