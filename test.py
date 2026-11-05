mySet = set()
myDict = {}

# myDict["Odoo 1"] = 11
myDict["Odoo 2"] = 12
# myDict.setdefault("Odoo 1", 0)
c = myDict.get("Odoo 1", 0) - 1
print(c)

print(myDict["Odoo 2"])

myList = [1,1,1,1,1,1,1,1,1,1,1,1,2]

mySet = set(myList)

print(mySet)

def test(*args):
    print(type(args))

def testKwargs(**kwargs):
    print(type(kwargs))

test(1,2,3,4,5,6)
testKwargs(name='seb',age='24')

