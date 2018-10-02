class ComputeGrades:


    studIdList = []
    fnameList = []
    lnameList = []
    studIdListInAssign = []
    gradesList = []
    maxScore = 0
    average = 0
    a1List = []
    a2List = []

    def getAssigmentGrades(self, type):
        with open(type, 'r') as f:
            list = f.readlines()
            self.studIdListInAssign.clear()
            self.gradesList.clear()
            for i in list:
                if i.__contains__("|"):
                    list1 = i.split("|")
                    self.studIdListInAssign.append(list1[0].rstrip())
                    self.gradesList.append(list1[1].rstrip())
                else:
                    self.maxScore = i.rstrip()


    def getStudentData(self, classList):
            self.studIdList.clear()
            self.fnameList.clear()
            self.lnameList.clear()
            for i in classList:
                listData = i.split("|")
                self.studIdList.append(listData[0].rstrip())
                self.fnameList.append(listData[1].rstrip())
                self.lnameList.append(listData[2].rstrip())


    def getRequestedData(self, classList, component_name):
        s = ComputeGrades()
        if component_name == "A1":
            s.getAssigmentGrades("a1.txt")
        elif component_name == "A2":
            s.getAssigmentGrades("a2.txt")
        elif component_name == "PR":
            s.getAssigmentGrades("project.txt")
        elif component_name == "T1":
            s.getAssigmentGrades("test1.txt")
        elif component_name == "T2":
            s.getAssigmentGrades("test2.txt")
        else:
            print("Invalid Entry!")
        s.getStudentData(classList)
        print(component_name.ljust(9), "grades".ljust(7), "(", s.maxScore, ")")
        for i in range(len(s.studIdList)):
            for j in range(len(s.studIdListInAssign)):
                if s.studIdList[i] == s.studIdListInAssign[j]:
                    name = s.lnameList[i]+", "+s.fnameList[i]
                    print(s.studIdList[i].ljust(7), name.ljust(14), s.gradesList[j])

    def displayIndividualComponent(self, classList):
        print("Enter component name A1, A2, PR, T1 or T2:")
        s = ComputeGrades()
        component_name = input().upper()
        if component_name == "A1":
            s.getRequestedData(classList, component_name)
        elif component_name == "A2":
            s.getRequestedData(classList, component_name)
        elif component_name == "PR":
            s.getRequestedData(classList, component_name)
        elif component_name == "T1":
            s.getRequestedData(classList, component_name)
        elif component_name == "T2":
            s.getRequestedData(classList, component_name)
        else:
            print("Invalid Entry!")
            s.displayIndividualComponent(classList)

    def getAverage(self, type, component_name):
        total = 0
        s = ComputeGrades()
        s.getAssigmentGrades(type)
        for k in s.gradesList:
            if k != '':
                total = total + int(k)
            average = round(total / len(s.gradesList), 2)
        print(component_name, " average: ", average, "/", s.maxScore)

    def displayComponentAverage(self):
        print("Enter component name A1, A2, PR, T1 or T2:")
        s = ComputeGrades()
        component_name = input().upper()
        if component_name == "A1":
            s.getAverage("a1.txt", component_name)
        elif component_name == "A2":
            s.getAverage("a2.txt", component_name)
        elif component_name == "PR":
            s.getAverage("project.txt", component_name)
        elif component_name == "T1":
            s.getAverage("test1.txt", component_name)
        elif component_name == "T2":
            s.getAverage("test2.txt", component_name)
        else:
            print("Invalid Entry!")
            s.displayComponentAverage()

    def calculateGrade(self, total, passFailPoint):
        limit = (100 - passFailPoint)/7
        if total <= passFailPoint:
            grade = 'F'
        elif total > passFailPoint and total <= passFailPoint + limit:
            grade = 'C'
        elif total> passFailPoint + limit  and total <= passFailPoint + (limit * 2):
            grade = 'B-'
        elif total > passFailPoint + (limit *2) and total <= passFailPoint +(limit * 3):
            grade = 'B'
        elif total > passFailPoint +(limit * 3) and total <=passFailPoint +(limit * 4):
            grade = 'B+'
        elif total > passFailPoint +(limit * 4) and total<= passFailPoint +(limit * 5):
            grade = 'A-'
        elif total > passFailPoint +(limit * 5) and total<= passFailPoint +(limit * 6):
            grade = 'A'
        elif total > passFailPoint +(limit * 6) and total<= passFailPoint +(limit * 7):
            grade = 'A+'
        return grade


    def displayStandardReport(self, listOfDict,maxA1Score, maxA2Score, maxPRScore, maxT1Score, maxT2Score, passFailPoint):
        s = ComputeGrades()

        print("ID".ljust(7), "LN".ljust(7), "FN".ljust(7), "A1".ljust(7), "A2".ljust(7), "PR".ljust(7), "T1".ljust(7), "T2".ljust(7), "GR".ljust(7), "FL".ljust(7))

        for dataDict in listOfDict:
            if dataDict['A1'] != '':
                A1 = int(dataDict['A1'])/maxA1Score * 7.5
            else:
                A1 = 0
            if dataDict['A2'] != '':
                A2 = int(dataDict['A2']) / maxA2Score * 7.5
            else:
                A2 = 0
            if dataDict['PR'] != '':
                PR = int(dataDict['PR']) / maxPRScore * 25
            else:
                PR = 0
            if dataDict['T1'] != '':
                T1 = int(dataDict['T1']) / maxT1Score * 30
            else:
                T1 = 0
            if dataDict['T2'] != '':
                T2 = int(dataDict['T2']) / maxT2Score * 30
            else:
                T2 = 0
            GR = round((A1 + A2 + PR + T1 + T2), 2)
            dataDict['GR'] = GR
            grade = s.calculateGrade(GR, passFailPoint)
            dataDict['grade'] = grade
            print(dataDict['studId'].ljust(7), dataDict['lName'].ljust(7), dataDict['fName'].ljust(7), dataDict['A1'].ljust(7), dataDict['A2'].ljust(7), dataDict['PR'].ljust(7), dataDict['T1'].ljust(7), dataDict['T2'].ljust(7), str(GR).ljust(7), grade)

    def sort(self,listOfDict, maxA1Score, maxA2Score, maxPRScore, maxT1Score, maxT2Score, passFailPoint):
        print("Enter sort key: LT(Last name) or GR(numeric grade)")
        usrinput = input().upper()
        s = ComputeGrades()
        if usrinput == 'LT':
            newlist = sorted(listOfDict, key=lambda k: k['lName'])
            s.displayStandardReport(newlist, maxA1Score, maxA2Score, maxPRScore, maxT1Score, maxT2Score, passFailPoint)
        elif usrinput == 'GR':
            newlist = sorted(listOfDict, key=lambda k: k['GR'], reverse = True)
            s.displayStandardReport(newlist, maxA1Score, maxA2Score, maxPRScore, maxT1Score, maxT2Score, passFailPoint)
        else:
            print("Invalid Entry!")
            s.sort(listOfDict, maxA1Score, maxA2Score, maxPRScore, maxT1Score, maxT2Score, passFailPoint)

    def changePassFailPoint(self, listOfDict,maxA1Score, maxA2Score, maxPRScore, maxT1Score, maxT2Score, passFailPoint):
        print("Please enter new Pass/Fail point:")
        newPoint = input()
        passFailPoint = int(newPoint)
        s = ComputeGrades()
        newlist = sorted(listOfDict, key=lambda k: k['studId'])
        s.displayStandardReport(newlist,maxA1Score, maxA2Score, maxPRScore, maxT1Score, maxT2Score, passFailPoint)