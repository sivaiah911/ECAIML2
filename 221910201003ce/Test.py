def centuryFromYear(year):
    
    m = year % 100
    print(m)
    if m == 0 :
        cet = year / 100
    else :
        cet = int( year / 100 ) + 1
        
    print(cet)
    return cet


centuryFromYear(1905)