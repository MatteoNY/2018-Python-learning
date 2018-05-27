
# using defaults keywork args order by name
# input()

# global variables
blockchain = []
name = 'mc'


def get_last_blockchain_value():
    """ Returns the last value ofthe current blockchain """
    global name
    name = 'Matteo'
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ appends the new value to current blockchain 

    Arguments:
        transaction_amount, # the amount to be added
        last_transaction # the last blockchain value

    """
    blockchain.append([last_transaction, transaction_amount])
    # print(blockchain)


def get_user_input():
    return float(input('Your transaction amount please: '))


add_value(get_user_input())
# using keyword arguments
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=get_user_input())

add_value(get_user_input(), get_last_blockchain_value())


print('using default')
print(blockchain)
print('global name is ' + name)

print('keyword arguments')


def greet(name, favfood):
    print('mi chiamo: ' + name + " fav food ", favfood)


# function is by name
greet(favfood='pizza', name='howdy')
