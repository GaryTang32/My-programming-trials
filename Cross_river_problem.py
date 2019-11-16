def genstates():
    z =""
    v =[]
    for i in range(0,4):
        v.append("")
    for i in range(0,2):
        if v[0] == "":
            v[0] = "E"
        elif v[0]=="E":
            v[0] = "W"
        else:
            v[0] = "E"
        for u in range(0,2):
            if v[1] == "":
                v[1] = "E"
            elif v[1]=="E":
                v[1] = "W"
            else:
                v[1] = "E"
            for y in range(0,2):
                if v[2] == "":
                    v[2] = "E"
                elif v[2]=="E":
                    v[2] = "W"
                else:
                    v[2] = "E"
                for t in range(0,2):
                    if v[3] == "":
                        v[3] = "E"
                        z = z +"".join(v)+" "
                    elif v[3]=="E":
                        v[3] = "W"
                        z = z +"".join(v)+" "
                    else:
                        v[3] = "E"
                        z = z +"".join(v)+" "
    z = z.split()
    return z

def validstates(a):
    v=[]
    for z in a:
        x = z
        if x[1] == x[2] and x[0] != x[1]:
            v.append(x)
        elif x[2] == x[3] and x[0] != x[2]:
            v.append(x)
    for z in v:
        a.remove(z)
    return a

def possible_states(s):
    d=len(s)
    c=[]
    for i in range(0,d):
        c.append([])   
    for v in range(0,d):
        z = s[v]
        for x in s:
            counter2=0
            if x[0] != z[0]:
                if x[1]!=z[1]:
                    counter2=counter2+1
                if x[2]!=z[2]:
                    counter2=counter2+1
                if x[3]!=z[3]:
                    counter2=counter2+1
                if counter2 == 1 or counter2 == 0:
                    c[v].append(x)
    return c     

def gen_path(a):
    path = []   
    path.append([])
    valid = validstates(genstates())
    possible = a
    path[0].append(valid[0])
    finish = False
    path3 = []
    final_path = []
    while not finish:
        length_of_path = len(path)
        path2 = []
        if len(path) > 1:
            
            for u in range (0,length_of_path):
                counter4 = path.count(path[u])
                if counter4 > 1 :
                    path2.append(path[u])                        
            for i in path2:
                path.remove(i)
        for i in range (0,len(path)):
            dummy = path[i]
            dummy1 = dummy[-1]
            index = valid.index(dummy1)
            next_path = possible[index]
            counter1 = 0           
            path1 = list(path[i])
            for o in range(0,len(next_path)):
                dummy2 = next_path[o]
                counter = 0
                for p in range(0,len(path1)):
                    if path1[p] == dummy2 :
                        counter = 1
                if counter == 0 and counter1 == 0:
                    counter1 = 1
                    path[i].append(dummy2)
                elif counter == 0 and counter1 != 0:
                    path.append(path1)
                    path[-1].append(dummy2)
        counter3 = 0
        for i in range(0,len(path)):
            path3 = path[i]
            if path3[-1] == 'WWWW' :
                final_path.append(path3)
                counter3 = counter3 + 1
        if counter3 !=0:
            finish = True
            return final_path
def print_states(path):
    list1 = []
    list2 = []
    action = [0,0,0,0]
    direction = ''
    print(path)
    print()
    for i in range(0,len(path)):        
        print('Path ',i+1)
        for o in range(1,len(path[i])):
            action = [0,0,0,0]
            list1 = path[i][o-1]
            list2 = path[i][o]
            if list1[0] != list2[0]:
                action[0] = 1
                if list2[0] == 'W':
                    direction = 'west'
                else:
                    direction = 'east'
            if list1[1] != list2[1]:
                action[1] = 1
                if list2[0] == 'W':
                    direction = 'west'
                else:
                    direction = 'east'
            if list1[2] != list2[2]:
                action[2] = 1
                if list2[0] == 'W':
                    direction = 'west'
                else:
                    direction = 'east'
            if list1[3] != list2[3]:
                action[3] = 1
                if list2[0] == 'W':
                    direction = 'west'
                else:
                    direction = 'east'
            if action[1] == 1:
                print(str(o)+'.','The man takes the cabbage to the',direction,end='.\n')
            elif action[2] == 1:
                print(str(o)+'.','The man takes the goat to the',direction,end='.\n')
            elif action[3] == 1:
                print(str(o)+'.','The man takes the wolf to the',direction,end='.\n')
            else:
                print(str(o)+'.','The man takes himself to the',direction,end='.\n')
        print()
    print()
            
            
def genstates1():
    z =""
    v =[]
    for i in range(0,3):
        v.append("")
    for i in range(0,2):
        if v[0] == "":
            v[0] = "E"
        elif v[0]=="E":
            v[0] = "W"
        else:
            v[0] = "E"
        for u in range(0,2):
            if v[1] == "":
                v[1] = "E"
            elif v[1]=="E":
                v[1] = "W"
            else:
                v[1] = "E"
            for y in range(0,2):
                if v[2] == "":
                    v[2] = "E"
                    z = z +"".join(v)+" "
                elif v[2]=="E":
                    v[2] = "W"
                    z = z +"".join(v)+" "
                else:
                    v[2] = "E"
                    z = z +"".join(v)+" "
                
    z = z.split()
    return z

def possible_states1(s):
    d=len(s)
    c=[]
    for i in range(0,d):
        c.append([])   
    for v in range(0,d):
        for o in range(3):
            z = list(s[v])
            if z[o] == 'E':
                z[o] = 'W'
            else:
                z[o] = 'E'
            x = ''.join(z)
            c[v].append(x)
    return c

def gen_path1(a):
    path = []
    path.append([])
    valid = genstates1()
    possible = a
    path[0].append(valid[0])
    finish = False
    path3 = []
    final_path = []
    while not finish:
        length_of_path = len(path)
        path2 = []
        if len(path) > 1 :
            for u in range(0,length_of_path):
                counter4 = path.count(path[u])
                if counter4 > 1:
                    path2.append(path[u])
            for i in path2:
                path.remove(i)
        for i in range (0,len(path)):
            dummy = path[i]
            dummy1 = dummy[-1]
            index = valid.index(dummy1)
            next_path = possible[index]
            counter1 = 0
            path1 = list(path[i])
            for o in range(3):
                dummy2 = next_path[o]
                counter = 0
                for p in range(0,len(path1)):
                    if path1[p] == dummy2:
                        counter = 1
                if counter == 0 and counter1 == 0:
                    counter1 += 1
                    path[i].append(dummy2)
                elif counter == 0 and counter1 != 0:
                    path.append(list(path1))
                    path[-1].append(dummy2)
        counter3 = 0
        path4 = []
        for i in range(0,len(path)):
            path3 = path[i]
            if path3[-1] == 'WWW':
                dummy4 = path3[-2]
                dummy5 = path3[1]
                if dummy4 == 'WEW'  and dummy5 == 'EWE':
                    final_path.append(path3)
                    counter3 += 1
                else:
                    path4.append(path3)
        if counter3 != 0:
            finish = True
            return final_path
        for o in path4:
            path.remove(o)

def print_states1(path):
    list1 = []
    list2 = []
    action = [0,0,0,0]
    direction = ''
    print(path)
    print()
    for i in range(0,len(path)):        
        print('Path ',i+1)
        
        flag = 'E'
        o = 1
        h = 0
        while o != len(path[i]):
            action = [0,0,0]
            list1 = path[i][o-1]
            list2 = path[i][o]
            if flag == 'W':
                flag = 'E'
                direction = 'east'
            else:
                flag = 'W'
                direction = 'west'
            if list1[0] != list2[0] and flag == list2[0]:
                action[0] = 1
                o += 1
                if list2[0] == 'W':
                    direction = 'west'
                else:
                    direction = 'east'
                
            if list1[1] != list2[1] and flag == list2[1]:
                action[1] = 1
                o += 1
                if list2[1] == 'W':
                    direction = 'west'
                else:
                    direction = 'east'
            if list1[2] != list2[2] and flag == list2[2]:
                action[2] = 1
                o += 1
                if list2[2] == 'W':
                    direction = 'west'
                else:
                    direction = 'east'
            h = h+1
            if action[0] == 1:
                print(str(h)+'.','The man takes the cabbage to the',direction,end='.\n')
            elif action[1] == 1:
                print(str(h)+'.','The man takes the goat to the',direction,end='.\n')
            elif action[2] == 1:
                print(str(h)+'.','The man takes the wolf to the',direction,end='.\n')
            else:
                print(str(h)+'.','The man takes himself to the',direction,end='.\n')
        print()
    print()

print_states(gen_path(possible_states(validstates(genstates()))))

print_states1(gen_path1(possible_states1(genstates1())))


