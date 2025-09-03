class Student:
    def __init__(self, name, id, marks):
        self.name = name
        self.id = id
        self.marks = marks

    def printDetails(self):
        print('='*30)
        print('STUDENT DETAILS')
        print('='*30)
        print(f'Name: {self.name}')
        print(f'ID: {self.id}')
        print(f'Marks: {marks}')
        print(f'Total Marks: {self.calTotal()}')
        print(f'Average Marks: {round(self.calAvg(), 2)}')
        print('='*30)
    
    def calTotal(self):
        return sum(self.marks)

    def calAvg(self):
        return sum(self.marks) / len(self.marks)


id = input('Enter ID: ')
name = input('Enter Name: ')
marks = list(map(float, input('Enter marks (m1 m2 m3): ').split()))

student = Student(name, id, marks)
student.printDetails()
