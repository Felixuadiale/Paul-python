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
print("Welcome to Phonebook app")
pb=initial_phonebook()
print(pb)