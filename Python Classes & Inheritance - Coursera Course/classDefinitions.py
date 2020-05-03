"""
    Final code submission
"""
import random

VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer():
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
        
    def addMoney(self, amt):
        self.prizeMoney += amt
    
    def goBankrupt(self):
        self.prizeMoney = 0
    
    def addPrize(self, prize):
        self.prizes.append(prize)
    
    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)


# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
        
    def getMove(self, category, obscuredPhrase, guessed):
        print(super().__str__())
        print("\nCategory: ", category)
        print("Phrase: ", obscuredPhrase)
        print("Guessed: ", guessed)
        return input("Guess a letter, phrase, or type 'exit' or 'pass':")
        
# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    
    SORTED_FREQUENCIES = "ZQXJKVBPYGFWMUCLDRHSNIOATE"
    
    def __init__(self, name, difficulty):
        super().__init__(name)
        self.difficulty = difficulty
    
    def smartCoinFlip(self):
        return True if random.randint(1, 10) > self.difficulty else False
    
    def getPossibleLetters(self, guessed):
        
        list_of_letters = [x for x in LETTERS if x not in guessed]
        if self.prizeMoney < VOWEL_COST:
            list_of_letters = [x for x in list_of_letters if x not in VOWELS]
        
        return list_of_letters
    
    def getMove(self, category, obscuredPhrase, guessed):
        super().__str__()
        possible_letters = self.getPossibleLetters(guessed)
        if possible_letters:
            if self.smartCoinFlip():
                for x in WOFComputerPlayer.SORTED_FREQUENCIES[::-1]:
                    if x in possible_letters:
                        return x
            else:
                return random.choice(possible_letters)
        else:
            return "pass"


"""
    Prior attempt
"""
import random

VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer():
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
        
    def addMoney(self, amt):
        self.prizeMoney += amt
    
    def goBankrupt(self):
        self.prizeMoney = 0
    
    def addPrize(self, prize):
        self.prizes.append(prize)
    
    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)


# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
        
    def getMove(self, category, obscuredPhrase, guessed):
        print(super().__str__())
        print("\nCategory: ", category)
        print("Phrase: ", obscuredPhrase)
        print("Guessed: ", guessed)
        return input("Guess a letter, phrase, or type 'exit' or 'pass':")
        
# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    
    SORTED_FREQUENCIES = "ZQXJKVBPYGFWMUCLDRHSNIOATE"
    
    def __init__(self, name, difficulty):
        super().__init__(name)
        self.difficulty = difficulty
    
    def smartCoinFlip(self):
        return True if random.randint(1, 10) > self.difficulty else False
    
    def getPossibleLetters(self, guessed):
        
        print(self.prizeMoney)
        list_of_letters = [x for x in LETTERS if x not in guessed]
        print("list without guessed letters: ", list_of_letters)
        if self.prizeMoney < VOWEL_COST:
            list_of_letters = [x for x in list_of_letters if x not in VOWELS]
        
        return list_of_letters
        
        """
        if self.prizeMoney < VOWEL_COST:
            print("in true")
            return [x for x in LETTERS if x not in VOWELS]
        else:
            print("in false")
            return [x for x in LETTERS if x not in guessed]"""
    
    def getMove(self, category, obscuredPhrase, guessed):
        print(super().__str__())
        print("Guessed --> ", guessed)
        possible_letters = self.getPossibleLetters(guessed)
        #possible_letters = possible_letters.sort()
        if possible_letters:
            print(possible_letters)
            if self.smartCoinFlip():
                for x in WOFComputerPlayer.SORTED_FREQUENCIES[::-1]:
                    if x in possible_letters:
                        print(x)
                        return x
            else:
                return random.choice(possible_letters)
            '''for x in possible_letters:
                if x not in VOWELS:
                    if self.smartCoinFlip():
                        return WOFComputerPlayer.SORTED_FREQUENCIES[0]
                    else:
                        return random.choice(LETTERS)'''
        else:
            return "pass"
        