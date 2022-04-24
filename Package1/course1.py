from student1 import Student1

class Course1:
    def __init__(self, c_num: int, c_name: str, capacity: int):
        if type(c_num) != int:
            raise TypeError ("course number must be int")
        if type(c_name) != str:
            raise TypeError("course name must be str")
        self.c_num = c_num
        self.c_name = c_name
        self.capacity = capacity
        self.details = {}
        self.l_students = []

    def __repr__(self):
        return f"course number: {self.c_num} course name: {self.c_name}  details: {self.details}" \
               f" students list:{self.l_students}  capacity: {self.capacity}"

    def AddStudent(self, student: Student1):
        if len(self.l_students) == self.capacity:
            return False
        else:
            self.l_students.append(student)
            return True

    def CalcFactor(self, percent: int, c_name ):
        self.c_name= c_name
        for i in self.l_students:
            i.calc_factor(self.c_name, percent)
            return i

    def del_student(self, student: Student1):
        if student not in self.l_students:
            print("student not found")
            return False
        else:
            self.l_students.remove(student)

    def laverages(self):
        l__averages = []
        for i in self.l_students:
            l__averages.append({i.name: i.Average()})
        return l__averages

    def weak_student(self):
        l__averages = []
        for i in self.l_students:
            l__averages.append(i.Average())
        lowests = []
        for i in range(len(l__averages)):
            if l__averages[i] == min(l__averages):
                lowests.append(i)
        return lowests

c1 = Course1(10, "science", 30)
c2 = Course1(11, "math", 25)
s1 = Student1(12, "nir", 21)
s3= Student1(11, "lion", 23)
s1.AddGrade("chemistry", 90)
s1.AddGrade("python", 80)
s2 = Student1(69, "gal", 22)
s2.AddGrade("chemistry", 75)
s2.AddGrade("python", 100)
s3.AddGrade("python", 75)
s3.AddGrade("chemistry", 100)

c1.del_student(s1)
c1.AddStudent(s1)
c1.AddStudent(s2)
c1.AddStudent(s3)
if __name__ == "__main__":
    print(c1.AddStudent(s1))
    print(c1.l_students)
    print(c1.CalcFactor(10, "python"))
    print(c1.l_students)
    print(c1.laverages())
    print(c1.weak_student())