def animal_cracker(namestr):
    words=namestr.split()
    if words[0][0].upper() == words[1][0].upper():
        print(f'Starting letters are same in {words[0]} and {words[1]}')
    else:
        print(f'Starting letters are not same in {words[0]} and {words[1]}')
    return

def makes_twenty(num1,num2):
    if num1==20 or num2==20 or num1+num2==20:
        return True
    else:
        return False

def reverse_sentence(sentence):
    wordlist=sentence.split()
    final_sent=''
    for items in wordlist:
        final_sent=items + ' ' + final_sent
    return final_sent

def summer_69(numlst):
    total=0
    stopaddition=False
    for x in range(0,len(numlst)) :
        if numlst[x]==6:
            stopaddition=True
            total=total+0
        elif stopaddition==False:
            total=total+numlst[x]
        elif numlst[x]==9:
            stopaddition=False
    return total

print(summer_69([2,4,1,6,7,1,9,4]))
'''print (reverse_sentence('My dog name is Kafee'))
print(makes_twenty(20,10))



animal_cracker('hello Jarry')'''

