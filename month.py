m=input('Enter the month name: ');
if(m=='february'):
    y=int(input('Please specify the year: '));
    if(y%4==0) :
        print('Leap year hence 29 days');
    else:
        print('Non leap year hence 28 days');
elif m in ("january","march","may","july","august","october","december") :
    print('31 days');
elif m in ('april','june','september','november') :
    print('30 days');

else:
    print('Wrong Month');
