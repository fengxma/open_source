"""
a recursive algorithm to yield all subsets of a set
"""

def subsets(s):
    if not s:
        yield ()
    else:
        for e in subsets(s[1:]):
            yield s[:1] + e
            yield e

for s in subsets((1,2,3)):
    print(s)
