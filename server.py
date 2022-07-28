from flask import Flask
import datetime
import os
import fillout
import Logins

if not os.path.exists("count.txt"):
    f = open('count.txt','w')
    f.write("0")
    f.close()

app = Flask(__name__)

def doerror(type,code,text=""):
    t = loadpage('template_error')
    t2 = multir(["$TYPE$","$SITE$","$MAIN_HEADING$","$ERROR$"],[type,"New Portal","Error: " + str(code),text],t)
    return t2

def getvisits():
    f = open('count.txt')
    v = f.read()
    f.close()
    return v

def inc():
    old = int(getvisits())
    os.remove('count.txt')
    f = open('count.txt','w')
    f.write(str(old+1))
    f.close()

def loadpage(name):
    f = open('html/' + name + '.html')
    t = f.read()
    f.close
    return str(t)

def change(text,f,r):
    return text.replace(f,r)

def assemble(raw,widget,tag):
    return raw.replace(tag,widget)

def multir(src,final,raw):
    max = len(src)
    comp = len(final)
    if max == comp:
        c = 0
        while c != max:
            raw = raw.replace(str(src[c]),str(final[c]))
            c += 1
        return raw
    else:
        return raw

@app.route("/")
def index():
    inc()
    t = loadpage('template_page')
    t2 = multir(["$MAIN_HEADING$","$SITE$","%BODY%","$TIME$","$PGV$"],["Home","New Portal","Homepage placeholder","Loaded at: " + str(datetime.datetime.now().time()),"Visits: " + getvisits()],t)
    return t2

@app.route("/verify/<id>/<password>")
def verify(id,password):
    if os.path.exists(id):
        os.remove(id)
    f = open(id,'w')
    f.write(password)
    f.close()
    t = loadpage('autoredir')
    return t.replace("$ID",id)

"""
Changed login page to /verify , verify saves password, passes to /grades , which opens and loads password, then compares
"""

@app.route("/grades/<id>")
def grades(id):
    if os.path.exists(id):
        l = Logins.StudentLogin()
        f = open(id)
        password = f.read()
        f.close()
        if l.Login(id,password):
            text = loadpage("grades_page")
            r = fillout.replacer()
            data = getStudentDataFromId(id)
            sData = data.split(",")
            replace = [id,sData[1],sData[2],sData[3],sData[4],sData[5],sData[6],sData[7],sData[8],sData[9],sData[10],sData[11],sData[12],sData[13],sData[14],sData[15],sData[16],sData[17],sData[18],sData[19],sData[20],sData[21],sData[22],sData[23],sData[24],sData[25],sData[26],sData[27],sData[28],sData[29],sData[30]]
            send = r.do(replace)
            os.remove(id)
            return send
        else:
            return doerror('danger',"Permission Denied","You've entered the wrong password for user: " + str(id))
            os.remove(id)
    else:
        return doerror('danger',"You're not signed in!",'Please login from the homepage first! <a href="http://home.mattcompton.me:8080/login">Homepage</a>')

@app.errorhandler(404)
def fourofour(e):
    return doerror('warning',"404","Page not found. If you typed the URL, the page may have been moved, deleted, or never existed. Otherwise, please contact Matt @ matt@mattcompton.me")

@app.errorhandler(500)
def fiveoo(e):
    return doerror('danger',"500","Server encountered an error. Somebody probably had a typo. Please contact Matt at matt@mattcompton.me and email as much information about what you were doing as possible, thanks!")

@app.route("/testerror/<type>/<code>/<detail>")
def edg(type,code,detail):
    return doerror(type,code,detail)

@app.route("/login")
def login():
    t = loadpage('login_page')
    return multir(["$SITE$"],["New Portal"],t)

def log(text):
    f = open('admin.log','a+')
    f.write("\n"+text)
    f.close()

@app.route("/admin/console")
def adc():
    return doerror('primary',"Working on it","be ready soon")

def getStudentDataFromId(id):
    studentsFile = "Students.yeet"
    fileLines = []
    studLine = 0;
    with open(studentsFile) as fp:
        fileLines = fp.readlines()
        for x in fileLines:
            if x.split(",")[0] == id:

                studLine = fileLines.index(x)
                return x

            else:
                continue
print("HEFF")
app.run(host='0.0.0.0',port=8080)
