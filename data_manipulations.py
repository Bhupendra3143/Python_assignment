students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 40},
    {"name": "Charlie", "score": 75},
    {"name": "Diana", "score": 90},
    {"name": "Eve", "score": 30}
]

# You are given a list of dictionaries representing student data.
# 1.Sort the list of students in descending order of their scores using a lambda function.
# 2.Filter out students who scored less than 50, again using a lambda function.
# 3.Combine both operations to first filter and then sort the students who scored 50 or more.

student_marks = sorted(students, key = lambda x : x["score"], reverse = True)
