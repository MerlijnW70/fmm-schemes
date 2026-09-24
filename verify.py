import json
import sys
from collections import defaultdict
from fractions import Fraction


def coeff(x):
    if isinstance(x, int):
        return Fraction(x)
    return Fraction(str(x).strip())


def check(path):
    d = json.load(open(path))
    n1, n2, n3 = d["n"]
    u = [[coeff(x) for x in row] for row in d["u"]]
    v = [[coeff(x) for x in row] for row in d["v"]]
    w = [[coeff(x) for x in row] for row in d["w"]]
    z2 = bool(d.get("z2", False))
    m = len(u)
    if not (len(v) == m and len(w) == m and d.get("m", m) == m):
        return False, "rank mismatch", m
    if any(len(r) != n1 * n2 for r in u) or any(len(r) != n2 * n3 for r in v) or any(len(r) != n3 * n1 for r in w):
        return False, "row length mismatch", m
    t = defaultdict(Fraction)
    for r in range(m):
        us = [(a, x) for a, x in enumerate(u[r]) if x]
        vs = [(b, y) for b, y in enumerate(v[r]) if y]
        ws = [(c, z) for c, z in enumerate(w[r]) if z]
        for a, x in us:
            for b, y in vs:
                xy = x * y
                for c, z in ws:
                    t[(a, b, c)] += xy * z
    want = set()
    for i in range(n1):
        for j in range(n2):
            for k in range(n3):
                want.add((i * n2 + j, j * n3 + k, k * n1 + i))
    for key in set(t) | want:
        target = Fraction(1) if key in want else Fraction(0)
        diff = t.get(key, Fraction(0)) - target
        if z2:
            if diff.denominator != 1 or diff.numerator % 2 != 0:
                return False, "fails mod 2 at %s" % (key,), m
        elif diff != 0:
            return False, "fails at %s: %s" % (key, t.get(key, 0)), m
    return True, "ok", m


def main(paths):
    bad = 0
    for p in paths:
        ok, why, m = check(p)
        print("%s rank %d %s %s" % ("OK  " if ok else "FAIL", m, why, p))
        bad += 0 if ok else 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
