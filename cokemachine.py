#coke machine

#handling valid inserts(25,10,5)
def valid_coin(due):#valid coin function
    while True:
      coin=int(input("Insert Coin:")) #25  #taking coins from user
      if coin in [25,10,5]:
        return coin
      else:
        print(f"Amount due: {due}") #keep showing amount due until getting right coins


#calculate due
def calculate_due(due,coin):
  due=due-coin #(50-25)
  return due #25
"""valid_coin and due functions will be used in our main coke machine function"""

def coke_machine():
  due=50

  while due>0: #the loop will run till the due is greater than 0
    print("Amount due:", due) #50   #showing amount due:50
    insert = None
    while insert is None:
      insert = valid_coin(due)  #25 #calling valid coin function and getting insert coin
    due = calculate_due(due, insert) #(50,25) #passing due and coin and calculating due
    #due=25
    if due==0:
        print("user owed:0") #when the due becomes 0 or it reaches 50
        break

    elif due<0:  #if exceed 50 cents
      over=-due
      print("user owed:",over) #showing the overdue amount
      break



coke_machine() #we're calling only coke machine function
#case study
#due=50,ins=25->due=25,ins=10->due=15,ins=10->due=5,ins=5->user owed 0
#due=50,ins=25->due=25,ins=10->due=15,ins=10->due=5,ins=10->user owed 5
#due=50,ins=25->due=25,ins=30->due=50
