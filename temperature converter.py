d=float(input('enter the temperature : '))
u=str(input('enter the unit given : '))
l=str(input('enter the unit required : ')) 
if u == 'F' and l == 'C' :
    q=5*((d-32)/9)
    print(q,'celcius')
elif u == 'F' and l == 'K' :
    m=(d-32)*(5/9)+273.15 
    print(m,'kelvin')
elif u == 'C' and l == 'F' :
    p=9*(d/5)+32
    print(p,'farenheit')
elif u == 'C' and l == 'K' :
    n=d+273.15
    print(n,'kelvin')
elif u == 'K' and l == 'C' :
    r=d-237.15
    print(r,'celcius')
elif u == 'K' and l == 'F' :
    h=(d-273.15)*(9/5)+32 
    print(h,'farenheit')
  
  
