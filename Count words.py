with open('C:/Users/HP/Downloads/python programmes/hello.txt','r') as file:
    data=file.readlines()
    print("Words in this are......")
    for line in data:
        word=line.split()
        print(word)
file.close()