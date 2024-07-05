#Queue  Implementation
''' Queue FIFO Structure  , Insertion from the last i.e.rea,  deletion  from the first i.e. front
Queue is bounded
'''
import sys
def Insert(que,front,rear):
    if rear==len(que)-1:
        print(" Queue is Overflow!!!")
        sys.exit(1)
    else:
        rear=rear+1
        data=input("Enter the information for the queue")
        que[rear]=data
    if  rear==0:
        front=0
    if rear==len(que)-1:
        print("\nNow Queue is Full")
        print("\nYou Can't Enter the more data")
    return que, front, rear

def Delete(que,front,rear):
    print("Call Function")
    if front<0:
        print("Under Flow")
        sys.exit()
    elif front>=0 and front<len(que)-1:
        print("Your Delete item is ",que[front])
        que.pop(front)
        front+=1
    elif front==len(que)-1:
        print("Your Delete item is ",que[front])
        print("Now Your Queue is Empty")
        que.pop(front)
        front=-1
    else:
        pass
    return que, front, rear

def show():
     print("Queue Item is")
     print("Front---> ",end= " ")
     for i  in range(front ,rear+1):
         print(Queue[i],end= "-")
     print("<---Rear ",end= " ")
     
#--------------------------------------------------#


#MAIN()
front =rear=-1 # stack is empty
size=3 # Size of stack
Queue=[0]*size # fixed the length of stack
while True: # Endless loop
    print("Press 1 for Insert")
    print("Press 2 for Show")
    print("Press 3 for Delete")
    
    ch=input("Enter the choice")
    if ch=='1':
        Queue,front,rear=Insert(Queue,front,rear) # function call with return value
    elif ch=='2': # function call with return value
        show()   
    elif ch=='3':
        Queue,front,rear=Delete(Queue,front,rear)
    else:        
        break

