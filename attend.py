import re
from datetime import datetime
today = datetime.now()
d1 = today.strftime("%d-%m-%Y \nTime - %H:%M")
f = open("d:\pro.txt","r")
lines = f.readlines()
l = [i.rstrip("\n") for i in lines]
x = []
total,total1,present,absent=[],[],[],[]
pattern = re.compile(r'\d\d-[a-zA-Z0-9]+|[a-zA-Z0-9]+\s+[a-zA-Z0-9]+')
for i in l:
        match = pattern.search(i)
        total.append(match.group())
total.sort()
numbers = ['0','1','2','3','4','5','6','7','8','9']
alphabets = ['19-5D','19-5E','19-5F','19-5G','19-5H','19-5I','19-5J','20-50','20-51']
for i in alphabets:
            for j in numbers:
                           if i == '19-5D' and j == '0':
                                             pass
                           elif i == '19-5G' and j == '2':
                                             pass
                           elif i == '19-5J' and j == '4':
                                             break
                           elif (i == '20-50') and (j == '0'):
                                             pass
                           elif (i == '20-50') and (j == '1'):
                                             pass
                           elif (i == '20-50') and (j == '5'):
                                             pass
                           elif (i == '20-50') and (j == '7'):
                                             pass
                           elif (i == '20-51') and (j == '0'):
                                             pass
                           elif (i == '20-51') and (j == '1'):
                                             pass
                           elif (i == '20-51') and (j == '2'):
                                             pass
                           elif (i == '20-51') and (j == '4'):
                                             break
                           else:
                                             x.append(i+j)
for k in x:
            if  k not in total:
                           absent.append(k)
            else:
                           present.append(k)
print("Today's date:", d1)
print("Total Students Present : ", len(present))
print("Total Students Absent : ", len(absent))
print("Absentees :  ",absent)