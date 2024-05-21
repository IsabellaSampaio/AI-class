import random

class UpgradedBot: 
    def __init__(self, mode, loc, energy):
        self.mode = mode
        self.loc = loc
        self.energy = energy
    
    def move(self, size):
        self.loc+=1
        if(self.loc == size):
            self.loc = 0
    
    def drainEnergy(self):
        print("Draining bot's battery in -1")
        self.energy -= 1

    def shutDownByEnergyLevel(self, energy):
        print("Bot is shutting down because it ran out of battery")
        self.mode = 0
    

class Environment:
    def __init__(self, bot_loc, bot_trace):
        self.bot = UpgradedBot("ON", bot_loc, 20)
        self.bot_loc = bot_loc
        self.bot_trace = bot_trace 

    def cleaning(self, spots):
        if(spots[self.bot_loc] == 0):
            print("Spot is clean, moving on")

        elif(spots[self.bot_loc] == 1):
            print("Cleaning spot...")
            spots[self.bot_loc] = 0
            self.bot.drainEnergy()

        self.bot_trace.append(self.bot_loc)
        updated_spots = spots

        if(len(self.bot_trace) == len(spots)):
            self.bot.mode = "OFF"

        if(self.bot.mode != "OFF"):
            self.bot.move(len(spots))
            self.bot_loc = self.bot.loc
            self.bot.drainEnergy()
            print(f"Bot moved to location {self.bot_loc}")
            self.cleaning(updated_spots)


rand = random.randint(0,1)
bot_trace = []
spots = [0,1]
environment = Environment(rand, bot_trace)

print(f"Bot started at location {rand}")

environment.cleaning(spots)

print(f"Bot ended at location {environment.bot_loc}")
print(f"Bot trace {environment.bot_trace}")
   
