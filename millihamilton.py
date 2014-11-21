import os
import sys
import random
import gadgets
import md5

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
    
def moveto(str, (x,y)):
    result = ""
    for l in str.split("\n"):
        if "(position" in l:
            items = l.strip().split()
            if len(items) != 4:
                result += l + "\n"
                print "WEIRD LINE", items, len(items)
            else:
                result += "        %s %d %d %s\n"%(items[0], int(items[1])+x, int(items[2])+y, items[3])
        else:
            result += l + "\n"
    return result
        
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
    lmap = {}
    for i in xrange(n):
        lmap[(i,i)] = ">"
        vertex = "V"
        if i == 0:
            vertex = "*"
        lmap[(2*n,i+n)] = vertex
        lmap[(2*n+i+2,n-i-1)] = "D"
        lmap[(2*n+1,i+n)] = vertex
        lmap[(i,3*n-i-1)] = "U"
        lmap[(n+i,2*n+i)] = "L"
        lmap[(2*n,i)] = "="
        lmap[(2*n+1,i)] = "="
        lmap[(2*n+2+i,n+i)] = "<"
        for j in xrange(n):
             lmap[(i+n,j+n)] = str(matrix[i][j])
             lmap[(i,j+n)] = "|"
             lmap[(i+n,j)] = "="

        for j in xrange(i):
             lmap[(j,i)] = "|"
             lmap[(n-i+j,2*n+i)] = "="
             lmap[(n+j,2*n+i)] = "="
             lmap[(n+i,2*n+j)] = "?"
             lmap[(2*n+j+2,n-i-1)] = "="
             lmap[(2*n+2+j,n+i)] = "-"
             lmap[(2*n+2+i,n-i+j)] = "|"
             lmap[(2*n+2+i,n+j)] = "|"

        for j in xrange(n-i-1):
             lmap[(j,2*n+i)] = "|"
             lmap[(j+i+1,i)] = "="


    for y in xrange(3*n+2):
        for x in xrange(3*n+2):
            if (x,y) in lmap:
                print lmap[(x,y)],
            else:
                print " ",
        print
    matrixstr = ";".join(map(lambda r: ",".join(map(str, r)), matrix))
    
    outf = open("%d_%s"%(n, md5.new(matrixstr).hexdigest()), "w")
    print >> outf, gadgets.HEADER%(input, n+1, n+1, n, n, 3*n, (n*3+5)*620, (n*3+5)*650)
    for (x,y) in lmap:
        if lmap[(x,y)] in gadgets.GADGETMAP:
            print >>outf, moveto(gadgets.GADGETMAP[lmap[(x,y)]], (x*620,y*650))
    print >> outf, "))"
    outf.close()
    
        
if __name__ == "__main__":
    main(" ".join(sys.argv[1:]))