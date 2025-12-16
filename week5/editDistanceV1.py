#Name : Thwin Htoo Aung
#Id : 6612109
#Section : 541

#.   Edit distance with recursive brute Force

A = input().strip()
B = input().strip()

def editDistance(A,B,i=0,j=0):
    if i == len(A): #case that A is empty and B still has characters
        return len(B) - j
    if j == len(B): #case that B is empty and A still has characters 
        return len(A) - i
    
    if A[i] == B[j]: #case that characters are same and copy 
        return editDistance(A,B,i+1,j+1) # copy and move forward so i+1 and j+1
    
    insert_cost  = 1 + editDistance(A, B, i, j+1)
    delete_cost  = 1 + editDistance(A, B, i+1, j)
    replace_cost = 1 + editDistance(A, B, i+1, j+1)

    return min(insert_cost, delete_cost, replace_cost)



print(editDistance(A,B))