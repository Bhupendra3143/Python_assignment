import json
data = json.load(open(r"C:\Users\Bhupendrajeet\Downloads\sample_data.json", 'r'))
average_dict = dict()

for student in data["students"]:
    total = 0
    count = 0
    x = student["details"]["grades"]
    completed_subject = [subject["scorw"] for subject in x.values() if subject["completed"]]
    
    for subject, status in student["details"]["grades"].items():
        if status["completed"]:
            total += status["score"]
            count += 1
    if count != 0:
        average_dict[f"{student["name"]}"] = total/count
    else:
        average_dict[f"{student["name"]}"] = 0

max = float(-1e9)
topper = ""
for name, avg in average_dict.items():
    if max < avg:
        topper = name

print(average_dict)
print(topper)



    
