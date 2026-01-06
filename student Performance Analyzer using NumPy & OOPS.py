import numpy as num
print("The student detatils are:\n")
class student:
    def __init__(self):
        self.names=[]
        self.id=[]
        self.age=[]
        self.department=[]
        self.std=int(input("enter your no of inputs of students:"))
        for i in range(self.std):
            self.names.append(str(input("enter the name of student:")))
            self.id.append(int(input("enter the id of student:")))
            self.age.append(int(input("enter the age of student:")))
            self.department.append(str(input("enter the department of student:")))
            print("\n")

    def subject(self):        
        self.mrk=int(input("enter the no of subject:"))
        self.__subject_mark = num.random.randint(0,100,size=(self.std,self.mrk))
        print(self.__subject_mark)
        print(self.__subject_mark.shape)
        print(self.__subject_mark.ndim)

    def mark(self):
        self.total =num.sum(self.__subject_mark,axis=1)
        self.average =num.average(self.__subject_mark,axis=1)
        print("they total mark:",num.sum(self.__subject_mark,axis=1))
        print("they average mark ",num.average(self.__subject_mark,axis=1))
        print("they maxium mark ",num.max(num.sum(self.__subject_mark,axis=1)))
        print("they minumn mark",num.min(num.sum(self.__subject_mark,axis=1)))
        print("\n")

    def analyse(self):
        ana = num.average(self.__subject_mark,axis=1)
        print("The higest mark is:",num.max(ana))
        print("The lowest mark is:",num.min(ana))
        self.category = num.where(ana>=75,"excellent",num.where(ana>=50,"average","poor"))
        print(self.category)
        print("\n")
        
    def report(self):
        print("The student report is:")
        print("***************************************************")
        for i in range(self.std):
            print("The name of student:",self.names[i])
            print("The id of student:",self.id[i])
            print("The department of student:",self.department[i])
            print("The age of student:",self.age[i])
            print("they total mark:",self.total[i])
            print("they average mark ",self.average[i])
            print("they category of student:",self.category[i])
            print("\n")


#calling the class
Student =student()
Student.subject()
Student.mark()
Student.analyse()
Student.report()



