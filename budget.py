class Category:

    def __init__(self, categories, ledger = []):
        
        self.categories = categories
        self.ledger = list()

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        return self.ledger

    def withdraw(self, amount_w, msg =""):
        if amount_w > self.ledger[0]["amount"]:
            return False
        else: 
            self.ledger[0]["amount"] = self.ledger[0]["amount"] - amount_w
            print(msg)
            return True

    def get_balance(self):
        data = self.ledger[0]
        for i in data:
            print(data[i])
    
    def transfer(self, amount, obg_name):
        obg_name = obg_name.categories
        a = self.withdraw(amount, f"Transferir a {obg_name}")
        b = self.deposit(amount, f"Transferido desde {self.categories}")
        if(a==True):
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.ledger[0]["amount"]:
            return False
        return True

#Obtiene una lista
def create_spend_chart(categories):
    for i in categories:
        print("categoría:", i)
        print("balance: ")
        i.get_balance()
    
food = Category("Food")
print(food.deposit(1000, "initial deposit"))
food.withdraw(10.15)
food.withdraw(15.89, "restaurant and more food for dessert")
food.get_balance()
