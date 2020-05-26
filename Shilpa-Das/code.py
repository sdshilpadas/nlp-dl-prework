# --------------
# Code starts here

import numpy as np

# Code starts here

# Adjacency matrix
adj_mat = np.array([[0,0,0,0,0,0,1/3,0],
                   [1/2,0,1/2,1/3,0,0,0,0],
                   [1/2,0,0,0,0,0,0,0],
                   [0,1,0,0,0,0,0,0],
                  [0,0,1/2,1/3,0,0,1/3,0],
                   [0,0,0,1/3,1/3,0,0,1/2],
                   [0,0,0,0,1/3,0,0,1/2],
                   [0,0,0,0,1/3,1,1/3,0]])

# Compute eigenvalues and eigencevectrs
values,vectors=np.linalg.eig(adj_mat)
print('eigenvalues',values, 'eigenvectors',vectors)

# Eigen vector corresponding to 1
eigen_1=abs(vectors[:,0])/np.linalg.norm(vectors[:,0],1)
print('eigen_1',eigen_1)

# most important page
page=np.where(np.max(eigen_1) == eigen_1)[0][0] + 1

print('page', page)

# Code ends here


# --------------
# Code starts here
import numpy as np
# Initialize stationary vector I
adj_mat = np.array([[0,0,0,0,0,0,1/3,0],
                   [1/2,0,1/2,1/3,0,0,0,0],
                   [1/2,0,0,0,0,0,0,0],
                   [0,1,0,0,0,0,0,0],
                  [0,0,1/2,1/3,0,0,1/3,0],
                   [0,0,0,1/3,1/3,0,0,1/2],
                   [0,0,0,0,1/3,0,0,1/2],
                   [0,0,0,0,1/3,1,1/3,0]])
print('adj_mat',adj_mat)

init_I=np.array([1,0,0,0,0,0,0,0])
print('init_I', init_I)
# Perform iterations for power method
for i in range(10):
    init_I = np.dot(adj_mat, init_I)
    init_I /= np.linalg.norm(init_I, 1)


print(init_I)
power_page = np.where(np.max(init_I) == init_I)[0][0] + 1
print(power_page)


# Code ends here


# --------------
# Code starts here

# New Adjancency matrix
# New Adjancency matrix
new_adj_mat = np.array([[0,0,0,0,0,0,0,0],
                   [1/2,0,1/2,1/3,0,0,0,0],
                  [1/2,0,0,0,0,0,0,0],
                   [0,1,0,0,0,0,0,0],
                   [0,0,1/2,1/3,0,0,1/2,0],
                   [0,0,0,1/3,1/3,0,0,1/2],
                   [0,0,0,0,1/3,0,0,1/2],
                   [0,0,0,0,1/3,1,1/2,0]])

# Initialize stationary vector I
new_init_I= np.array([1,0,0,0,0,0,0,0])
# Perform iterations for power method
for i in range(10):
    new_init_I=np.dot(new_adj_mat,new_init_I)
    new_init_I/=np.linalg.norm(new_init_I,1)
    print(new_init_I)




# Code ends here


# --------------
# Alpha value
alpha = 0.85

# Code starts here
import numpy as np
# Modified adjancency matrix
n=len(new_adj_mat)
I=np.ones(new_adj_mat.shape)
G=alpha*new_adj_mat+(I-alpha)*1/n*I
print('G',G)

# Initialize stationary vector I
final_init_I = np.array([1,0,0,0,0,0,0,0])
print('final_init_I',final_init_I)
# Perform iterations for power method
for i in range (1000):
    final_init_I=np.dot(G,final_init_I)
    final_init_I/=np.linalg.norm(final_init_I,1)
print(final_init_I)
# Code ends here


