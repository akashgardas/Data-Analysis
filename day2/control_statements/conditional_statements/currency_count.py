class Currency:
    def __init__(self, amt, available_notes=[500, 200, 100, 50, 20, 10]):
        self.amt = amt
        self.available_notes = sorted(available_notes, reverse=True)
        
    def count_notes(self):
        temp = amt
        count = 0
        for note_value in self.available_notes:
            count += temp // note_value
            temp %=  note_value
            
        return count


amt = 880
# 11, 1, 1

currency = Currency(amt)

print(currency.count_notes())