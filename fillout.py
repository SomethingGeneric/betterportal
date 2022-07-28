class replacer:
    def __init__(self):
        f = open("html/grades_page.html")
        self.raw = f.read()
        f.close()
    def multir(self,src,final):
        max = len(src)
        comp = len(final)
        if max == comp:
            c = 0
            while c != max:
                self.raw = self.raw.replace(str(src[c]),str(final[c]))
                c += 1
            return self.raw
        else:
            return self.raw
    def do(self,data):
        cn = "$CN_x$"
        find_dat = ["$SID$","$SP$"]
        for x in range(1, 8):
            find_dat.append(cn.replace("x",str(x)))
        tn = "$TN_x$"
        for x in range(1, 8):
            find_dat.append(tn.replace("x",str(x)))
        rn = "$RN_x$"
        for x in range(1, 8):
            find_dat.append(rn.replace("x",str(x)))
    #gdl = "$GDL_x$"
    #for x in range(1,8):
    #	find_dat.append(gdl.replace("x",str(x)))
        gdp = "$GDP_x$"
        for x in range(1, 8):
            find_dat.append(gdp.replace("x",str(x)))
        gdp = "$GDL_x$"
        for x in range(1, 8):
            find_dat.append(gdp.replace("x",str(x)))

        f = open('oof','w')
        f.write(str(find_dat))
        f.close()
        
        new = self.multir(find_dat,data)
        return new

    def calcLetter(self, number):
        if number >= 89:
          return 'A'
        elif number >= 79 and number < 89:
          return 'B'
        if number >= 69 and number < 79:
          return 'C'
        if number >= 59 and number < 69:
          return 'D'
        if number < 59:
          return 'E'

#ex
if __name__ == "__main__":
    r = replacer()
    replace = ["135039","yeet","Digital Art","AP NSL","Chemistry","English 10","Algebra 2","Microcomputer Tech","Website Design","Vorhees","Gallagher","Jewell","Judge","Kalabakas","N-Asli","Villman","F127","A407","F208","F118","C105","B302","B302","100","100","100","100","100","100","100",]
    text = r.do(replace)
    print(text)
