def stack():
    s=[]
    return(s)

def push(s,data):
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

def biner(desi):
    st=stack()
    des=desi
    while des>0:
        push(st,str(des%2))
        des=des//2
    hasil=''
    while not isEmpty(st):
        if len(st)==1:
            hasil=hasil+st.pop()
        else:
            hasil=hasil+st.pop()+"."
    return(hasil)

s=int(input("masukkan nilai desimal:"))
print("biner:"+biner(s))

