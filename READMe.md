Python Cook book Chapter 1 Data Structures and Algorithms

Covered Unpacking variables with fixed and arbitrary length

deque uses/is a basically a fixed/unbounded(not fixed) length queue, when something new is added the earliest value is removed.

heapq module is best for looking for teh n smallest or n largest values, when ny is significantly smaller than the size of the collection.

heaps can be used with priority

Using defaultdict

To Do: Differentiate between iterator and iterables

What are hashable items?

Lambda functions basics - to learn

Learned how to use pprint package for making terminal outlook look more legible.

    import pprint
    stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
    stuff.insert(0, stuff[:])
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(stuff)

    pp.pprint(data)