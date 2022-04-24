
class HardDisk:
    def __init__(self, occupied_space=0, n_files=0):
        self.total_space= 100
        self.occupied_space = occupied_space
        self.n_files = n_files

    def __str__(self):
        return f'{self.total_space}  {self.occupied_space} {self.n_files}'

    def free_space(self):
        self.free_space = self.total_space - self.occupied_space
        return f'{self.free_space}'
    def addfile(self):
        self.new_file=int(input("add file:"))
        if self.occupied_space+self.new_file <= 100:
            self.occupied_space += self.new_file
            self.n_files+=1
        else:
            print("not enough space available")
        return f'{self.total_space}  {self.occupied_space} {self.n_files}'
    def delfile(self):
        self.old_file=int(input("delete file:"))
        if self.occupied_space-self.old_file >= 0:
            self.occupied_space -= self.old_file
        else:
            self.occupied_space=0
            self.n_files-=1
        return f'{self.total_space}  {self.occupied_space} {self.n_files}'


disk1=HardDisk(54, 7)
print(disk1)
print(disk1.free_space())
print(disk1.addfile())
print(disk1.delfile())

