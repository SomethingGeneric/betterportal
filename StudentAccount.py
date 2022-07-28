import sys, re

class StudentAccount:
    username = ""
    password = ""
    Id = 000000
    email = str(Id) + "@mcpsmd.net"
    studentLine = 0;

    def __init__(self, username, password, Id):
        self.username = username
        self.password = password
        self.Id = Id
    def recordData(Line,c1,c2,c3,c4,c5,c6,c7,t1,t2,t3,t4,t5,t6,t7,r1,r2,r3,r4,r5,r6,r7,p1,p2,p3,p4,p5,p6,p7):
        studentsFile = "Students.yeet"
        fileLines = []

        with open(studentsFile) as fp:
            fileLines = fp.readlines()
            studLine = fileLines[Line].split(",")
            studLine[2] = c1
            studLine[3] = c2
            studLine[4] = c3
            studLine[5] = c4
            studLine[6] = c5
            studLine[7] = c6
            studLine[8] = c7
            studLine[9] = t1
            studLine[10] = t2
            studLine[11] = t3
            studLine[12] = t4
            studLine[13] = t5
            studLine[14] = t6
            studLine[15] = t7
            studLine[16] = r1
            studLine[17] = r2
            studLine[18] = r3
            studLine[19] = r4
            studLine[20] = r5
            studLine[21] = r6
            studLine[22] = r7
            studLine[23] = p1
            studLine[24] = p2
            studLine[25] = p3
            studLine[26] = p4
            studLine[27] = p5
            studLine[28] = p6
            studLine[29] = p7
