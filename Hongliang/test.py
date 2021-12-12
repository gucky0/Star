# Imaginary Question 1L average, dictionary for sum

filename = "data.txt" #input("prompt")
##infile = open(filename, 'r')
##infile.readline() # <- discard 1st line
##data = infile.readlines()

##filename = "result.txt"
##outfile = open(filename, "w")

# Qn 1
d = {}
for line in data: # line: "STUDENT 1     32     54     25"
    scores = data.split()[2:] # scores: ['32', '54', '25']
    total = 0
    for num in scores: # num: 22
        total += float(num)
    for i in range(1, len(data)):
        d[f"student_{i}"] = total


# Qn 2
# 80 -> A
# 70 B
# 60 F
def give_grade(score): 
    if  score >= 80:
        grade = 'A'
    elif score >= 70:
        grade = 'B'
    else:
        grade = 'C'
    return grade

good = 0
medium = 0
bad = 0

for line in data:
    scores = data.split() # -> ['32', '54', '25']
    total = 0
    for score in scores:
        total += score
    avg = total / len(scores)
    grade = give_grade(avg)
    if grade == 'A':
        good += 1
    elif grade == 'B':
        medium += 1
    elif grade == 'C':
        bad += 1
    
print("Number of students that scored A: ", good, "\n")
print("Number of students that scored B: ", medium, "\n")
print("Number of students that scored C: ", bad, "\n")

# Qn 3
'''
"s1 s2 s3 ..." x
" physics 32 15 51"
" maths 15 52 51
'''
d = {}
##infile.readline() # <- discard 1st line
    
#assume number of students is 10
for index in len(10):
    d[f"student_{index+1}"] = 0

for index, row in enumerate(data): #line: physics 32 15 51
    splitted = row.split() # "physics", "32", "15", "51", ....
    scores = spliited[1:] # "32", "15", "51", ..
    num_of_students = len(scores)
##    student_1 = scores[0]   #s1 p  s1 p
##    student_2 = scores[1]
    d[f"student_{index+1}"] += float(scores[index])

for index in len(10):
    d[f"student_{index+1}"] = [f"student_{index+1}"] / 10
    
##infile.close()
##outfile.close()

for num in line:
    try:
        int(num)
    except:
        print("error")
        









