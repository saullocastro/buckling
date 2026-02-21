from sympy import var, factorial, factorial2, sympify, diff
from sympy.printing import pycode

NMAX = 200

xi = var('xi')

u = list(map(sympify, ['1./2. - 3./4.*xi + 1./4.*xi**3',
                       '1./8. - 1./8.*xi - 1./8.*xi**2 + 1./8.*xi**3',
                       '1./2. + 3./4.*xi - 1./4.*xi**3',
                       '-1./8. - 1./8.*xi + 1./8.*xi**2 + 1./8.*xi**3']))

for r in range(5, NMAX+1):
    utmp = []
    for n in range(0, r//2+1):
        den = 2**n*factorial(n)*factorial(r-2*n-1)
        utmp.append((-1)**n*factorial2(2*r - 2*n - 7)/den * xi**(r-2*n-1)/1.)
    u.append(sum(utmp))

consts = {0:'d1t', 1:'d1r', 2:'d2t', 3:'d2r'}
with open('./legendre_functions.py', 'w') as f:
    f.write("# Modified Legendre polynomial's hierarchical functions\n")
    f.write("# - d1t and d2t control the displacements at extremity along each\n")
    f.write("#   natural coordinate\n")
    f.write("# - d1r and d2r control the rotations at extremity along each\n")
    f.write("#   natural coordinate\n")
    f.write('\n')
    f.write('# Maximum number of terms: {0}\n\n'.format(len(u)))
    f.write('import numpy as np\n\n\n')
    f.write('NMAX = %d\n\n\n' % NMAX)
    f.write('def f(xi, i, d1t, d1r, d2t, d2r):\n')
    f.write('    assert i <= (NMAX-1), "Current implementation requires i <= %d"\n' % (NMAX-1))
    for i in range(len(u)):
        if i == 0:
            f.write('    if i == %d:\n' % i)
        else:
            f.write('    elif i == %d:\n' % i)
        const = consts.get(i)
        if const is None:
            f.write('        return %s\n' % (pycode(u[i])))
        else:
            f.write('        return %s*(%s)\n' % (const, pycode(u[i])))
    f.write('\n\n')
    f.write('def fxi(xi, i, d1t, d1r, d2t, d2r):\n')
    f.write('    assert i <= (NMAX-1), "Current implementation requires i <= %d"\n' % (NMAX-1))
    for i in range(len(u)):
        if i == 0:
            f.write('    if i == %d:\n' % i)
        else:
            f.write('    elif i == %d:\n' % i)
        const = consts.get(i)
        if const is None:
            f.write('        return %s\n' % pycode(diff(u[i], xi)))
        else:
            f.write('        return %s*(%s)\n' % (const, pycode(diff(u[i], xi))))
    f.write('\n\n')
    f.write('def fxixi(xi, i, d1t, d1r, d2t, d2r):\n')
    f.write('    assert i <= (NMAX-1), "Current implementation requires i <= %d"\n' % (NMAX-1))
    for i in range(len(u)):
        if i == 0:
            f.write('    if i == %d:\n' % i)
        else:
            f.write('    elif i == %d:\n' % i)
        const = consts.get(i)
        if const is None:
            f.write('        return %s\n' % pycode(diff(u[i], xi, xi)))
        else:
            f.write('        return %s*(%s)\n' % (const, pycode(diff(u[i], xi, xi))))

    f.write('\n\n')
    f.write('def vecf(n, xi, d1t, d1r, d2t, d2r):\n')
    f.write('    assert n <= NMAX, "Current implementation requires n <= %d"\n' % NMAX)
    f.write('    out = np.zeros(n)\n')
    for i in range(len(u)):
        const = consts.get(i)
        if const is None:
            f.write('    out[%d] = %s\n' % (i, pycode(u[i])))
        else:
            f.write('    out[%d] = %s*(%s)\n' % (i, const, pycode(u[i])))
        f.write('    if n == %d:\n' % (i+1))
        f.write('        return out\n')
    f.write('\n\n')
    f.write('def vecfxi(n, xi, d1t, d1r, d2t, d2r):\n')
    f.write('    assert n <= NMAX, "Current implementation requires n <= %d"\n' % NMAX)
    f.write('    out = np.zeros(n)\n')
    for i in range(len(u)):
        const = consts.get(i)
        if const is None:
            f.write('    out[%d] = %s\n' % (i, pycode(diff(u[i], xi))))
        else:
            f.write('    out[%d] = %s*(%s)\n' % (i, const, pycode(diff(u[i], xi))))
        f.write('    if n == %d:\n' % (i+1))
        f.write('        return out\n')
    f.write('\n\n')
    f.write('def vecfxixi(n, xi, d1t, d1r, d2t, d2r):\n')
    f.write('    assert n <= NMAX, "Current implementation requires n <= %d"\n' % NMAX)
    f.write('    out = np.zeros(n)\n')
    for i in range(len(u)):
        const = consts.get(i)
        if const is None:
            f.write('    out[%d] = %s\n' % (i, pycode(diff(u[i], xi, xi))))
        else:
            f.write('    out[%d] = %s*(%s)\n' % (i, const, pycode(diff(u[i], xi, xi))))
        f.write('    if n == %d:\n' % (i+1))
        f.write('        return out\n')
