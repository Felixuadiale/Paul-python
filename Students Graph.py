import matplotlib.pyplot as plt
students_names=["sanjay","Rahul","Karan","Wasim","Ramesh","Ajay",'Sartaj','priya']
students_marks=[35,50,20,45,25,40,25,40]
marks_perc=[]
for x in students_marks:
    res=(x/50)*100
    marks_perc.append(res)
print(marks_perc)
def marks_line_chart():
    plt.plot(students_names,students_marks)
    plt.title("Students Marks Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students Marks")
    plt.show()
marks_line_chart()
def percentage_bar_chart():
    plt.bar(students_names,marks_perc)
    plt.title("Students Percentage Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students percentage")
    plt.show()
percentage_bar_chart()