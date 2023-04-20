import logging as lg
lg.basicConfig(level=lg.INFO)
a=10
lg.info("First Number value taken")
b=9
lg.info("Second Number value taken")
try:
    a=a/b
    lg.info("Division operation done")
    print(a)
except Exception as e:
    print("Divison not possible")
    lg.error(f"{a}/{b} is not possible",exc_info=False)
lg.info("EOF") 
