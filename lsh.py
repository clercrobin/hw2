import numpy as np

k = 3
alpha = 10
N = 1000000

def h(p, thetas):
    d = np.minimum(np.abs(p - thetas), (p - thetas) % 360)
    return (d <= alpha).astype(int)
    
def estimate_proba(p, q):
    thetas = np.random.rand(N, k) * 360
    h_p = np.max(h(p, thetas), 1)
    h_q = np.max(h(q, thetas), 1)
    return (h_p == h_q).mean()

# p1
p = np.random.rand() * 360
q = (p + np.random.rand()) % 360
print('p = {}, q = {}, p1 = {}'.format(p, q, estimate_proba(p, q)))

# p2
p = np.random.rand() * 360
q = (p + np.random.rand() * 340 + 10) % 360
print('p = {}, q = {}, p2 = {}'.format(p, q, estimate_proba(p, q)))

    
