import gurobipy as gp
from gurobipy import GRB

s = [55, 17, 33, 44, 23, 15, 54, 31, 7, 53, 40, 28]
mT = sum(s)
m = int(len(s)/3)
T = int(mT/m)

model = gp.Model()

x = model.addVars(len(s), m, vtype=GRB.BINARY)

model.addConstrs(gp.quicksum(x[i, j] for j in range(m)) == 1 for i in range(len(s)))
model.addConstrs(gp.quicksum(x[i, j] for i in range(len(s))) == 3 for j in range(m))
model.addConstrs(gp.quicksum(x[i, j] * s[i] for i in range(len(s))) == T for j in range(m))

model.optimize()

result = []
for i in range(m):
    result.append([])

for v in x.items():
    for k in x.keys():
        if v[0] == k:
            if v[1].X == 1:
                result[k[1]].append(s[k[0]])

print(f'\nResult of the division: {result}')
