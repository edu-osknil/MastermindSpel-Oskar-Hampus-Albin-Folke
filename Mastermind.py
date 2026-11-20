import random as rand

def intro():
    '''printar startmeddelandet'''
    print("""
    Datorn kommer att slumpa fram en kod på fyra siffror mellan 1 och 6.
    Du ska försöka gissa denna kods siffror på max 12 drag.
    Efter respektive gissning så kommer du att få en respons:
    För varje gissad korrekt siffra på korrekt plats i koden: ✔
    För varje gissad siffra på fel plats i koden: ▢
    För de siffror som inte finns med i koden ges ingen markering.

    Exempel: om den slumpade koden är 2315
    och du gissar 3165
    så blir responsen ✔▢▢

    Du får välja mellan två svårighetsnivåer:
    Lättare nivå: Alla siffror är garanterat olika
    Svårare nivå: Det kan finnas upprepningar av en eller flera siffror
    """)
    
def dif(): 
    '''returnerar 1 eller 2 beroende på svar, säker inmatning'''
    while True:
        ans=input("Ange önskad nivå: lättare (1), svårare (2) -> ")
        if ans=='1' or ans=='2':
            return int(ans)
        print("Felaktig inmatning, skriv en siffra")

def codeGen(ans):
    '''genererar en kod beroende på om inmatningen är 1 eller 2'''
    num=list(range(1,7))
    codeT = ""
    for i in range(4):
        if ans==1: #flyttar ett slumpat index från num till codeT (1)
            randIdx=rand.randint(0,5-i)
            codeT+=str(num[randIdx])
            num.pop(randIdx)
        elif ans==2: #slumpar fram fyra tal (2)
            codeT += str(rand.randint(1,6))
    return codeT

def giveFeedback(a): 
    '''tar emot en gissning (a) och returnerar feedbacken'''
    retStr=[]
    guessT=list(a)
    codeT=list(code)
    for i in range(4): #kollar om respektive siffra finns i kodens motsvarande plats
        if guessT[i]==code[i]:
            retStr.append("✓")
            guessT[i]=0
            codeT[i]=0
    for i in guessT: #kollar om respektive siffra finns i koden alls
        if i in codeT and i!=0:
            retStr.append("▢")
            codeT.remove(i)
    return "".join(retStr)

def guessPrint(guessT): 
    '''tar in en gissning (guess) och printar loggen för alla gissningar'''
    guesses.append(guessT)
    print(f"Drag #    Drag        Feedback\n{'-'*43}")
    for i in range(12,0,-1):
        #printar nummer
        print(f"\n{i:<8}",end="")
        #printar gissningar
        try:
            print(f"{' '.join(guesses[i-1]):<14}",end="")
        except IndexError:
            pass
        #printar feedback
        try:
            print(feedbacks[i-1],end="")
        except IndexError:
            pass
        print()

def retry():
    '''låter spelaren välja om den vill köra igen, säker inmatning'''
    while True:
        igen=input("Vill du spela igen (j/n) --> ")
        if igen.lower()=='j' or igen.lower()=='n':
            return igen.lower() == 'j'
        print("Felaktig inmatning")

def checkGuess(guessT):
    '''tar in guess och kollar ifall den uppfyller kraven för en giltig gissning, returnerar boolesk variabel'''
    right = len(guessT) == 4
    for char in guessT:
        if not guessT.isdigit() or guessT.isdigit() and (int(char) < 1 or int(char) > 6):
            right = False
    if not right:
        print("Ogiltig gissning")
    return right


#---------- Huvudprogram ----------
intro()

while True:
    #deklarerar grundläggande variabler
    won=0
    guesses=[]
    feedbacks=[]
    code=codeGen(dif())
    
    for times in range(1,13):
        while True:
            #tar in gissning
            guess=input("\nAnge gissning som följd av fyra siffror --> ") 
            if checkGuess(guess):
                break
        #printar ut loggen inkl. senaste gissningen
        feedbacks.append(giveFeedback(guess))
        guessPrint(guess)
        #kollar om du van
        if guess==code:
            print(f"Du vann på {len(guesses)} försök!")
            won=1
            break
    if won==0:
        print(f"Du förlorade, rätt kod var: {code}")
    
    if retry():
        continue
    break
        
print("Programmet avslutades")