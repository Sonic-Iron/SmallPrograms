
americanCountries = ['USA','Mexico','Canada','Alaska']
southamericanCountries = ['Brazil','Chile','Argentina','Peru','Colombia','Venezulea','Uruguay']
aftericanCountries = ['South Aftica','Nigeria','Kenya','Morocco','Ghana','Ethiopia','Uganda']
europeanCountries = ['UK','France','Spain','Belgium','Germany','Poland','Italy']
asiancountries = ['China','India','Japan','South Korea','North Korea','Nepal','Saudi Arabia']
australianCountries = ['Australia','Papua New Guinea','Indonesia','Solomon Islands','New Zealand']
antaricanCountries = ['Antartica']

class player():
    def __init__(self, playerID, location):
        self.playerID = playerID
        self.location = location
        self.countries = []
        if self.location == 'America':
            for a in americanCountries:
                self.counties.append(a)
        if self.location == 'South America':
            for a in southamericanCountries:
                self.countries.append(a)
        if self.location == 'Africa':
            for a in aftericanCountries:
                self.countries.append(a)
        if self.location == 'Europe':
            for a in europeanCountries:
                self.countries.append(a)
        if self.location == 'Asia':
            for a in asiancountries:
                self.countries.append(a)
        if self.location == 'Australia':
            for a in australianCountries:
                self.countries.append(a)
        if self.location == 'Antartica':
            for a in antaricanCountries:
                self.countries.append(ca)

        

class country():
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def changeOwner(old, new):
        old.removeCountry(self)
        self.owner = new.PlayerID
        new.addCountry(self)

class continant():
    def __init__(self, name, startOwner):
        self.name = name
        self.startOwner = startOwner

    def addCountry(self):
        self.countries.append(country())

    def removeCountry

def main():
    playerList = []
    continantList = ['America','Europe',]
    for a in continantList:
        
    Nplayers = input('How many players?')
    for a in range(Nplayers):
        for a in 
        location = input('Player'+str(a+1)+' where would you like to start?')
        playerList.append(player(a+1, ))
    
    
main()        
