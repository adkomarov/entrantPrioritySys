
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

req_101001=ReferReq(3)
req_101002=ReferReq(2)
req_101003=ReferReq(1)

reqAll=[req_101001,
        req_101002,
        req_101003]
#print(len(reqAll))

declarAll=[]
import csv
with open('testTry10-2.csv', newline='') as csvfile:
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
for i in range(8):
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
