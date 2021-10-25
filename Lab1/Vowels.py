v = ['a', 'e', 'i', 'o', 'u']
def vowels(word):
    s = ''
    for l in word:
        if not l.lower() in v:
            s += l

    return s

if __name__ == '__main__':
    print(vowels('kAreem'))