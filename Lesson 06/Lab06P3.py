# Lesson 6 problem 3

# get user input for Jean's four scores
print("Please enter Jean's scores one by one.")
jeans_scores = []
for i in range(4):
	jean_score = int(input('Enter a score: '))
	jeans_scores.append(jean_score)
print("Jean's scores:", jeans_scores)
print()

# get user input for Kayla's four scores
print("Please enter Kayla's scores one by one.")
kaylas_scores = []
for i in range(4):
	kayla_score = int(input('Enter a score: '))
	kaylas_scores.append(kayla_score)
print("Kayla's scores:", kaylas_scores)
print()

# get user input for Connie's four scores
print("Please enter Connie's scores one by one.")
connies_scores = []
for i in range(4):
	connie_score = int(input('Enter a score: '))
	connies_scores.append(connie_score)
print("Connie's scores:", connies_scores)
print()

# create a list that is a list of jean's scores, kayla's scores and
# connie's scores
all_scores = [jeans_scores, kaylas_scores, connies_scores]
print('All scores:', all_scores)

# add one point to each score using a set of nested for loops
for row in range(3):
	for col in range(4):
		all_scores[row][col] = all_scores[row][col] + 1
print("All scores after extra point: ", all_scores)

# sort each list inside all_scores and redisplay all_scores
for i in range(3):
	all_scores[i].sort()
print("All score's afer sorting:", all_scores)
