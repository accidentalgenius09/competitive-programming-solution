'''
	Topic : Algorithms
	Subtopic : Grading Students

	Problem Statement :
		Complete the function gradingStudents in the editor below.
		It should return an integer array consisting of rounded grades.

	Url : https://www.hackerrank.com/challenges/grading/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
	# Write your code here
	for i in range(len(grades)):
		if grades[i] > 37:
			if(grades[i]%5 >= 3):
				grades[i] = grades[i]+(5-grades[i]%5)
	return grades
		

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	grades_count = int(input().strip())

	grades = []

	for _ in range(grades_count):
		grades_item = int(input().strip())
		grades.append(grades_item)

	result = gradingStudents(grades)

	fptr.write('\n'.join(map(str, result)))
	fptr.write('\n')

	fptr.close()