def sing():
    
    for i in range(100, 1, -1):
        
        if i == 1:
            print(i + ' bottles of milk on the wall, ' + i +' bottles of milk.')
            print('Take one down and pass it around, no more bottles of milk on the wall.')
            
        elif i == 0:
            print('No more bottles of milk on the wall, no more bottles of milk.')
            print('Go to the store and buy some more, 99 bottles of milk on the wall.')
        else:
            print(i + ' bottles of milk on the wall, ' + i +' bottles of milk.')
            print('Take one down and pass it around, '+ (i-1) +' bottles of milk on the wall.')       
