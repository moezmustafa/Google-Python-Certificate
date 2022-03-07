#returning_vlaues_from_methods

class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 3

ploggy = Piglet()
ploggy.years = 5
print(ploggy.pig_years())

