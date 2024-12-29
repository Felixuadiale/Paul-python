import os
print("Checking if my_file exist or not..........")
if os.path.exists("C:/Users/HP/Downloads/python programmes/hellonew.txt"):
  os.remove("C:/Users/HP/Downloads/python programmes/hellonew.txt")
else:
  print("The file does not exist")
os.rmdir("C:/Users/HP/Downloads/python programmes/myfolder")