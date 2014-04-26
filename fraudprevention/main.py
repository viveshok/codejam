
import sys

N = int(sys.stdin.readline())

frauds = list()

# two hashmaps:
# keys: (dealID, email), values: (recordID, credit card #)
emails = dict()
# keys: (dealID, address), values: (recordID, credit card #)
addresses = dict()

# loop through the records
for i in range(N):
    record = sys.stdin.readline().lower().split(',')
    (oID, dID, email, street, city, state, zipcode, card) = tuple(record)

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
    archive = emails.get((dID, email))
    if archive and archive[1] != card:
        frauds.append(archive[0])
        frauds.append(int(oID))
    else:
        emails[(dID, email)] = (int(oID), card)

    # Check for fraud type 2
    archive = addresses.get((dID, address))
    if archive and archive[1] != card:
        frauds.append(archive[0])
        frauds.append(int(oID))
    else:
        addresses[(dID, address)] = (int(oID), card)

frauds = [str(x) for x in sorted(list(set(frauds)))]
print(','.join(frauds))

