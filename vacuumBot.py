import random 

class Cbot: 
    def __init__(self, mode, loc, trace):
        self.mode = mode
        self.loc = loc
        self.trace = trace

    def move(self, size):
        self.loc+=1
        if(self.loc == size): 
            self.loc = 0

    def cleaning(self, spots):
        if(spots[self.loc] == 0):
            print("Spot is clean")

        elif(spots[self.loc] == 1):
            print("Cleaning spot...")
            spots[self.loc] = 0

        self.trace.append(self.loc)
        updated_spots = spots
        
        if(len(self.trace) == len(spots)):
            self.mode = "OFF"

        if(self.mode != "OFF"):
            self.move(len(spots))
            print(f"Bot moved to location {self.loc}")
            self.cleaning(updated_spots) 

rand = random.randint(0,4)
trace = []
cleaner = Cbot("ON", rand, trace)
spots = [0,1,1,0,1]

print(f"Bot started at location {rand}")

cleaner.cleaning(spots)

print(f"Bot ended at location {cleaner.loc}")
print(f"Bot trace {cleaner.trace}")
