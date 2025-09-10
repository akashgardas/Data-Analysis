class School:
    def __init__(self):
        self.students = []
    
    def add_student(self, rno, name, marks):
        self.students.append((rno, name, marks))
    
    def get_highest_scored_student(self):
        top_std = max(self.students, key=lambda std: std[2])
        return top_std

    def display(self):
        print('-'*30)
        print('STUDENTS')
        print('-'*30)
        print('Roll No          Name        Marks')
        for std in self.students:
            print(f'{std[0]}        {std[1]}        {std[2]}')
        
        print('-'*30)
        print(f'Highest marks student: {self.get_highest_scored_student()[1]}')
        print('-'*30)
        
        print(f'Students with marks above 75')
        print('-'*30)
        print('Roll No          Name        Marks')
        for std in self.students:
            if std[2] >= 75:
                print(f'{std[0]}        {std[1]}        {std[2]}')

school = School()
school.add_student(1, 'John', 78)
school.add_student(2, 'Emily', 95)
school.add_student(3, 'David', 88)
school.add_student(4, 'Sophia', 72)
school.add_student(5, 'Michael', 65)
school.add_student(6, 'Olivia', 100)
school.add_student(7, 'James', 91)
school.add_student(8, 'Isabella', 79)
school.add_student(9, 'Daniel', 83)
school.add_student(10, 'Mia', 68)
school.add_student(11, 'William', 99)
school.display()