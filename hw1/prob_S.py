def prob_S(S, D):
    ret = []
    counter = defaultdict(int)
    for d in D:
        counter[d] += 1
    tot = len(D)
    for s in S:
        prob = counter[s] / tot
        ret.append(prob)
    return ret