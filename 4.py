i = 0
count = 0
str = ''
roman_list = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
roman_dict = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
arabic_dict = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}

while True:
    print '1. Arabic to Roman'
    print '2. Roman to Arabic'
    answer = raw_input('> ')
    if answer == '1':  
        num = int(raw_input('Arabic to Roman: '))     
        while i < len(roman_list):
            if num / roman_list[i] != 0:
                mod = num % roman_list[i]
                div = num / roman_list[i]
                str += roman_dict[roman_list[i]] * div
                num = mod    
            i+=1
        print '-' * 10
        print str
        print '-' * 10
        str = ''
        i = 0

    elif answer == '2':
        num = raw_input('Roman to Arabic: ')
        while i < len(num):
            if i+1 < len(num) and (num[i] + num[i+1]) in arabic_dict:
                count += arabic_dict[num[i] + num[i+1]]
                i += 2
            else:
                count += arabic_dict[num[i]]
                i += 1
        print '-' * 10        
        print count
        print '-' * 10
        i = 0
        count = 0
    else:
        print 'Wrong input. Exiting application'
        exit(0)