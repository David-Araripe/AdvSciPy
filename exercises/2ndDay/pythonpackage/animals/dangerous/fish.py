class Fish:
    def __init__(self):
        '''constructor for this class'''
        # Create some member animals
        self.members = ["Shark", "Tuna", "Salmon"]
    def printMembers(self):
        print("Printing members of the Fish class")
        for member in self.members:
            print('\t%s ' % member)