def decor(func):
    def wrap():
        print("="*int(len(func())))
        func()
        print("="*int(len(func())))
    return wrap

@decor
def print_text(x):
    print (x)
    return x

words = "I just want to test"
print_text();

# def make_word():
#     word = ""
#     for ch in "spam":
#         word += ch
#         yield word

# print(list(make_word()))


# def isPrime(x):
#     if x < 2:
#         return False
#     elif x == 2:
#         return True  
#     for n in range(2, x):
#         if x % n ==0:
#             return False
#     return True

# def primeGenerator(a, b):
#     for i in range(a,b):
#         if isPrime(a):
#             yield a
#         a+=1
    
# f = int(input())
# t = int(input())

# print(list(primeGenerator(f, t)))