l = [2,3,5,7]
for i in range(0,2):
    if i == 0:
        x = int(input("Enter your first number: "))
    else:
        y = int(input("Enter your second number: "))
lx = x
ly = y
lcm = 1
for i in l:
    if lx%i == 0 and ly%i == 0:
        while (lx%i == 0) and (ly%i == 0):
            lx/=i
            ly/=i
            lcm*=i
    else:
        continue
lcm = lcm*lx*ly
print("The LCM of two numbers is: ",lcm) 

if x>y:
    r = x%y
    m=y
    q=r
    if r != 0:
        while r!=0 :
            r = m%q
            if r == 0:
                print("the gcd of the two numbers is: ",q)
            m = q
            q = r
        
    else:
        print("the gcd of two numbers is: ",y)
else:
    r = y%x
    m=x
    q=r
    if r != 0:
        while r!=0 :
            r = m%q
            if r == 0:
                print("the gcd of the two numbers is: ",q)
            m = q
            q = r
        
    else:
        print("the gcd of two numbers is: ",x)
