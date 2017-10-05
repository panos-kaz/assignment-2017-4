"four russians algorithm"
"Panagiotis Kazantzis \ 8130049"
import csv
import sys
def initialization():
    filename1 = sys.argv[-1]
    filename2 = sys.argv[-2]
    if filename2 == sys.argv[0]:
        graph = []
        with open(filename1, 'r') as f:
            graph = [[int(num) for num in line.split()] for line in f]
        result = closure(graph)
        for s in result:
            for g in s:
                print(*g)
    else:
        with open (filename1) as f1:
            reader = csv.reader(f1)
            rows1 = [row for row in reader]
        file1 = [list(map(int, row)) for row in rows1]
        with open(filename2) as f2:
            reader = csv.reader(f2)
            rows2 = [row for row in reader]
        file2 = [list(map(int, row)) for row in rows2]
        result = multiply(file2, file1)
        for s in result:
            str1=','.join(str(e) for e in s)
            print(str1)
    filename1 = None
    filename2 = None


#multiplys the tables of the files
def multiply(fileA, fileB):
    tableA = [[]]
    tableB = [[]]
    tableA = fileA
    tableB = fileB
    n = len(tableA)
    tableC = [[0]*n]*n
    lg = 1
    while 2**lg<n:
        lg = lg+1
    lg = lg -1
    i = 1
    #if necessary fill with zeros
    if n%lg != 0:
        while i<=(lg - n%lg):
            tableB.append([0]*n)
            tableA = [row + [0] for row in tableA]
            i =i+1
    i = 1
    y = 0
    s = 0
    tableC = [[0]*n]*n
    while i<n//lg +1:
        Ci = []
        tA = []
        tAi = [[]*n]*lg
        tBi = [[]*lg]*n
        #split the tables
        for c in range(lg):
            tA.append([r[y+c] for r in tableA])
        tBi = tableB[s*lg:i*lg]
        #take only the wanted part of tableB
        tAi = [[j[i] for j in tA] for i in range(len(tableA))]
        #swap rows and columns for tableA to take tableAi
        j = 1
        k = 0
        bp = 1
        rs = []
        rs.append([0]*n)
        tAB = []
        rtBi = []
        tBi.reverse()
        rtBi = tBi
        while j < 2**lg:
            count = 0
            #calculate rs
            L = []
            while count<n:
                if rs[j-2**k][count] == 0 and rtBi[k][count] == 0:
                        L.append(0)
                else:
                        L.append(1)
                count = count+1
            rs.append(L)
            if bp == 1:
                bp = j+1
                k = k+1
            else:
                bp = bp-1
            j = j+1
        j =0
        #calculate tAB
        while j < n:
            x = 0
            w = 0
            while w < lg:
                x = x + tAi[j][w]*2**(lg-w-1)
                #transform the binary number
                w = w+1
            tAB.append(rs[x])
            j = j+1
        #add tAB to the final table
        for q in range(n):
            Cx = []
            count = 0
            while count<n:
                if tableC[q][count] == 0 and tAB[q][count] == 0:
                    Cx.append(0)
                else:
                    Cx.append(1)
                count = count+1
            Ci.append(Cx)
            #print(Ci)
        tableC = Ci
        y = y+lg
        #delete all the lists that i want to found again for the next round
        del tA [:]
        del tAi [:]
        del tBi [:]
        del rtBi [:]
        del tAB [:]
        i =i+1
        s = s+1

    return tableC

def closure(graph):
    n = len(graph)
    A = []
    i = 0
    #create a nxn binary table
    # 1 for connection / 0 for no connection
    while i <= n:
        a = []
        j=0
        while j <= n:
            if i!=n:
                if i==j:
                    a.append(1)
                elif graph[i] == [i, j]:
                    a.append(1)
                else:
                    a.append(0)
            else:
                if i==j:
                    a.append(1)
                else:
                    a.append(0)
            j=j+1
        A.append(a)
        i=i+1
    Ax = A
    # multiply A^n-1 * A
    for i in range(n):
        Ax = multiply(Ax, A)
    G = []
    # reverse back to a list of 2 columns and n rows
    for i in range(n+1):
        g = []
        j = 0
        for j in range(n+1):
            if Ax[i][j] == 1:
                g.append([i, j])
        G.append(g)
    return G
initialization()
