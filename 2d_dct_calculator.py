import numpy as np

# -----------------------------
# USER INPUTS
# -----------------------------
N = int(input("Enter image size N (e.g., 64): "))
print(f"Image will be {N}x{N} pixels")

# White square
x_start = int(input(f"Enter top-left row of white square (0-{N-1}): "))
x_end   = int(input(f"Enter bottom-right row of white square (1-{N}): "))
y_start = int(input(f"Enter top-left column of white square (0-{N-1}): "))
y_end   = int(input(f"Enter bottom-right column of white square (1-{N}): "))

# DCT coefficient
u = int(input(f"Enter DCT coefficient row index u (0-{N-1}): "))
v = int(input(f"Enter DCT coefficient column index v (0-{N-1}): "))

# -----------------------------
# CREATE IMAGE
# -----------------------------
test_image = np.zeros((N, N), dtype=np.uint8)
test_image[x_start:x_end, y_start:y_end] = 255

# -----------------------------
# ALPHA FUNCTION
# -----------------------------
def alpha(k, N):
    return np.sqrt(1/N) if k == 0 else np.sqrt(2/N)

alpha_u = alpha(u, N)
alpha_v = alpha(v, N)

# -----------------------------
# MANUAL 2D DCT CALCULATION
# -----------------------------
S = 0.0
for x in range(x_start, x_end):
    for y in range(y_start, y_end):
        S += test_image[x, y] * np.cos(np.pi * (2*x + 1) * u / (2*N)) * np.cos(np.pi * (2*y + 1) * v / (2*N))

# Multiply by alpha factors
F_uv = alpha_u * alpha_v * S

print("\nManual calculation of DCT coefficient F({},{})".format(u, v))
print(F_uv)
