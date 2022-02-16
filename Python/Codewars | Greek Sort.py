def greek_comparator(lhs, rhs):
    greek_alphabet = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega']
    if lhs == rhs:
        res = 0
    elif greek_alphabet.index(lhs) < greek_alphabet.index(rhs):
        res = -1
    else:
        res = 1
    return res
