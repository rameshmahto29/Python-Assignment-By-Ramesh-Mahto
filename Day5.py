#Day5 Assignment
lt = [9, 12, 15, 45, 55, 60, 70, 80, 100, 120]
divi = list(filter(lambda x:(x % 15 == 0), lt))
print("Numbers divisible by 3 & 5 are : ", divi)