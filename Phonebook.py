import sys
def initial_phonebook():
    row,cols=int(input('Enter initial number of contact')),2
    phonebook=[]
    print(phonebook)
    for i in range(row):
        temp=[]
        for j in range(cols):
            if j==0:
                temp.append(input("Enter name*: "))
                if temp[j]==''or temp[j]=='':
                    sys.exit("Name is a mandatory field.Process exiting due to blank field...")
            if j==1:
                temp.append(int(input("Enter Number*: ")))
        phonebook.append(temp)
    print(phonebook)
    return phonebook
def add_contact(pb):
    dip=[]
    for i in range(len(pb[0])):
        if i==0:
            dip.append(str(input("Enter name: ")))
        if i==1:
            dip.append(int(input("Enter number: ")))
        pb.append(dip)
        return pb
print("Welcome to Phonebook app")
pb=initial_phonebook()
print(pb)
add=input(' Do you want to add a new contact(y/n)')
if add=='y':
    pb=add_contact(pb)
    print(pb)