print ("-----리스트컴프리헨션----")
lst = list(range(1,11))
print( [i**2 for i in lst if i > 5])
tp = ("apple", "banana", "orange")
print([len(i) for i in tp])
d = { 100:"apple", 200:"kiwi"}
print( [v.upper() for v in d.values()])
