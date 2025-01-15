import csv

def validEntry(listvar):
    for it in listvar[2:]:
        if not it.isdigit():
            return False
    return True

def averageCal(listvar):
    total = 0
    count = 0
    for it in listvar[2:]:
        total += int(it)
        count += 1
    return total, int(total/count)

if __name__ == "__main__":
    csvread = csv.reader(open(r"C:\Users\Bhupendrajeet\Downloads\student_scores.csv", 'r'))
    marks_list = []
    header = next(csvread)
    marks_list.append(header + ["Total", "Average"])
    for entry in csvread:
        if not validEntry(entry):
            continue
        total, avg = averageCal(entry)
        entry = entry + ([total, avg])
        marks_list.append(entry)
    with open ("processed_student_scores.csv", "w", newline="\n") as f:
        writercsv = csv.writer(f)
        for it in marks_list:
            writercsv.writerow(it)

    

