def move (f , t) :
    print("move disc from {} to {}!".format(f, t))



move ("A" , "C")
def moveVia(f,v,t):
    move(f,v)
    move(v,t)
    moveVia("A","B","C")

def foo(x):
    foo(x)

foo(3)
#[N]umber of disk, [F]rom position, [H]elper position, [T]arget position.
def hanoi(n, f, h, t): 
    if n==0 :
        pass
    else:
        hanoi(n - 1, f, t, h)
        move(f, t)
        hanoi(n - 1, h, f, t)

hanoi(4, "A","B","C")






