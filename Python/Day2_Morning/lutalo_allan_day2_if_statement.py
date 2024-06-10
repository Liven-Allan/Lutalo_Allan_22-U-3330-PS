#children under 13 years, discount for price shs 1000
#Teenagers between 13 and 18 years, discount for price she 500
# Adults 18 years and above, pay full price shs 2000
# Senior citizens 65 years above, pay shs 5000  

#Using if,elif,else statements 

price = 2000
age = int(input("Enter your age to determine movie price: "))

if age < 13:
    final_price = price - 1000
    print("Movie price for children : shs" + str(final_price))

elif age >= 13 and age < 18:
    final_price = price - 500
    print("Movie price for teenagers: shs" + str(final_price))

elif age >= 18 and age < 65:
    print("Movie price for adults: shs" + str(price))

else:
    final_price = price + 3000
    print("Movie price for senior citizens: shs" + str(final_price))        