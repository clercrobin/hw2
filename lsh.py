import numpy as np

alpha = 10
N = 1000000

def h(p, thetas):
    d = np.minimum(np.abs(p - thetas), (p - thetas) % 360)
    return (d <= alpha).astype(int)
    
def estimate_proba(p, q):
    thetas = np.random.rand(N) * 360
    return (h(p, thetas) == h(q, thetas)).mean()

# p1
p = np.random.rand() * 360
q = (p + np.random.rand()) % 360
print('p = {}, q = {}, p1 = {}'.format(p, q, estimate_proba(p, q)))

# p2
p = np.random.rand() * 360
q = (p + np.random.rand() * 340 + 10) % 360
print('p = {}, q = {}, p2 = {}'.format(p, q, estimate_proba(p, q)))

    
