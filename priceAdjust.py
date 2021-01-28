#import Price
#... Price ('20000', 'MSRP')
#MSRP 20000

#Price('15000', 'Black')
#Black 15000

#Price('19600', 'White')
#White 19600

#Price('14500', 'Veteran')
#Veteran 14500

def discountCalc(n1, n2):
    discount = n1 * n2
    return discount

# if car is black
print(discountCalc(20000, .25)) # discount if black

# if car is white
print(discountCalc(20000, .02)) # discount if white

# if customer is veteran
#print (discountCalc(20000, .725)) # discount if veteran

#if MSRP
print (discountCalc(20000)) # MSRP

