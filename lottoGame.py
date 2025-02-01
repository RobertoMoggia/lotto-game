import random

def billsPrinter(*args):
    if not all(type(bill)==Bill for bill in args):
        raise(TypeError('Only object of class Bill!'))
    billsNumber=len(args)
    billNumberColumnWidth=max(len(str(billsNumber)),len('Bill number'))
    ruotaColumnWidth=len('Ruota')
    guessColumnWidth=len('Guesses')
    for bill in args:
        if ruotaColumnWidth<len(bill.city):
            ruotaColumnWidth=len(bill.city)
        
        if guessColumnWidth<len(str(bill.guessList))-2:
            guessColumnWidth=len(str(bill.guessList))-2
    
    billsTable=[]
    billsTable.append('+--{}--+--{}--+--{}--+'.format('-'*billNumberColumnWidth,'-'*ruotaColumnWidth,'-'*guessColumnWidth))
    billsTable.append('|  {}{}  |  {}{}  |  {}{}  |'.format('Bill number',' '*(billNumberColumnWidth-len('Bill number')),'Ruota',' '*(ruotaColumnWidth-len('Ruota')),'Guesses',' '*(guessColumnWidth-len('Guesses'))))
    billsTable.append('+--{}--+--{}--+--{}--+'.format('-'*billNumberColumnWidth,'-'*ruotaColumnWidth,'-'*guessColumnWidth))
    for i in range(len(args)):
        bill=args[i]
        guesses=', '.join(str(guess) for guess in bill.guessList)
        billsTable.append('|  {}{}  |  {}{}  |  {}{}  |'.format(i+1,' '*(billNumberColumnWidth-len(str(i))),bill.city,' '*(ruotaColumnWidth-len(bill.city)),guesses,' '*(guessColumnWidth-len(str(guesses)))))
    billsTable.append('+--{}--+--{}--+--{}--+'.format('-'*billNumberColumnWidth,'-'*ruotaColumnWidth,'-'*guessColumnWidth))
    print('\n'.join(billsTable))

class Bill:
    def guessGenerator(self,guessType):
        return random.sample(range(1,91),guessType)

    def __init__(self,city,*args):
        if len(args)<1:
            raise(SyntaxError('At least one guess type is needed!'))
        elif not all(type(guess)==int for guess in args):
            raise(TypeError('Only int values for guessType!'))
        elif not all(guess in range(1,6) for guess in args):
            raise(SyntaxError('Review your guess types! One or more of them are not an existing guess type!'))
        elif sum(args)>10:
            raise(SyntaxError('At most 10 numbers for each bill!'))
        elif not city.lower() in ["bari", "cagliari", "firenze", "genova", "milano", "napoli", "palermo", "roma", "torino", "venezia","tutte"]:
            raise(SyntaxError('{} is not an existing "ruota"'.format(city)))
        else:
            guessList=[]
            for i in range(len(args)):
                guessList.append(self.guessGenerator(args[i]))
            self.guessList=guessList
            self.city=city
    
    def __str__(self):
        return 'Bill: Ruota di {} - {}'.format(self.city.capitalize(),self.guessList)