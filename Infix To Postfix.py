class StackClass:

    def __init__(self, itemlist=[]):
        self.items = itemlist

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False                   
                                                    
    def peek(self):                     
        return self.items[-1:][0]        
                                          
    def pop(self):
        return self.items.pop()             
                                            
    def push(self, item):
        self.items.append(item)              
        return 0                         
                                         
def toposfix(bil):             
                                          
    s=StackClass()                                 
    outdata=[]                                 
    operan={}
    operan['(']=1
    operan['+']=2
    operan['-']=2
    operan['/']=3                                
    operan['*']=3
    opdata=['/','*','+','-']

    tokenlst=bil.split()
    for token in tokenlst:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            outdata.append(token)

        elif token =='(':
            s.push(token)

        elif token ==')':
            topToken=s.pop()
            while topToken != '(':
                outdata.append(topToken)
                topToken=s.pop()
        else:
            while (not s.isEmpty()) and (operan[s.peek()] >= operan[token]):
                outdata.append(s.pop())
            s.push(token)
            print (s.peek())

    while not s.isEmpty():
        opToken=s.pop()
        outdata.append(opToken)
    return outdata

b=input("masukkan operasi infix,contoh A * B + C * D :")
print("infix yang anda masukkan : "+b)
print ("postfix:"+str(toposfix(b)))
