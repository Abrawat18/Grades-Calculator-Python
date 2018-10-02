import compute
import  sys

listOfDict = []
maxA1Score = 0
minPassFail =50
def searchStudId(listOfDict, studentId):
    for item in listOfDict:
        if item["studId"] == studentId:
            return item

with open("class.txt", 'r') as f:
    classList = f.readlines()
for i in classList:
    classData = i.split('|')
    studId = classData[0].rstrip()
    fname = classData[1].rstrip()
    lname = classData[2].rstrip()
    dataDict = {'studId': studId, 'fName': fname, 'lName': lname, 'A1': '0', 'A2': '0', 'PR': '0', 'T1':'0', 'T2' : '0'}
    listOfDict.append(dataDict)

with open("a1.txt", 'r') as f:
    a1List = f.readlines()
    for item in a1List:
        if item.__contains__("|"):
            list = item.split("|")
            studentId = list[0].rstrip()
            recGrade = list[1].rstrip()
            studentData = searchStudId(listOfDict, studentId)
            studentData["A1"] = recGrade
        else:
            maxA1Score = int(item.rstrip())

with open("a2.txt", 'r') as f:
    a2List = f.readlines()
    for item in a2List:
        if item.__contains__("|"):
            list = item.split("|")
            studentId = list[0].rstrip()
            recGrade = list[1].rstrip()
            studentData = searchStudId(listOfDict, studentId)
            studentData["A2"] = recGrade
        else:
            maxA2Score = int(item.rstrip())
with open("project.txt", 'r') as f:
    prList = f.readlines()
    for item in prList:
        if item.__contains__("|"):
            list = item.split("|")
            studentId = list[0].rstrip()
            recGrade = list[1].rstrip()
            studentData = searchStudId(listOfDict, studentId)
            studentData["PR"] = recGrade
        else:
            maxPRScore = int(item.rstrip())
with open("test1.txt", 'r') as f:
    t1List = f.readlines()
    for item in t1List:
        if item.__contains__("|"):
            list = item.split("|")
            studentId = list[0].rstrip()
            recGrade = list[1].rstrip()
            studentData = searchStudId(listOfDict, studentId)
            studentData["T1"] = recGrade
        else:
            maxT1Score = int(item.rstrip())
with open("test2.txt", 'r') as f:
    t2List = f.readlines()
    for item in t2List:
        if item.__contains__("|"):
            list = item.split("|")
            studentId = list[0].rstrip()
            recGrade = list[1].rstrip()
            studentData = searchStudId(listOfDict, studentId)
            studentData["T2"] = recGrade
        else:
            maxT2Score = int(item.rstrip())
com = compute.ComputeGrades()


def mainMenu():
    print("1> Display individual components")
    print("2> Display components average")
    print("3> Display Standard Report")
    print("4> sort by alternate column")
    print("5> change pass/fail point")
    print("6> exit")


while True:
    print('\n')
    mainMenu()
    usr_input = input()
    if usr_input == "1":
        com.displayIndividualComponent(classList)
    elif usr_input == "2":
        com.displayComponentAverage()
    elif usr_input == "3":
        newlist = sorted(listOfDict, key=lambda k: k['studId'])
        com.displayStandardReport(newlist, maxA1Score, maxA2Score, maxPRScore, maxT1Score, maxT2Score, minPassFail)
    elif usr_input == "4":
        com.sort(listOfDict,maxA1Score, maxA2Score, maxPRScore, maxT1Score, maxT2Score, minPassFail)
    elif usr_input == "5":
        com.changePassFailPoint(listOfDict,maxA1Score, maxA2Score, maxPRScore, maxT1Score, maxT2Score, minPassFail)
    elif usr_input == "6":
        print("Good Bye")
        sys.exit()
    else:
        print("Invalid Entry!")
