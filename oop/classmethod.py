

class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #instance method
    def get_info(self):
        return f'{self.name} {self.gpa} '
    @classmethod
    def get_count(cls):
        return f'Total # of students: {cls.count}'
    
    @classmethod # truy cap truc tiep vao data cua class de su dung
    def get_ave_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f'{cls.total_gpa / cls.count}'
    

student1 = Student('bbao', 1)
student2 = Student('bu', 10)
student3 = Student('cu', 20)



print(Student.get_count())
        
print(Student.get_ave_gpa())


