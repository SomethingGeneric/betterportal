new = []
names = ["ID: ","Password: ","Class name 1: ","Class name 2: ","Class name 3: ","Class name 4: ","Class name 5: ","Class name 6: ","Class name 7: ","Teacher name 1: ","Teacher name 2: ","Teacher name 3: ","Teacher name 4: ","Teacher name 5: ","Teacher name 6: ","Teacher name 7: ","Room # 1: ","Room # 2: ","Room # 3: ","Room # 4: ","Room # 5: ","Room # 6: ","Room # 7: ","Grade (number) 1:","Grade (number) 2:","Grade (number) 3:","Grade (number) 4:","Grade (number) 5:","Grade (number) 6:","Grade (number) 7:",]

max = len(names)
c = 0
while c != max:
    text = input(str(names[c]))
    new.append(text)
    c += 1
f = open('Students.yeet','a+')
f.write("\n"+str(new).replace('"',"").replace("[","").replace("]",""))
f.close()
