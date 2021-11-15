'''
9. Write a script to remove an empty tuple(s) from a list of tuples.
        Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
        Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
'''
arr = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print([el for el in arr if len(el) > 0])
