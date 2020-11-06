# python3.6
# coding: utf-8
# store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
# store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
insulin = bInsulin + aInsulin

pKR = {}
pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53,
       'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}

# counting how many amino acids are in insulin are "Y"
insulin.count("Y")
float(insulin.count("Y"))
seqCount = ({x: float(insulin.count(x))
             for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']})


# creating variable & initializing it to zero
pH = 0
  # Writing net change formula
netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x])))
           for x in ['k', 'h', 'r']}.value()))lseek(fd, pos, how)
    - (sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x])))
            for x in ['y', 'c', 'd', 'e']}.value())))
while(pH <= 14):
    print('0:.2f}'.format(pH),netCharge)
    pH += 1
    