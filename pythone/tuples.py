thistuple=("mandazi","bread","cake")

# print(thistuple)

# print(thistuple[1])

x=("mandazi","bread","cake")
y=list(x)
y[1]="donut"
x=tuple(y)
# print(x)

y=list(thistuple)
y.remove("mandazi")
thistuple=tuple(y)
# print(y)

y=list(thistuple)
y.append("colour")
thistuple=tuple(y)
print(y)
