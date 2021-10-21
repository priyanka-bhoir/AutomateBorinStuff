# dictionaries have no order

eggs = {'name':'zophie','spices':'cat','age':8}
ham = {'spices':'cat','name':'zophie','age':8}

print(eggs == ham)

#

print("name" in eggs)

# dictionaries are mutable
print(list(eggs.keys()))

print(list(eggs.values()))

print(list(eggs.items()))# this will return tuples

# get work as turnerry operator

print(eggs.get("name","l"))
print(eggs.get("cat","l"))

# setdefault method
print(eggs.setdefault('color','black'))
print(eggs)
