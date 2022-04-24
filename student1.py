class Student1:
    def __init__(self, id: int, name: str, age: int):
        self.id = id
        self.name = name
        self.age = age
        self.grades_sheet = {}
        if type(id) != int or type(name) != str or type(age) != int or age > 120 or age < 0:
            raise TypeError ("invalid arguments, try again!")

    def AddGrade(self, course: str, grade: int):
        if type(course) != str:
            raise TypeError ("course name must be string!")
        if type(grade) != int:
            raise TypeError ("grade must be int!")
        if grade > 100:
            print("grade cannot be over 100!, 100 is written instead!")
            grade = 100
        if grade < 0:
            print("grade cannot be less than 0!, 0 is written instead!")
            grade = 0
        self.grades_sheet.update({course: grade})

    def __repr__(self):
        return f'id: {self.id} name: {self.name} age: {self.age} grades: {self.grades_sheet}'

    def calc_factor(self, course: str, factor: int):
        self.course = course
        self.factor = factor
        if type(course) != str:
            raise TypeError("course must be string")
        if factor < -100 or type(factor) != int:
            raise TypeError("factor must be a whole number over -100")
        self.grades_sheet[self.course] += (self.grades_sheet[self.course] * self.factor) / 100
        if self.grades_sheet[self.course] > 100:
            self.grades_sheet[self.course] = 100
        return f'grades: {self.grades_sheet}'

    def Average(self):
        return sum(self.grades_sheet.values())/len(self.grades_sheet)

    def __eq__(self, other):
        if self.id == other.id:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False


st1=Student1(12, "nir", 21)
st1.AddGrade("chemistry", 90)
st1.AddGrade("python", 80)
if __name__ == "__main__":
    print(st1)
    print(st1)
    print(st1.calc_factor("chemistry", 10))
    print(st1.Average())
st1=Student1(12, "nir", 21)
st1.AddGrade("chemistry", 90)
st1.AddGrade("python", 80)

