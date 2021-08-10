std = {'Vasiliy':[2,3,5], 'Alex':[4,5,4], 'Dmitriy':[4,3,5]}
beststd = []
badstd = []
for stud in std.values():
    x = sum(stud)/len(stud)
    print (x,)


