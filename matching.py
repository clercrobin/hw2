from random import randrange

p = 1000000009

def pow(x, n):
    if n == 0:
        return 1
    b = pow(x, n//2)
    if n % 2 == 0:
        return (b * b) % p
    else:
        return (((b * b) % p) * x) % p
        
def inv(x):
    return pow(x, p-2)
    
def det(A):
    n = len(A)
    # Gauss-Jordan elimination
    for j in range(0, n-1):
        # Find a row with nonzero coefficient at column j
        i0 = None
        for i in range(j, n):
            if A[i][j] != 0:
                i0 = i
                break
        if i0 is None:
            break
        A[j], A[i0] = A[i0], A[j]
        # Substract the row
        for i in range(j+1, n):
            b = (A[i][j] * inv(A[j][j])) % p
            for k in range(j, n):
                A[i][k] = (A[i][k] - ((b * A[j][k]) % p)) % p
    # Compute the determinant
    d = 1
    for i in range(n):
        d = (d * A[i][i]) % p
    return d
    
def generate_matrix(n, edges):
    A = [[0] * n for _ in range(n)]
    for i, j in edges:
        x = randrange(p)
        A[i][j] = x
        A[j][i] = (-x) % p
    return A
    
n, m = map(int, input().split())
edges = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(m)]

N = 100
for _ in range(N):
    if det(generate_matrix(n, edges)) != 0:
        print('YES')
        exit()
print('NO')

