t1 = [1, 2]
t2 = t1.append(3)
print(t1)
#[1, 2, 3]
print(t2)
#None
t3 = t1 + [3]
print(t3)
#[1, 2, 3]
t2 is t3
#False
