class CustomerClass:
    def __init__(self,customerID,name,address,email,phone,member_status):
        self.__customerID=customerID
        self.__name=name
        self.__address=address
        self.__email=email
        self.__phone=phone
        self.__memberstatus=member_status

    def get_customerID(self):
        return self.__customerID
    
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_email(self):
        return self.__email
    
    def get_phone(self):
        return self.__phone
    
    def get_memberstatus(self):
        return self.__memberstatus
            
    
class TransactionClass:
    def __init__(self,date,itemname,cost,customerID):
        self.__date=date
        self.__item_name=itemname
        self.__cost=cost
        self.__customerID=customerID

    def get_date(self):
        return self.__date
    
    def get_item_name(self):
        return self.__item_name
    
    def get_cost(self):
        return self.__cost
    
    def get_customerID(self):
        return self.__customerID