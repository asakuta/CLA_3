import math
import sys

def analyse():
    if len(sys.argv) > 1:
        File=sys.argv[1]
        handle=open(File, "r")
        text=handle.read()
        handle.close()
        lines=text.split("\n")
        catList=lines[0].split(",")
        cat={}
        for x in range(0, len(catList)):
            cat[catList[x]]=x
        newData=[]        
        for y in range(1, len(lines)-1):
            newLine=lines[y].split(",")
            salary=int(newLine[cat["Salary"]])
            bonus=int(newLine[cat["Bonus"]])
            if newLine[cat["Currency"]] != "GBP":
                rate=newLine[cat["Currency"]]
                value1=convert(salary, rate)
                value2=convert(bonus, rate)
                salary=value1
                bonus=value2
            newLine[cat["Salary"]]=salary
            newLine[cat["Bonus"]]=bonus
            total=0
            if "+" in newLine[cat["Total"]]:
                data=newLine[cat["Total"]].split("+")
                key1=cat[data[0]]
                value1=newLine[key1]
                key2=cat[data[1]]
                value2=newLine[key2]
                total=value1+value2
            else:
                if "-" in newLine[cat["Total"]]:
                    data=newLine[cat["Total"]].split("-")
                    key1=cat[data[0]]
                    value1=newLine[key1]
                    key2=cat[data[1]]
                    value2=newLine[key2]
                    total=value1-value2
            newLine[cat["Total"]]=round(total, 2)
            obj={}
            for z in range(0, len(catList)-1):
                obj[catList[z]]=newLine[z]
            newData.insert(len(newData), obj)
        column=sys.argv[2]
        finalData=sortBy(newData, column)
        for item in finalData:
            print(item)
    else:
        print("nope")

def convert(salary, rate):
    rates={"USD": 1.39, "JPY": 151.99, "HUF": 429.22} #as of 15.03.2021
    newSalary=round(salary/rates[rate], 2)
    return(newSalary)

def sortBy(List, category):
    original=[]
    values=[]
    for x in range(0, len(List)):
        original.insert(len(original), List[x][category])
        values.insert(len(values), List[x][category])
    ranking=[]
    while len(values) > 0:
        highest=max(values)
        for x in range(0, len(original)):
            if original[x] == highest:
                ranking.insert(len(ranking), x)
        newList=[]
        for item in values:
            if item != highest:
                newList.insert(len(newList), item)
        values=newList
    sortedData=[]
    for item in ranking:
        obj=List[item]
        sortedData.insert(len(sortedData), obj)
    return(sortedData)

analyse()