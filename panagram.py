import string

def is_pangram(st):
    alph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", 
            "P", "Q", "R", "S", "T", "U","V","W","X","Y","Z"]
    
    # sent.strip()
    st = st.strip().translate(st.maketrans('', '', string.punctuation))
    st = st.lower().strip().replace(" ","")
    st = ''.join([i for i in st if not i.isdigit()])

    t = ""
    for i in st:
        if i in t:
            pass
        else:
            t = t + i

    if len(t) == len(alph):
        return True
    else:
        return False
    

output = is_pangram("oZVpK.y\nF['FDXURhHKxdBTnaiGMu oCw5H|w8 ,  S[F@LmqJ 1G jpa#Ee@F")

print(output)