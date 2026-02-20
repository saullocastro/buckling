import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

# --- 1. Global Style Settings ---
# This ensures the font is Times New Roman and the math matches the style
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]
plt.rcParams["mathtext.fontset"] = "cm"  # Computer Modern for math (LaTeX-like)

# --- 2. Define the Domain ---
chi = np.linspace(-1, 1, 400)

# --- 3. Helper Functions for Higher Order Terms ---
def double_factorial(n):
    """Calculates n!!"""
    if n < 0: return 1
    result = 1
    for k in range(n, 0, -2):
        result *= k
    return result

def s_high_order(i, chi):
    """Calculates the shape function for i > 4 based on the summation formula."""
    total = np.zeros_like(chi)
    limit = int((i - 1) // 2)
    
    for p in range(limit + 1):
        # Calculate terms based on the user's provided equation
        term_num = ((-1)**p) * double_factorial(2*i - 2*p - 7)
        term_den = (2**p) * factorial(p) * factorial(i - 2*p - 1)
        term_pow = chi**(i - 2*p - 1)
        
        total += (term_num / term_den) * term_pow
        
    return total

# --- 4. Plot Figure 1: Standard Hermitian (i=1 to 4) ---
p1 = (1/2) - (3/4)*chi + (1/4)*chi**3
p2 = (1/8) - (1/8)*chi - (1/8)*chi**2 + (1/8)*chi**3
p3 = (1/2) + (3/4)*chi - (1/4)*chi**3
p4 = -(1/8) - (1/8)*chi + (1/8)*chi**2 + (1/8)*chi**3

plt.figure(figsize=(10, 6))

# Plotting with distinct line styles
plt.plot(chi, p1, color='black', linestyle='-', label=r'$P_{i=1}(\chi)$', linewidth=2.5)
plt.plot(chi, p2, color='black', linestyle='--', label=r'$P_{i=2}(\chi)$', linewidth=2.5)
plt.plot(chi, p3, color='black', linestyle='-.', label=r'$P_{i=3}(\chi)$', linewidth=2.5)
plt.plot(chi, p4, color='black', linestyle=':', label=r'$P_{i=4}(\chi)$', linewidth=2.5)

# Styling with large fonts
plt.xlabel(r'$\chi$', fontsize=24)
plt.ylabel(r'$P(\chi)$', fontsize=24)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim([-1, 1])

# Save or Show
plt.savefig('BucklingPlates-Legendre-BC.svg', bbox_inches='tight')
plt.savefig('BucklingPlates-Legendre-BC.pdf', bbox_inches='tight')
#plt.show()


# --- 5. Plot Figure 2: Higher Order Bubble Functions (i=5 to 8) ---
p5 = s_high_order(5, chi)
p6 = s_high_order(6, chi)
p7 = s_high_order(7, chi)
p8 = s_high_order(8, chi)

plt.figure(figsize=(10, 6))

# Definitions for the loop
functions = [p5, p6, p7, p8]
styles = [
    ('-', r'$P_{i=5}(\chi)$'),
    ('--', r'$P_{i=6}(\chi)$'),
    ('-.', r'$P_{i=7}(\chi)$'),
    (':',  r'$P_{i=8}(\chi)$')
]

for func, (ls, label) in zip(functions, styles):
    plt.plot(chi, func, color='black', linestyle=ls, label=label, linewidth=2.5)

# Styling with large fonts
plt.xlabel(r'$\chi$', fontsize=24)
plt.ylabel(r'$P(\chi)$', fontsize=24)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim([-1, 1])

# Save or Show
plt.savefig('BucklingPlates-Legendre-inner.svg', bbox_inches='tight')
plt.savefig('BucklingPlates-Legendre-inner.pdf', bbox_inches='tight')
#plt.show()