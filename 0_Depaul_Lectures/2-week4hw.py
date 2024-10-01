def vowelIndex(str):
    for i in range(len(str)):
        if str[i] in 'aeiouAEIOU':
            return i
    
    return -1

if __name__ == "__main__":
    import doctest 
    print(doctest.testfile("2-week4hwTEST.py"))

