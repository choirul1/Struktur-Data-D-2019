def stack ():
    s=[]
    return (s)
def push(s, data):
    s.append(data)
    
def pop(s):
    data=s.pop()
    return(data)

def peek(s):
    return(s[len(s)-1])

def isEmpty(s):
    return (s==[])
    
def size(s):
    return (len(s))

def oktal(desi):
    st=stack()
    des=desi
    while des>0:
        push(st,str(des%8))
        des=des//8
    hasil=''
    while not isEmpty(st):
        hasil=hasil+st.pop()
    return(hasil)
s = int(input("masukkan nilai desimal = "))
print("oktal = "+oktal(s))
