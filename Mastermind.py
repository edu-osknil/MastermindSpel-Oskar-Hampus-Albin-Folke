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
    code = ""
    for i in range(4):
        if ans==1: #flyttar ett slumpat index från num till codeT (1)
            randIdx=rand.randint(0,5-i)
            code+=str(num[randIdx])
            num.pop(randIdx)
        elif ans==2: #slumpar fram fyra tal (2)
            code += str(rand.randint(1,6))
    return code

def giveFeedback(a): 
    '''tar emot en gissning (a) och returnerar feedbacken'''
    retStr=[]
    g=list(a)
    codeTemp=list(code)
    for i in range(4):
        if g[i]==code[i]:
            retStr.append("✓")
            g[i]=0
            codeTemp[i]=0
    for i in a:
        if i in codeTemp:
            retStr.append("▢")
    return "".join(retStr)

def guessPrint(guess): 
    '''tar in en gissning (guess) och printar loggen för alla gissningar'''
    guesses.append(guess)
    print(f"Drag #    Drag        Feedback\n{'-'*43}")
    for i in range(12,0,-1): #printar numrerade gissningar
        print(f"\n{i:<8}",end="")
        try:
            print(f"{" ".join(guesses[i-1]):<14}",end="")
        except IndexError:
            pass
        try:
            print(feedbacks[i-1],end="")
        except IndexError:
            pass
        print()

def retry():
    while True:
        igen=input("Vill du spela igen (j/n) --> ")
        if igen=='j' or igen=='n'
            return igen
        print("Felaktig inmatning")

def checkGuess(guess):
    right = len(guess) == 4
    for char in guess:
        if not guess.isdigit() or guess.isdigit() and (int(char) < 1 or int(char) > 6):
                right = False
    if not right:
        print("Ogiltig gissning")
    return right
    
intro()

while True:
    won=0
    guesses=[]
    feedbacks=[]
    code=codeGen(dif())
    
    for i in range(1,13):
        while True:
            right = False
            guess=input("\nAnge gissning som följd av fyra siffror --> ") 
            if checkGuess(guess):
                break
        feedbacks.append(giveFeedback(guess))
        guessPrint(guess)
        if guess==code:
            print("Du van!")
            won=1
            break
    
    if won==0:
        print(f"Du förlorade, rätt kod var: {code}")
    
    if retry()=="j":
        continue
    break
        
print("Programmet avslutades")