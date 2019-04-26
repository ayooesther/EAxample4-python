class MpesaAccount:

	def __init__(self,name,phone):
		 self.name=name
		 self.phone=phone
		 self.balance=0
		 self.deposits=[]
		 self.withdrawals=[]
		 self.loan=0


	def check_balance(self):
		 check_balance=self.balance + amount
		 return "hellow {} ,phone number {} ,your balance is Ksh.{}".format(self.name,self.phone,self.balance)

	def deposit (self,amount):
	 	  deposit=amount
	 	  self.balance=self.balance+amount
	 	  self.deposits.append(amount)
	 	  return "welcome {},you have deposited Ksh.{},your current balance is Ksh.{}".format(self.name,amount,self.balance)

	def withdraw(self,c):

	     withdraw=c
	     if c >=self.balance:
	     	print("insufficient funds")
	     else:
	     	self.balance=self.balance-c
	     	self.withdrawals.append(c)
	     	return "welcome {} ,you have withdraw Ksh.{},your current balance is Ksh.{}". format(self.name,c,self.balance)
	 	  	 	  

	def my_deposits(self):
		 for d in self.deposits:
		 	print("the deposits {}".format(d))

	def my_withdrawals(self):
		 for e in self.withdrawals:
		 	print("the withdrawals {}".format(e))

	def give_loan(self, amount):


		loan=amount
		if len(self.deposits)>=5 and amount<1/3* sum(self.deposits) and self.loan==0:
			self.loan = self.loan + amount
			print("you can borrow a loan")
			
		else:
			print("you cant borrow a loan")

	def loan_repayment(self.cash):
		repayment=cash
		if self.loan>cash:
			self.loan = self.loan -cash
			customer= "heloo{} ,you have paid a loan of {} your loan balance is{}" .format(self.name,amount,self.loan)

		elif self.loan<cash:
			over_payment=cash-self.loan
			self.balance=self.balance-self.loan
			self.balance=self.balance+over_payment
			customer=" heloo {} ,you have paid your loan fully, you have paid ksh {} your over_repayment has been added to your balance of ksh{}" .format(self.name,cash,self.balance))
        else 
            print("not available")
			


