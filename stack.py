#Stack Implementation
import sys
def Push(stk,Top): # Top=-1  stk=[0,0,0]
    if Top==len(stk)-1:
        print ("Over Flow !!")
        sys.exit(1)
    else:
        Top=Top+1
        data=input("Enter the Value for Stack") # 10
        stk[Top]=data #  stk[10,0,0]
    if Top==len(stk)-1:
        print("Stack Full !")
    return stk,Top

def Pop(stk, Top):
    if Top<0: # Stack already empty
        print("Under Flow")
        sys.exit(1)
    else:  
        print("your deleted element is ",stk[Top]) # To show the deleted item
        #stk[Top]=0 #  replace value with 0
        stk.pop(Top)
        Top=Top-1
    if Top<0:
        print("\nNow Stack is Empty! You can't delete more item")
    return stk,Top

def show(stk,Top):
    print("Stack Value")
    for i in range(0,Top+1):
        print(stk[i], " ",end= " ")
    print("<---Top Element")

#MAIN()
Top=-1 # stack is empty
size=3 # Size of stack
stack=[0]*size # fixed the length of stack
while True: # Endless loop
    print("Press 1 for Push")
    print("Press 2 for Show")
    print("Press 3 for Pop")
    
    ch=input("Enter the choice")
    if ch=='1':
        stack,Top=Push(stack, Top) # function call with return value
    elif ch=='2': # function call with return value
        show(stack,Top)   
    elif ch=='3':
        stack,Top=Pop(stack, Top)
    else:        
        break

