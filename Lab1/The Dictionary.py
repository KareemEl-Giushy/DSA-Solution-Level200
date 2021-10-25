def alpha_maker(names):
    dic = {}
    for n in names:
        dic[n[0]] = [n]
    
    return dic

if __name__ == '__main__':
    print(alpha_maker(['kareem', 'ahmed', 'fatma', 'hessan']))