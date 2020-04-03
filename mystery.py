
def double(arg):
    print('Before: value ', arg, ' Id ', id(arg))
    arg = arg * 2
    print('After: value ', arg, ' Id ', id(arg))

def change(arg):
    print('Before: value ', arg, ' Id ', id(arg))
    arg.append('More data')
    print('After: value ', arg, ' Id ', id(arg))

num = 10 
double(num)
print(num)

nums = [1,2,3]
change(nums)
print(nums)