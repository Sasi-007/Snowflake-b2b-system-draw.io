from random import randint, randrange
import random
from datetime import datetime
import first_last_gen
number_of_tickets=8
max_no_of_tickets=5
def num_gene():
    bought_tickets=randrange(1,max_no_of_tickets)
    return bought_tickets
bought_tickets=num_gene()
def again():
    transaction_id=randrange(113535343445,156865567423)
    event_names=(
        'Movie',
        'Dance',
        'Music',
        'Games',
        'Standup comedy'
    )
    event_name=random.choice(event_names)
    vendor_ticket_amount=bought_tickets*100
    vendor_ticket_amount=f'₹{vendor_ticket_amount}'
    sales_channel='Vendor'
    customer_first_name=first_last_gen.name()
    customer_last_name=first_last_gen.name()
    office_locs=(
        'Chennai',
        'Trichy',
        'Salem',
        'Mysore',
        'New Delhi',
        'Sri lanka'
    )
    office_loc=random.choice(office_locs)
    line="("+str(transaction_id)+","+"'"+event_name+"'"+","+str(bought_tickets)+","+"'"+vendor_ticket_amount+"'"+","+"'"+sales_channel+"'"+","+"'"+customer_first_name+"'"+","+"'"+customer_last_name+"'"+","+"'"+office_loc+"'"+","+"current_timestamp()"+")"+","
    print(line)
for i in range(0,number_of_tickets,bought_tickets):
    print(i)
    again()