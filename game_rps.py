import random
print('Hello world')

def check(comp, user):
    if comp==user:
        return 0
    if(comp==2, user==1):
        return -1
    if(comp==0,user==2):
        return -1
    if(comp==1,user==0):
        return -1
    else:
        return 1

print('rock 0,paper 1 ,scessor 2')
comp = random.randint(0,2)
user = int(input('0 for rock, 1 for paper,2 for scissors'))


score = check(comp, user)
print('computer:',comp)
print('you:', user)

if(score==0):
    print('its a draw')
if(score==-1):
    print('you won')
if(score == 1):
    print('you won')