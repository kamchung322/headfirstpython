
def removeItem():
    nums = ['A','B','C','B']
    print("Original List : ", nums)
    nums.remove('B')
    print("nums.remove('B')")
    print("Latest List : ", nums)

def popItem():
    nums = ['A','B','C','D']
    print("Original List : ", nums)
    nums.pop()

def P67Challenge():
    print("Convert Don't panic! to on tap ")
    phrase = "Don't panic!"
    plist = list(phrase)
    print(phrase)
    
    for i in range(4): #  remove last 4 letter "nic!"
        plist.pop()  
    
    plist.pop(0) # remove first letter "D"
    plist.remove("'")  # ont pa
    plist.extend([plist.pop(), plist.pop()])  # ont ap
    plist.insert(2, plist.pop(3)) # on tap
    new_phrase = ''.join(plist)
    print(new_phrase)

P67Challenge()
#popItem()
#removeItem()
