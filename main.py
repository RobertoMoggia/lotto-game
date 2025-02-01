import lottoGame
import re

print('LOTTO GAME BILL GENERATOR')
billNumber=input('How many bills you want to generate? Enter an integer between 1 and 5 (0 to exit): ')
while not billNumber in ['0','1','2','3','4','5']:
    billNumber=input('Only an integer between 1 and 5 (0 to exit)! Retry: ')

billNumber=int(billNumber)
if billNumber==0:
    print('EXIT')
else:
    billsList=[]
    for i in range(billNumber):
        ruota=input('Enter the "ruota where you want to play (Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia or Tutte): ')
        while not ruota.lower() in ["bari", "cagliari", "firenze", "genova", "milano", "napoli", "palermo", "roma", "torino", "venezia", "tutte"]:
            ruota=input('{} is not an existing "ruota"! Retry: '.format(ruota))

        guesses=input("Enter the list of guess types in this way 'guesstype1,guesstype2,...' (remember that 1=estratto, 2=ambo, 3=terna, 4=quaterna, 5=cinquina and that at most 10 numbers for bill are allowed): ")
        guessesNumber=11
        while guessesNumber>10:
            while not re.fullmatch('([1-5],)*[1-5]{1}',guesses):
                guesses=input('Wrong syntaxt, retry: ')
            guesses=[int(i) for i in guesses.split(',')]
            guessesNumber=sum(guesses)
            if guessesNumber>10:
                guesses=input('At most 10 numbers for bill! Retry: ')
        
        billsList.append(lottoGame.Bill(ruota,*guesses))
    
    print("Here's your bills!")
    lottoGame.billsPrinter(*billsList)
