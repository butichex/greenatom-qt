""" Напиши функцию на Python, выполняющую сравнение версий. Условия: 
Return -1 if version A is older than version B 
Return 0 if versions A and B are equivalent 
Return 1 if version A is newer than version B 
Each subsection is supposed to be interpreted as a number, therefore 1.10 > 1.1. """

comparisonResult = -1 | 0 | 1

def compare(A: str, B: str) -> comparisonResult:
    A = [int(x) for x in A.split(".")]
    B = [int(x) for x in B.split(".")]
    
    for i in range(max(len(A), len(B))):
        if i >= len(A):
            return -1
        elif i >= len(B):
            return 1
        elif A[i] > B[i]:
            return 1
        elif A[i] < B[i]:
            return -1
        
    return 0


if __name__ == '__main__':
    A = '1.10'
    B = '1.1'
    print(compare(A, B))
