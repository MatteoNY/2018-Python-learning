
# using defaults keywork args order by name
# input()

# global variables
MINING_REWARD = 10

genisis_block = {
        'previous_hash': '', 
        'index': 0,
        'transactions': []  
    }
blockchain = [genisis_block]
open_transactions = []
owner = "Chase"
participants = {'Chase', 'Cooper'}
 
name = 'mc'
age = 29

def hash_block(block):
    # list comprehension shortcut approach does the same thing in one-line
    return  '-'.join([str(block[key]) for key in block])

def get_balance(participant):
    # list comprenhension wild stuff
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain ]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            # print ('tx? in block...', tx)
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain ]
    amount_received= 0
    for tx in tx_recipient:
        if len(tx) > 0:
            # print ('tx? in block...', tx)
            amount_received += tx[0]        
    return amount_received - amount_sent 

def get_last_blockchain_value():
    """ Returns the last value ofthe current blockchain """
    global name
    name = 'Matteo'
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def verify_transaction(transaction):
    


def add_transaction(recipient, sender=owner, amount=1.0):
    """ appends the new value to current blockchain 

    Arguments:
        sender: sender of the coins
        recipient: the recipient of the coins.
        amount: sent in transaction default 1

    """
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transactions.append(transaction)
    # adding will only add unique values to the set no dups :-)
    participants.add(sender)
    participants.add(recipient)
    

def mine_block():
    # pass is used for stub 
    # pass
    last_block = blockchain[-1]
    # list comprehension shortcut approach does the same thing in one-line
    # hashed_block = str([last_block[key] for key in last_block])
    hashed_block = hash_block(last_block)
    reward_transaction = {
      "sender" : 'MINING',
      'recipient': owner,
      'amount' :  MINING_REWARD
    }
    open_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block, 
        'index': len(blockchain),
        'transactions': open_transactions  
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    
    tx_recipient = input('Enter recipient of transaction: ')
    txt_amount = float(input('Your tranaction amount please: '))
    # return truple
    return (tx_recipient, txt_amount)


def get_user_choice():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in user_input
    user_input = input('Your choice: ')
    return user_input  


# Get the first transaction input and add the value to the blockchain
# tx_amount = get_transaction_value()
# add_value(tx_amount)


def print_blockchain_elements():
    # for loop
    for block in blockchain:
        print('for loop output - blockchain')
        print(block)
    else:
        print ('-' * 20)

# def verify_chain():
#     for (index, block) in enumerate(blockchain):
#         if block == 0:
#             continue
#         if block['previous_hash'] != hash_block(blockchain[index -1]):
#             return False
#     return True

def verify_chain():
    """ Verify the current blockchain and return True if it's valid, False otherwise."""
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


waiting_for_input = True

while waiting_for_input:
    print ('Please choose')
    print ('1: add transation')
    print ('2: mine new block')
    print ('3: end and print output')
    print ('4: output participants')
    print ('h: modify')
    print ('q: to quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        txt_data = get_transaction_value()
        recipient, amount = txt_data
        # sender is owner is set globally and by default
        add_transaction(recipient, amount=amount)
        print('open?', open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print('participants:', participants)
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] =  {
                'previous_hash': '', 
                'index': 0,
                'transactions': [{'sender': 'Howdy', 'recipient': 'ZZ', 'amount': 100.0}]  
            }
    elif user_choice == 'q':
        # you can also use break or continue 
        waiting_for_input = False
    else:
        print ('error: input was invalid, please enter a value from the list!')
    if not verify_chain():
        print_blockchain_elements()
        print ('invalid blockchain!')
        break
    print ('balance', get_balance('Chase'))
else:
    print ('user left and is done!')


if name == 'mc' and (age > 20 or age < 30):
    print ('ciao Matteo -- cool age ', age ) 


print('************ global name is ' + name)
print('keyword arguments')


def greet(name, favfood):
    print('mi chiamo: ' + name + " fav food ", favfood)

# function is by name
greet(favfood='pizza', name='howdy')



print('finito!')