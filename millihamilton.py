import os
import sys
import random

def make_cycle(n):
    result = []
    for i in xrange(n):
        line = [0]*n
        line[(i+1)%n] = 1
        line[i-1] = 1
        result.append(line)
    return result
    
def make_random(n):
    result = []
    for i in xrange(n):
        line = []
        for j in xrange(n):
            if i == j:
                line.append(0)
            else:
                line.append(random.choice([0,1]))
        result.append(line)
    return result
    
def make_complete(n):
    result = []
    for i in xrange(n):
        line = [1]*n
        result.append(line)
    return result
        
def make_line(itemstr):
    items = itemstr.replace(",", " ").split()
    return map(int, items)
    
def verify(matrix):
    if not matrix:
        return False
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return False
    return True
        
def main(fname):
    input = ""
    if os.path.exists(fname):
        f = open(fname)
        for l in f:
            if l.strip() and not l.strip()[0] == "#":
                input += l.strip() + ";"
        input = input[:-1]
    else:
        input = fname
    matrix = []
    if input.startswith("C"):
        matrix = make_cycle(int(input.split()[1]))
    elif input.startswith("K"):
        matrix = make_complete(int(input.split()[1]))
    elif input.startswith("R"):
        matrix = make_random(int(input.split()[1]))
    else:
        matrix = map(make_line, input.split(";"))
        if not verify(matrix):
            print "Matrix is not square, aborting"
            sys.exit(-1)
    n = len(matrix)
    map = {}
    for i in xrange(n):
        map[(i,i)] = ">"
        vertex = "V"
        if i == 0:
            vertex = "*"
        map[(2*n,i+n)] = vertex
        map[(2*n+i+2,n-i-1)] = "D"
        map[(2*n+1,i+n)] = vertex
        map[(i,3*n-i-1)] = "U"
        map[(n+i,2*n+i)] = "L"
        map[(2*n,i)] = "="
        map[(2*n+1,i)] = "="
        map[(2*n+2+i,n+i)] = "<"
        for j in xrange(n):
             map[(i+n,j+n)] = str(matrix[i][j])
             map[(i,j+n)] = "|"
             map[(i+n,j)] = "="

        for j in xrange(i):
             map[(j,i)] = "|"
             map[(n-i+j,2*n+i)] = "="
             map[(n+j,2*n+i)] = "="
             map[(n+i,2*n+j)] = "?"
             map[(2*n+j+2,n-i-1)] = "="
             map[(2*n+2+j,n+i)] = "-"
             map[(2*n+2+i,n-i+j)] = "|"
             map[(2*n+2+i,n+j)] = "|"

        for j in xrange(n-i-1):
             map[(j,2*n+i)] = "|"
             map[(j+i+1,i)] = "="


    for y in xrange(3*n+2):
        for x in xrange(3*n+2):
            if (x,y) in map:
                print map[(x,y)],
            else:
                print " ",
        print
        
    
    
        
if __name__ == "__main__":
    main(" ".join(sys.argv[1:]))