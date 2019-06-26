A = dict(zip(('a','b','c'),(1,2,3))) # tuples
print(A)
for i,j in enumerate(A):
    print(j,i)
A2 = range(10)
print(A2)

Output:-
{'c': 3, 'b': 2, 'a': 1}                                                                                              
c 0                                                                                                                   
b 1                                                                                                                   
a 2                                                                                                                   
range(0, 10)
