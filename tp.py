import random

k=7


def permutation(lst):
 
    
    if len(lst) == 0:
        return []
 
 
    if len(lst) == 1:
        return [lst]
 
 
    l = []
 
    for i in range(len(lst)):
       m = lst[i]
 
       
       remLst = lst[:i] + lst[i+1:]
 
       
       for p in permutation(remLst):
           l.append([m] + p)
    return l
        
        

def pcmax(n1,m1):
    n = int(n1)
    m = int(m1)
    #f= open("result.txt", "x")
    
    
    pi = []
    for b in range(n):
        pi.append(random.randint(1, 1000))
        
        
    ti = []
    ci = []
    orde = []
    ordeK = pi[:k]
    resultri={}
    AK={}
    ak = []
    bk = []
    All = []
    bestSolIndice = 0
    allSol = {}
    BRUTTE={}
    
    sortredri = sorted(pi,reverse=True)

    
    resultri = {}
    
    #task with in machines
    
    machines = [[] for i in range(m)]
 
    #time with in machines
    
    machinesTimes = []
    
    for j in range(0,n) :
        resultri["T" + str(j+1)] =  pi[j]
        
    resultri = {k: v for k, v in sorted(resultri.items(), key=lambda item: item[1], reverse=True)}
    
    AK = dict(list(resultri.items())[:k])
    BK = dict(list(resultri.items())[k:])
    for y in AK:
        ak.append(y)

    for z in BK:
        bk.append(z)
    
    for p in permutation(ak):
        All.append(p)
        

    

        
    for u in range(len(All)):
        
        
    
        completion_times = [0 * m for _ in range(m)]

        
        c=0
        for i in All[u]:
            if(c==m):
                c=0
            completion_times[c] = completion_times[c] + AK[i]
            c = c+1
        makespan = max(completion_times)
        BRUTTE[u] = makespan

          
    #la sol optimal
    r = min(BRUTTE,key=BRUTTE.get)
    
    c=0    
    for f in All[r] :
        if(c==m):
            c=0
        machines[c].append(f)
        
    
        c = c+1
        
    for w in machines:
        g=0
        sommes = 0
        for z in w:
            sommes = sommes+ resultri[z]
        machinesTimes.append(sommes)
        

    cMax = BRUTTE[r]
    
    #sol optimae de K premier element 
    PartSol = All[r]
    
    
    #remaing tasks
    
    remaing = dict(list(resultri.items())[k:])
    
    #remaing tasks BK,bk
    
    #

    for job in bk:
        
        machine_index = machinesTimes.index(min(machinesTimes))
        machines[machine_index].append(job)
        machinesTimes[machine_index] = machinesTimes[machine_index] + BK[job]
   
    

        
    print(machines) #l'odre sur chaque machine
    print(machinesTimes)  #le cmax de chauqe machine
    print(max(machinesTimes)) #le cmax total
    
 
    return max(machinesTimes)


pcmax(100,10)