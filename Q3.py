import math
from inspect import signature

print("######Q1#######")

def func(funcList):
    return list(map(lambda f: f.__name__, filter(lambda fn: len(signature(fn).parameters) < 2, funcList)))

def func1(a,b,c):
    pass

def func2(a):
    pass

def func3():
    pass
l = (func1, func2, func3)
print(func(l))
print("\n######Q2#######")

numbers = [1, 2, 3, 4]
(lambda total: print(total))((sum(num for num in numbers)))

print("\n######Q3#######")

number = 9 # choose your number
print("for number ", number)
(lambda sqrt: print(int(sqrt)) if (sqrt % 1 == 0) else print(0))(math.sqrt(number))
number = 8 # choose your number
print("for number ", number)
(lambda sqrt: print(int(sqrt)) if (sqrt % 1 == 0) else print(0))(math.sqrt(number))

print("\n######Q4#######")

sentences = ['Mary read a story to Sam and Isla.', 'Isla cuddled Sam.', 'Sam chortled.']
print(sentences)
(lambda sam_count: print("Sam count is:", sam_count))(sum(sentence.count('Sam') for sentence in sentences))

print("\n######Q5a#######")

input =0
output =0
count =0
def dec(func):
    def wrapper(*args):
        global input
        global output
        global count
        count += 1
        l= []
        targs = list(args)
        for i in targs:
            if isinstance(i,int):
                input = (input +i) /count
        output= (output + func(*targs)) /count
        l.append(input)
        l.append(output)
        t = tuple(l)
        print(t)
    return wrapper

@dec
def f(x):
    return x
@dec
def f2(y):
    return y+1

##Decorator 5 a
print(f(5))
print(f2(5))
print("\n######Q5b#######")

##Decoartor 5b
def logg(func):
    def wrapper(*args,**kwargs):
        targs = list(args)
        l =[]
        for i in targs:
            l.append(i)
        tkwargs =kwargs
        for i in tkwargs.values():
            l.append(i)
        t = tuple(l)
        print("you called func ",t," it returned: ",func(*targs, **tkwargs))
    return wrapper

##you called func(4, 4, 4) it returned 6
@logg
def func1log(x,y):
    return x+y

print(func1log(6,y=7))
print("\n######Q6#######")

counter = 0
functionname = []
def functionNameDec(func):
    def wrapper(*args):
        global counter
        global functionname
        l =[]
        functionname.append(func.__name__)
        counter +=1

        if(counter>2):
            for i in range(len(functionname)-3,len(functionname)):
                l.append(functionname[i])
            print("the current list",l)
    return wrapper

@functionNameDec
def func1(a):
    pass
@functionNameDec
def func2(a):
    pass
@functionNameDec
def func3(a):
    pass
func1(1)
func2(1)
func3(1)
print("\n######Q8#######")

def f1(x, y=[]):
    y.append(x)
    return sum(y)
def f2(x, y=None):
    if y is None:
        y = []
    y.append(x)
    return sum(y)
print(f1(10))
print(f1(30))
print(f2(10))
print(f2(30))
## ההבדל בין הפונקציות הינו שבפןקנציה הראשונההגדרה של המשתנה הסוכם היא מחוץ לפנוקציה כמשתנה גלובלי ולכן היא צוברת את ערכי איקס לעומת הפוקנצייה השנייה שבה המשתנה הסוכם הינו לוקלי והוא מאפס בכל איטרציה
print("\n######Q9#######")

class a():
    global z
    z = 4
    def __init__(self,y):
        self.y =y
        self.z= z
    def __call__(self,z):
        if z > self.y:
            return z-self.y
        else:
            return self.y-z
class b(a):
    def __call__(self,*args):
        if z > self.y:
            return z-self.y
        else:
            return self.y-z
print(a(5)(b(6)()))
print(a(6)(b(5)(6)))

print("\n######Q10#######")

functionCallDic = {}
functionArgsDic = {}
functionTypeDic = {}
def functionNameDec(func):
    def wrapper(*args,**kwargs):
        global counter
        global functionCallDic
        global functionArgsDic
        global functionTypeDic

        if func.__name__ in functionCallDic.keys():
            functionCallDic[func.__name__ ] +=1
        else:
            functionCallDic[func.__name__ ]=1
        if not func.__name__ in functionArgsDic.keys():
            functionArgsDic[func.__name__]=len(args)+len(kwargs)
        else:
            functionArgsDic[func.__name__]+=len(args)+len(kwargs)
        ttype = type(func(*args, **kwargs))
        if not ttype in functionTypeDic.keys():
            functionTypeDic[ttype] = 1
        else:
            functionTypeDic[ttype] += 1

        print("statistic Function print: ")
        for name in functionCallDic.keys():
            print(name," calls :",functionCallDic[name],", Parameters :", functionArgsDic[name])
        print("Type statistic :")
        print(functionTypeDic)
        print("--------------------------------------------------------------------------")
    return wrapper

@functionNameDec
def func1(x,y,z):
    return 5
@functionNameDec
def func2(x):
    return 'str'
@functionNameDec
def func3(x,k):
    return x
func1(1,2,3)
func1(4,5,z=6)
func2(0)
func2(1)
func3(x=1,k=3)
## לא ניתן לממש דקורטייטור זה בגוואה כיוון שהפרדיגמה בגוואה עובדת פר מחלקה עבור דקרותור לעומת זאת בפייתון הינה פרדימגמה פונקציונאלית
