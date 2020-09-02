from dataclasses import dataclass

@dataclass
class Student:
    #the fields in dataclass class is explicitly typed from the start rather than implicitly typed, which could later cause errors
    #I prefer this to the __init__ way because it won't accept data types that the program isn't looking for
    name: str
    s_id: str
    gpa: float


    def __str__(self):
        return f'Student name: {self.name}, ID: {self.s_id}, GPA: {self.gpa}'

def main():
    ben = Student('Ben', 'abcdef', 3.9)
    jordan = Student('Jordan', 'bcdefg', 3.5)
    print(ben,'\n', jordan)

main()