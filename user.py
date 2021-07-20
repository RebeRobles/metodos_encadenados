class User:
    def __init__(self, username, email_address):
        self.name = username			
        self.email = email_address		
        self.account_balance = 0

# agrega el método depósito 
    def make_deposit(self, amount):	
        self.account_balance += amount
        return self

# agrega el método de retiro de fondos 
    def make_withdrawal(self, amount):
        if amount > self.account_balance:
            print('No existe saldo suficiente para su retiro')
        else:
    	    self.account_balance -= amount
        return self

#agrega el método que muestra el saldo
    def display_user_balance(self):
        return f'Usuario: {self.name}, Saldo: $  {self.account_balance}' 

#agrega el método que muestra transferencia a otro usuario
    def transfer_money (self, other_user, amount):
        self.make_withdrawal(amount)
        if self.account_balance > amount:
            other_user.make_deposit(amount)
        else:
            print(f'Saldo insuficiente para efectuar transferencia')
        other_user.display_user_balance()
        self.display_user_balance()
        return self      


user1 = User('Bruce Dickinson', 'bruce@ironmaiden.com')
user1.make_deposit(2000).make_deposit(200).make_deposit(500).make_withdrawal(5000).display_user_balance()

user2 = User('Colin Firth', 'cfirth@kingsman.com')
user2.make_deposit(100).make_deposit(1000).make_withdrawal(900).make_withdrawal(100).display_user_balance()

user3 = User('Chris Martin', 'cmartin@coldplay.uk')
user3.make_deposit(10000).make_withdrawal(1500).make_withdrawal(500).make_withdrawal(300).display_user_balance()

user1.transfer_money(user2, 199)
print(user1.display_user_balance())
print(user2.display_user_balance())
print(user3.display_user_balance())