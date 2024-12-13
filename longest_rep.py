def longest_repetition(chars):
    """
    accept a string input
    sort the string
    split it into a list element
    remove duplicates
    store it in a dictionary with the count set to 0
    iterate through the previous list element and count the occurences
    """
    st = list(chars)
    # print(st)
    st.sort()
    listElem = []
    # dictionary data structure to store occurences of characters
    myDict = {}
    h = 0
    # establish a tuple data structure
    t = ()
    for i in st:
    # check if value not already in list
        if i not in listElem:
            listElem.append(i)
    
    for i in listElem:
        myDict[i] = st.count(i)

    if len(myDict) == 0:
        t = ("",0)

    for i in myDict:
        if myDict[i] > h:
            t = (i, myDict[i])
    
    return t

t = longest_repetition("bbbaaabaaaa")
print(t)