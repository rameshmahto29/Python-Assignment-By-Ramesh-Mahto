#Day3 Assignment
marks = {"Hindi" : 71, "English" : 75, "Mathematics" : 98, "Science" : 98, "Social Science" : 80}
maximum = max(marks.values())
result = list(filter(lambda x:marks[x] == maximum,marks.keys()))
print(result)