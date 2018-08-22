#Ques1
def area():
    a=int(input("enter radius of sphere"))
    pi=3.14
    ar=4*pi*a*a
    return ar
b=area()
print("area of sphere is = ",b)

#Ques2
def perfect(s):
    total=0
    if s==1:
        print(s)
    else:
        for i in range(1,s):
            if s%i==0:
                total=total+i
        if total==s:
             print(s) 
for i in range(1,1000):
    b=perfect(i)

#Ques3
def multi(n):
    for i in range(0,11):
        b=n*i
        print(n,"*",i,"=",b)
x=int(input("enter no"))
a=multi(x)

#Ques4
c=int(input("enter no"))
d=int(input("enter power"))
def pow(c,d):
    if d==0:
        return 1
    if d>0:
        return c*pow(c,d-1)
print("ans = ",pow(c,d))    

