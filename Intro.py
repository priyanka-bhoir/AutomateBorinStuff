#list

def eggs(someparameter):
    someparameter.append("hello")


spam = [1,2,3]
eggs(spam)
print(spam)

# copy.deepcopy makes a seprate list

import copy
cheese = copy.deepcopy(spam)
cheese[1] = 50
print(cheese)

# '/' line for ignore indentation and going to next line
