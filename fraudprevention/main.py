
import sys
import collections

N = int(sys.stdin.readline())

frauds = list()

emails = collections.defaultdict(set)
addresses = collections.defaultdict(set)

class ID():
    def __init__(self, oID, card_):
        self.orderID = oID
        self.card = card_

    def __hash__(self):
        return self.card

# loop through the records
for i in range(N):
    record = sys.stdin.readline().lower().split(',')
    (oID, dID, email, street, city, state, zipcode, card) = tuple(record)

    oID = int(oID)
    card = int(card)

    # process email
    (prefix, suffix) = tuple(email.split('@'))
    prefix = prefix.replace('.','')
    prefix = prefix.split('+')[0]
    email = prefix + '@' + suffix

    # process address
    street = street.replace('street', 'st.').replace('road', 'rd.')
    state = state.replace('illinois', 'il').replace('california', 'ca').replace('new york', 'ny')
    address = street + city + state + zipcode

    # Check for fraud type 1
    if emails[(dID, email)].difference([card]):
        frauds.append(oID)
        frauds.extend([x.orderID for x in emails[(dID, email)]])

    # Check for fraud type 2
    if addresses[(dID, address)].difference([card]):
        frauds.append(oID)
        frauds.extend([x.orderID for x in addresses[(dID, address)]])

    emails[(dID, email)].add(ID(oID, card))
    addresses[(dID, address)].add(ID(oID, card))

frauds = [str(x) for x in sorted(list(set(frauds)))]
print(','.join(frauds))

