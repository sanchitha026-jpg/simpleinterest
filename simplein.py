import sys
def simple_interest(principal,interest,time):
    return (principal*interest*time)/100

if__name__=="__main__":
p= int(sys,argv[1])
i= int(sys,argv[2])
t= int(sys,argv[3])

print("Simple interest is:",simple_interest(p,i,t))