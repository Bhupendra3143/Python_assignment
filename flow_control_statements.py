class StudentMarks:
    def __init__(self, name, marks):
        self.name = name
        self.maths = marks["maths"]
        self.physics = marks["physics"]
        self.chemistry = marks["chemistry"]\
        
    def evaluation(self):
        if(self.maths >= 35 and self.chemistry >= 35 and self.physics >= 35):
            return True
        return False
    
    def studentStatus(self):
        if self.evaluation():
            print(f"{self.name} has Passed")
        else:
            print(f"{self.name} has Failed")

    def grading(self):
        avgNum = (self.maths + self.chemistry + self.physics)/3
        if avgNum <= 59:
            return "C Grade"
        elif avgNum <= 69:
            return "B Grade"
        else:
            return "A Grade"
        
    def displayGrades(self):
        print(f"{self.name} scored {self.grading()}")


if __name__ == "__main__":
    print("Enter the number of students : ")
    numOfStudents = int(input())
    studentCard = []
    
    for it in range(0, numOfStudents):
        print("Enter name of Student : ")
        name = input()
        print("Enter marks : ")
        print("Maths : ")
        maths = int(input())
        print("Physics : ")
        physics = int(input())
        print("Chemistry : ")
        chemistry = int(input())
        marks = {"maths" : maths, "physics" : physics, "chemistry" : chemistry}
        student = StudentMarks(name, marks)
        studentCard.append(student)

    for it in studentCard:
        it.studentStatus()
        it.displayGrades()



