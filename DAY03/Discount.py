def calculate_total(cart):
    total=sum(cart.values())
    if total>2000 and total<5000:
        total*=0.1
    if total>=5000:
        total*=0.15
    return total


cart={'laptop':500,'headphones':2000,'mouse':3500,'keyboard':1500,'monitor':8000,'USB drvie':1000}
print(f"cart items:{cart}")
print(f"total price:{calculate_total(cart)}")
