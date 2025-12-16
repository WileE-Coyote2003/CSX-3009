#Name : Thwin Htoo Aung
#Id : 6612109
#Section : 541

#.   Edit distance recursive brute Force with memorization

A = input().strip()
B = input().strip()

memo = {} # stores results for (i, j)


def editDistance(A,B,i=0,j=0):
    if (i,j) in memo:
        return memo[(i,j)]
    
    if i == len(A): #case that A is empty and B still has characters
        return len(B) - j
    if j == len(B): #case that B is empty and A still has characters 
        return len(A) - i
    if A[i] == B[j]: #case that characters are same and copy 
        memo[(i,j)] = editDistance(i+1,j+1) # copy and move forward so i+1 and j+1
        return memo[(i,j)]

    insert_cost  = 1 + editDistance(i, j+1)
    delete_cost  = 1 + editDistance(i+1, j)
    replace_cost = 1 + editDistance(i+1, j+1)

    memo[(i,j)] = min(insert_cost, delete_cost, replace_cost)
    return memo[(i,j)]
    

print(editDistance(A,B))