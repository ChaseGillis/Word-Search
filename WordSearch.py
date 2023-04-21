# function:   cleanup_string
# input:      a string to clean up
# processing: (1) makes the entire string lowercase.
#             (2) retains only alphabetic, numeric and space characters
#                 [all punctuation and special characters removed]
# output:     returns the cleaned up string
def cleanup_string(data):
    newstring = ''
    data = data.lower()
    data = data.strip()
    for i in data:
        if i.isalnum() or i.isspace():
            newstring += i
    return newstring

'''
# TEST CODE
test1 = cleanup_string("Hello World! This is a simple test of this function!")
print (test1)
# hello world this is a simple test of this function

test2 = cleanup_string("ABC123abc this is Another TEST!!!#@@")
print (test2)
# abc123abc this is another test

test3 = cleanup_string("I'm so happy today! La la la la it doesn't get any better than this.")
print (test3)
# im so happy today la la la la it doesnt get any better than this'''

import os
files = os.listdir("data")
if  '.DS_Store' in files:
    print('Here it is!', files.find('.DS_Store'))

search = {}
for i in files:
    file= open('data/'+i, 'r')
    data = file.read()
    file.close()
    data = cleanup_string(data)
    newdata = data.split(' ')
    for j in newdata:
        list = []
        list.append(i)
        if j not in search:
            search[j] = list
        elif i not in search[j]:
            search[j].append(i)

x = 0
for i in search.keys():
    x += 1
#print(x)

'''
print ('happy:', search['happy'])
print ('cat:', search['cat'])
print ('rainbow:', search['rainbow'])
print ('apple:', search['apple'])

# OUTPUT

happy: ['aUAFHAlczU.txt', 'R2ECugDCAv.txt']
cat: ['jJG5h8GyyY.txt']
rainbow: ['L9fMTLX60i.txt', 'S0zDFkXpZW.txt']
RUNTIME ERROR (apple does not exist as a KEY in the dictionary)
'''
while True:
    wordsearch = input('search for a (s)ingle word or (q)uit: ')
    if wordsearch == 'q':
        break
    elif wordsearch == 's':
        try:
            word = input('Enter a word to search for: ')
            if word not in search:
                raise KeyError
        except KeyError:
            print("'"+word+"'", 'cannot be found')
        else:
            print("'"+word+"'", 'can be found in',len(search[word]), 'files')
            print('These files are:')
            for i in search[word]:
                print('* ', i)
            y_or_n = input('Display these files? (y/n): ')
            print()
            if y_or_n == 'y':
                for i in search[word]:
                    print('* ', i)
                    newestfile = open('data/'+i, 'r')
                    newestdata = newestfile.read()
                    newestfile.close()
                    print(newestdata)
                    print()
            elif y_or_n == 'n':
                break
            else:
                print('Invalid input')
    else:
        print('Invalid command')
        print()
