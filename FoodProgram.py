import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}

order_total = 0

#customer1=fc.CustomerClass(570,'Danni Sellyar','97 Mitchell Way Hewitt Texas 76712','dsellyarft@gmpg.org','254-555-9362',False)
customer1=fc.CustomerClass(569,'Aubree Himsworth','1172 Moulton Hill Waco Texas 76710','ahimsworthfs@list-manage.com','254-555-2273',True)

print(f"Customer Name: {customer1.get_name()}")
print(f"Phone: {customer1.get_phone()}")
for key in dict:
    trans=fc.TransactionClass(dict[key][0],dict[key][1],dict[key][2],dict[key][3])
    if customer1.get_customerID()==trans.get_customerID():
        print(f"Order Item: {trans.get_item_name()}  Price: ${format(trans.get_cost(), '.2f')}")
        cost=dict[key][2]
        order_total+=cost

if customer1.get_memberstatus()==True:
    disc=order_total*.20
    totalcost=order_total-disc
    print(f"Total Cost: ${format(order_total, '.2f')}")
    print(f"Member Discount: ${format(disc, '.2f')}")
    print(f"Total Cost after discount: ${format(totalcost, '.2f')}")
else: 
    print(f"Total Cost: ${format(order_total, '.2f')}")
    
    