def alpha_maker(names):
    dic = {}
    for n in names:
        if n[0] not in names.keys():
            dic[n[0]] = [n]
        else:
            dic[n[0]].append(n)
    return dic

if __name__ == '__main__':
    print(alpha_maker(['kareem', 'ahmed', 'fatma', 'hessan']))