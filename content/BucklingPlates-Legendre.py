import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

# --- 1. Global Style Settings ---
# This ensures the font is Times New Roman and the math matches the style
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]
plt.rcParams["mathtext.fontset"] = "cm"  # Computer Modern for math (LaTeX-like)

# --- 2. Define the Domain ---
xi = np.linspace(-1, 1, 400)

# --- 3. Helper Functions for Higher Order Terms ---
def double_factorial(n):
    """Calculates n!!"""
    if n < 0: return 1
    result = 1
    for k in range(n, 0, -2):
        result *= k
    return result

def s_high_order(i, xi):
    """Calculates the shape function for i > 4 based on the summation formula."""
    total = np.zeros_like(xi)
    limit = int((i - 1) // 2)
    
    for p in range(limit + 1):
        # Calculate terms based on the user's provided equation
        term_num = ((-1)**p) * double_factorial(2*i - 2*p - 7)
        term_den = (2**p) * factorial(p) * factorial(i - 2*p - 1)
        term_pow = xi**(i - 2*p - 1)
        
        total += (term_num / term_den) * term_pow
        
    return total

# --- 4. Plot Figure 1: Standard Hermitian (i=1 to 4) ---
s1 = (1/2) - (3/4)*xi + (1/4)*xi**3
s2 = (1/8) - (1/8)*xi - (1/8)*xi**2 + (1/8)*xi**3
s3 = (1/2) + (3/4)*xi - (1/4)*xi**3
s4 = -(1/8) - (1/8)*xi + (1/8)*xi**2 + (1/8)*xi**3

plt.figure(figsize=(10, 6))

# Plotting with distinct line styles
plt.plot(xi, s1, color='black', linestyle='-', label=r'$s_{i=1}(\xi)$', linewidth=2.5)
plt.plot(xi, s2, color='black', linestyle='--', label=r'$s_{i=2}(\xi)$', linewidth=2.5)
plt.plot(xi, s3, color='black', linestyle='-.', label=r'$s_{i=3}(\xi)$', linewidth=2.5)
plt.plot(xi, s4, color='black', linestyle=':', label=r'$s_{i=4}(\xi)$', linewidth=2.5)

# Styling with large fonts
plt.xlabel(r'$\xi$', fontsize=24)
plt.ylabel(r'$s(\xi)$', fontsize=24)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim([-1, 1])

# Save or Show
plt.savefig('BucklingPlates-Legendre-BC.pdf', bbox_inches='tight')
#plt.show()


# --- 5. Plot Figure 2: Higher Order Bubble Functions (i=5 to 8) ---
s5 = s_high_order(5, xi)
s6 = s_high_order(6, xi)
s7 = s_high_order(7, xi)
s8 = s_high_order(8, xi)

plt.figure(figsize=(10, 6))

# Definitions for the loop
functions = [s5, s6, s7, s8]
styles = [
    ('-', r'$s_{i=5}(\xi)$'),
    ('--', r'$s_{i=6}(\xi)$'),
    ('-.', r'$s_{i=7}(\xi)$'),
    (':',  r'$s_{i=8}(\xi)$')
]

for func, (ls, label) in zip(functions, styles):
    plt.plot(xi, func, color='black', linestyle=ls, label=label, linewidth=2.5)

# Styling with large fonts
plt.xlabel(r'$\xi$', fontsize=24)
plt.ylabel(r'$s(\xi)$', fontsize=24)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim([-1, 1])

# Save or Show
# plt.savefig('high_order_shape_functions.png', bbox_inches='tight')
plt.savefig('BucklingPlates-Legendre-inner.pdf', bbox_inches='tight')
#plt.show()