import math

st='print only the word that start with s in this sentence'
lst=st.split()
final_sentence=''
for items in lst:

    if items[0]=='s':
        final_sentence=final_sentence + ' ' + items

print(final_sentence)

even_num=[ x for x in range(0,11) if x % 2 ==0 ]
print (even_num)

num_div =[x for x in range(0,51) if x % 3==0]
print(num_div)

str1='print every word in this sentence that has an even number of letters'
lststr1=str1.split()
for items in lststr1:
    if len(items) % 2==0:
        print('even')
print('fizz buzz fizzbuzz')
for x in range(0,101):
    if x%3==0 and x%5==0:
        print('fizzbuzz')
    elif x%3==0:
        print('fizz')
    elif x%5==0:
        print('buzz')
    else:
        print(x)


print('list comprehension')
str3='create a list of first letter of every word in this string'
lststr3=[ s[0] for s in str3.split()]
print(lststr3)




