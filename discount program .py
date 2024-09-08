## discount program vala
def discount(cost,d):
    sum=cost-(cost*(d/100))
    return sum
cost=int(input())
d=int(input())
print(discount(cost,d))
