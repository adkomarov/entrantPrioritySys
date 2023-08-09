
import json
import csv
'''
f = open('text.txt', 'wr')
for row in f:
    print(row)
'''
class ReferReq:
    def __init__(self,cT):
        self.cT=cT
        self.cList=[]
    def __repr__(self):
        return self.cList
    def countNV(self):
        return len(self.cList)-self.cT
    @property
    def name(self):
        for k, v in globals().items():
            if v == self: return k;

req_150304=ReferReq(40)
req_070301=ReferReq(49)
req_380305=ReferReq(9)
req_070304=ReferReq(9)
req_070303=ReferReq(14)
req_380310=ReferReq(5)
req_090301=ReferReq(90)
req_090302=ReferReq(22)
req_150305=ReferReq(25)
req_220301=ReferReq(18)
req_150301=ReferReq(58)
req_380302=ReferReq(10)
req_220302=ReferReq(38)
req_120301=ReferReq(19)
req_090303=ReferReq(28)
req_090304=ReferReq(51)
req_190303=ReferReq(38)
req_420301=ReferReq(2)
req_430301=ReferReq(14)
req_080301=ReferReq(187)
req_130301=ReferReq(15)
req_150302=ReferReq(29)
req_230301=ReferReq(36)
req_200301=ReferReq(30)
req_270304=ReferReq(39)
req_030302=ReferReq(18)
req_180301=ReferReq(71)
req_380301=ReferReq(9)
req_180302=ReferReq(43)
reqAll=[req_150304,
        req_070301,
        req_380305,
        req_070304,
        req_070303,
        req_380310,
        req_090301,
        req_090302,
        req_150305,
        req_220301,
        req_150301,
        req_380302,
        req_220302,
        req_120301,
        req_090303,
        req_090304,
        req_190303,
        req_420301,
        req_430301,
        req_080301,
        req_130301,
        req_150302,
        req_230301,
        req_200301,
        req_270304,
        req_030302,
        req_180301,
        req_380301,
        req_180302]
#print(len(reqAll))
'''
ct_090304=37
ct_090302=15
ct_090301=61
'''

declarAll=[]
import csv
with open('testTry13-3.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)#, delimiter=',', quotechar=',')
    for row in spamreader:
        declar=(str(row)[2:-2]).split(";")
        declarPost=[declar[0],int(declar[1]),int(declar[2]),declar[3].replace(".","")]
        declarAll.append(declarPost)

declarAll3=declarAll
from itertools import groupby

#declarAll = [el for el, _ in groupby(declarAll3)]

'''
declarAll.sort(reverse=True, key=lambda declar: declar[1])
for i in declarAll:
    print(i)
'''


flag=True
i=0
k=0
for i in range(10000):
    failedSnilsAll=[]

    i+=1

    failedSnils=[]#те у кого понижаем в приор
    '''
    for req in reqAll:#по кодировкам-специализациям
        req.cList.sort(key=lambda declar: declar[1])#сортировка списка абитур на кодировку
    '''
    for declar in declarAll:#пробегаем по всем заявлениям
        if declar[2]==1:#где приор равен 1
            for req in reqAll:#пробегаем по списку специальности
                if declar[3] in req.name:#если нашли кодировку направления у абитур в имени переменной списка направления#print(declar)#print(1)
                    #print(declar)
                    req.cList.append(declar)#добавили в список абитур на эту кодировку
                    declarAll.remove(declar)#удалили из списка всех заявлений
                   
    for req in reqAll:#по кодировкам-специализациям
        req.cList.sort(key=lambda declar: declar[1])#сортировка списка абитур на кодировку

    '''
    w=0
    for req in reqAll:
        w+=1
        print(w)
        for declar in req.cList:
            print(req.name,declar[0],declar[1],declar[2])
        print('\n')
    '''
    for req in reqAll:
        while req.countNV()>0:
            req.cList.sort(key=lambda declar: declar[1])#сортировка списка абитур на кодировку
            #print(req.cList[0])#добавили первое заявление (с наим баллов) в фейл снилсы (те кто не смогли пройти)
            failedSnils.append(req.cList[0][0])
            req.cList.remove(req.cList[0])
    '''
    w=0
    for req in reqAll:
        w+=1
        print(w)
        for declar in req.cList:
            print(req.name,declar[0],declar[1],declar[2])
        print('\n')
    '''
    
    ''' 
    w=0
    for req1 in reqAll:#по кодировкам-специализациям
        #print(req1.name)
        req1.cList.sort(key=lambda declar: declar[1])#сортировка списка абитур на кодировку
        #print(req1.cList)
        for declar1 in req1.cList:#по заяв в кодировке
            #req1.cList.sort(key=lambda declar: declar[1])#сортировка списка абитур на кодировку
            #print(declar1)
            if req1.countNV()>0:#если больше возможных мест#print(2)
                w+=1
                print(declar1)
                failedSnils.append(declar1[0])#добавили первое заявление (с наим баллов) в фейл снилсы (те кто не смогли пройти)
                req1.cList.remove(declar1)#вырезали из списка абитур того кто не прошел!!!!!!баг
                #print(declar in failedSnils,declar in req.cList)
    #print(w)    
    #failedSnils=list(set(failedSnils)) 
    #print(len(failedSnils))
    '''
    
    for m in failedSnils:#пробежались по пониженным
        #print(m)
        for declar in declarAll:#по заявл в общем списке
            if m == declar[0]:#снилсы совпали#
                #print(declar[0])
                g=declar[2]
                declar[2]-=1#повышаем приоритет у этого снилса по остальным направлениям так как он не прошел по 1 приор
                #failedSnils.remove(m)
                #print(i in failedSnils)
                #print(declar ==g)
    failedSnilsAll+=failedSnils
    failedSnils.clear()#очистили пониженных
    #print(failedSnils)
'''
for i in failedSnils:
        print(type(i))
#print(failedSnilsAll)
'''

#print(req_090301.cList)



w=0
for req in reqAll:
    w+=1
    print(w)
    for declar in req.cList:
            print(req.name,declar[0],declar[1])
    print('\n')
#print(i)

'''
for i in failedSnilsAll:
    print(i)

preflag=False#префлаг
    for declar in declarAll:#по всем заявлениям
        if declar[2]==1:#если хотяб где-то 1 приор
            preflag=True#установка продолжать цикл до полного перебора
    if preflag == False:
        flag=False


'''
#print(len(failedSnilsAll),len(set(failedSnilsAll)))
#print(failedSnilsAll,set(failedSnilsAll))

