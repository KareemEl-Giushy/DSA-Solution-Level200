def locator(word, char):
    lst = []
    for i, l in enumerate(word):
        if l == char:
            lst.append(i)
    return lst       

if __name__ == '__main__':
    print("kareem".index('e'))
    print(locator('kareemakakjfkaaa', 'a'))