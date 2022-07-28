class GradeChanger:


    def __init__(self):
        self.studentsFile = "Students.yeet"
        self.fileLines = []
        self.loginLine = 0;

    def changeGrade(self,ID,class,percentage):
        with open(self.studentsFile) as fp:
            self.fileLines = fp.readlines()
            for x in self.fileLines:
                elements = x.split(",")
                if elements[0] == ID:
                    self.loginLine = fileLines.index(x)
                    elements[22] + class = percentage
                    break
                else:
                    continue
