import random
f = open("words.txt", "r")
lis=list(f.read().split('\n'))
pcword=lis[random.randint(0,len(lis)-2)]
out=[]
for x in range(len(pcword)):
    out.append('_ ')
print(f'the word is of length: {len(out)}\nYou have 6 chances')
for i in range(6):
    guess=input("Guess a letter in the word: ")
    if guess in pcword:
        for x in range(len(pcword)):
            if pcword[x]==guess:
                out[x]=guess
        print(''.join(out))
        print(f'you have {5-i} chances')
    else:
        print("Wrong guess")
        print(f'you have {5-i} chances')
if ''.join(out)==pcword:
    print('You Win!')
else:
    print(f"Your loose\nThe word is {pcword}")
    
