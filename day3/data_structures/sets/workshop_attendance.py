class WorkShop:
    def __init__(self, *attendance):
        self.no_of_days = 3
        self.data = attendance
        self.attendees = self.clean_data()
    
    def clean_data(self):
        attendees = []
        for i in self.data:
            attendees.append(set([j.lower() for j in i]))
        
        return attendees
    
    def unique_attendees(self):
        unique = set()
        for i in self.attendees:
            unique |= i
        
        return unique
    
    def all_days_attendees(self):
        all_days = self.attendees[0]
        for i in self.attendees:
            all_days &= i 
        
        return all_days
    
    def one_day_attendees(self):
        one_day = set()
        for i in self.attendees:
            one_day ^= i
        
        return one_day
    
    def pairwise_day_attendees(self):
        pass
    
    def display(self):
        print('-'*30)
        print('Workshop Report'.center(30, ' '))
        print('-'*30)
        print(f'Number of days: {self.no_of_days}')
        print(f'All attendees count: {len(self.unique_attendees())}')
        print(f'Number of attendees attended all days: {len(self.all_days_attendees())}')
        print(f'Number of attendees attended only one day: {len(self.one_day_attendees())}')
        print(f'Pairwise attendees: ')


day1 = ["alice@example.com", "Bob@Example.com", "carol@example.com", "alice@example.com"]
day2 = ["bob@example.com", "dave@example.com", "carol@example.com"]
day3 = ["ALICE@EXAMPLE.COM", "carol@example.com", "erin@example.com"]

workshop = WorkShop(day1, day2, day3)
workshop.display()

# TODO: complete the bugs
