import StudentAccount, TeacherAccount

class StudentLogin:
    def __init__(self):
        studentsFile = "Students.yeet"
        fileLines = []
        loginLine = 0;
        with open(studentsFile) as fp:
            self.fileLines = fp.readlines()


    def Login(self,id,password):

        for x in self.fileLines:
            if x.split(",")[0] == id:
                if(x.split(",")[1] == password):
                    loginLine = self.fileLines.index(x)
                    return True
                else:
                    break
            else:
                continue

        return False
