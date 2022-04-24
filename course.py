class Course:
    def __init__(self, c_number: int,  c_name: str, students: int, capacity: int ):
        self.c_number = c_number
        self.c_name = c_name
        self.students = students
        self.capacity = capacity

    def __str__(self):
        return f'{self.c_number} \n{self.c_name} \n{self.students} \n{self.capacity}'

    def remaining(self):
        self.available=self.capacity-self.students
        return self.available

    def register(self):
        self.applying= int(input("applying students:"))
        if self.applying<self.available:
            self.students+=self.applying
        else:
            print("not enough available spots!")
        return self.students
c_num=int(input("enter course number:"))
name=input("enter name:")
students=int(input("how many students?"))
capacity=int(input("limit:"))
chess=Course(c_num, name, students, capacity)
print(chess)
print(chess.remaining())
print(chess.register())
print(chess)