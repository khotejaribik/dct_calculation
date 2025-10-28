import numpy as np

# Image size
N = 64

# Create 64x64 black image
test_image = np.zeros((N, N), dtype=np.uint8)

# Add 20x20 white square
test_image[20:40, 20:40] = 255

# DCT indices we want
u = 1
v = 1

# Compute alpha(u) and alpha(v)
def alpha(k, N):
    return np.sqrt(1/N) if k == 0 else np.sqrt(2/N)

alpha_u = alpha(u, N)
alpha_v = alpha(v, N)

# Calculate the sum S
S = 0.0
for x in range(20, 40):      # rows of white square
    for y in range(20, 40):  # columns of white square
        S += test_image[x, y] * np.cos(np.pi * (2*x + 1) * u / (2*N)) * np.cos(np.pi * (2*y + 1) * v / (2*N))

# Multiply by alpha factors
F_uv = alpha_u * alpha_v * S

print("Manual calculation of F(1,1) DCT coefficient:")
print(F_uv)
