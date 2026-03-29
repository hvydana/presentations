● Einsum Explained                                                                                                  
                                                                                                                    
  einsum (Einstein summation) is a way to express tensor operations using index notation.                           
                                                                                                                    
  Basic Rules:                                                                                                      
                                                                                                                    
  - Each letter represents a dimension/axis
  - Repeated letters on the left → sum over that dimension
  - Letters on the right → output dimensions

  ---
  Example 1: np.einsum('ci,cdij->di', diff, inv_cov)

  Shapes:
  - diff: shape [C, I] → [100, 3136] (C=channels, I=positions)
  - inv_cov: shape [C, D, I, J] → wait, actually it's [C, D, I] = [100, 100, 3136]

  Let me correct - the actual operation:

  # diff shape:    [B, C, I] = [1, 100, 3136]  (batch, channels, positions)
  # inv_cov shape: [C, D, I] = [100, 100, 3136]

  left = np.einsum('cdi,bdi->bci', inv_cov, diff)

  What it does: Matrix-vector multiply at each position

  For each position i (0 to 3135):
      left[:, :, i] = inv_cov[:, :, i] @ diff[:, :, i]

      # In math: left[b,c,i] = Σ_d inv_cov[c,d,i] * diff[b,d,i]

  Simple example:
  import numpy as np

  # 2 channels, 3 positions
  diff = np.array([[1, 2, 3],      # shape [2, 3]
                   [4, 5, 6]])

  # 2x2 matrix at each of 3 positions
  inv_cov = np.array([[[1, 0, 1],   # shape [2, 2, 3]
                       [0, 1, 0]],
                      [[1, 0, 1],
                       [0, 1, 0]]])

  # einsum: for each position, do matrix @ vector
  result = np.einsum('cdi,di->ci', inv_cov, diff)
  # Position 0: [[1,0],[1,0]] @ [1,4] = [1, 1]
  # Position 1: [[0,1],[0,1]] @ [2,5] = [5, 5]
  # Position 2: [[1,0],[1,0]] @ [3,6] = [3, 3]

  ---
  Example 2: np.einsum('di,di->i', diff, left)

  This is element-wise multiply then sum over d:

  # diff shape: [D, I] = [100, 3136]
  # left shape: [D, I] = [100, 3136]

  dist_sq = np.einsum('di,di->i', diff, left)
  # Output shape: [I] = [3136]

  # What it does:
  # dist_sq[i] = Σ_d diff[d,i] * left[d,i]
  # This is a dot product at each position!

  Simple example:
  diff = np.array([[1, 2],    # shape [2, 2] (2 channels, 2 positions)
                   [3, 4]])

  left = np.array([[5, 6],
                   [7, 8]])

  result = np.einsum('di,di->i', diff, left)
  # Position 0: 1*5 + 3*7 = 5 + 21 = 26
  # Position 1: 2*6 + 4*8 = 12 + 32 = 44
  # Result: [26, 44]

  ---
  The Full Mahalanobis Formula:

  # Mahalanobis: d = sqrt((x - μ)ᵀ Σ⁻¹ (x - μ))

  diff = embedding - mean           # (x - μ)
  left = einsum(inv_cov, diff)      # Σ⁻¹ @ (x - μ)
  dist_sq = einsum(diff, left)      # (x - μ)ᵀ @ [Σ⁻¹ @ (x - μ)]
  dist = sqrt(dist_sq)              # final distance

  Without einsum (slow loop):
  for i in range(3136):
      d = diff[:, i]                    # [100]
      S_inv = inv_cov[:, :, i]          # [100, 100]
      dist[i] = sqrt(d.T @ S_inv @ d)   # scalar

  With einsum (fast, vectorized):
  # All 3136 positions computed in ONE operation!
  left = np.einsum('cdi,bdi->bci', inv_cov, diff)
  dist_sq = np.einsum('bci,bci->bi', diff, left)
  dist = np.sqrt(dist_sq)