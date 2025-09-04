class Consumer:
    UNIT_COST = 3.80

    def __init__(self, name, id, last_month_reading, present_reading):
        self.name = name
        self.id = id
        self.last_month_reading = last_month_reading
        self.present_reading = present_reading

        self.totalUnits = self.calcTotalUnits()
        self.bill_amt = self.calcBill()
        self.UNIT_COST = self.get_cost_per_unit(self.totalUnits)

    def printDetails(self):
        print('='*30)
        print('CONSUMER DETAILS')
        print('='*30)
        print(f'Name: {self.name}')
        print(f'ID: {self.id}')
        print(f'METER DETAILS:')
        print(f'    Last Month Reading: {self.last_month_reading}')
        print(f'    Present Reading: {self.present_reading}')
        print(f'    Total Units: {self.totalUnits}')
        print(f'Bill Amount: {self.bill_amt}')
        print('='*30)
    
    def calcBill(self):
        return self.totalUnits * self.UNIT_COST

    def calcTotalUnits(self):
        return self.present_reading - self.last_month_reading
    
    def get_cost_per_unit(self, units):
        cost = 3.80
        if units > 300:
            cost = 3.80
        elif units > 200:
            cost = 6.30
        elif units > 100:
            cost = 5.10
        elif units > 50:
            cost = 4.20
        
        return cost
        

id = input('Enter ID: ')
name = input('Enter Name: ')
last_month_reading = int(input('Enter Last month reading: '))
present_reading = int(input('Enter present reading: '))

consumer = Consumer(name, id, last_month_reading, present_reading)
consumer.printDetails()
