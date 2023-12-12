def push():
    doc_id=int(input('Enter the doctor id:'))
    doc_name=input("Enter the name of the doctor")
    mob=int(input('Enter the mobile number of the doctor'))
    special=input("enter the specialization")
    if special == 'ent':
        stack.append([doc_id,doc_name])
def pop():
    if stack == []:
        print('stack is empty')
    else:
        print('the deleted doctor detail is:',stack.pop())
def display():
    if stack == []:
        print('stack is empty')
    else:
        top=len(stack)-1
        print(top)
        for i in range(top,-1,-1):
            print(stack[i])
stack=[]
ch='y'
print('performing stack operations using list\n')
while ch == 'y' or ch == 'Y':
    print()
    print('1.Push')
    print('2.Pop')
    print('3.Display')
    opt=int(input('Enter your choice'))
    if opt == 1:
        push()
    elif opt == 2:
        pop()
    elif opt ==3:
        display()
    else:
        print('Invaild choice, try again!!!')
    ch=input('\n Do you want to perform another operation(Y/N)')