# write a code to check whether th ewater is hot or cold
#real scenario: the input is received fromt eh thermometert o intert via IOT and the value is fee, for now we use dummy value
# house 2 million
#if buyer has good credit and high income - give down 10%
#if buyer has bad credit - give down 20%
# print down payment

house_cost =1000000
credit_good =True
income_good =True
has_criminal_record =False

if credit_good and income_good and not has_criminal_record:
    down_payment =house_cost*0.1
    print(f"Downpayment to be paid is ${down_payment}")

else:
    #down_payment =house_cost*0.2
    print("Not eligible for loan")
#print("Downpayment to be paid is " + str(down_payment))
