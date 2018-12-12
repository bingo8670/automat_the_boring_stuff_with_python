import random,logging
logging.basicConfig(level=logging.DEBUG, format=('%(asctime)s--%(levelname)s--%(message)s'))
# logging.disable(logging.DEBUG)
logging.debug('\n============start of debug============')
guess = ''
while guess not in ('heads','tails'):
    guess = input("Guess the coin toss!Enter heads or tails: \n")
    logging.debug('you input is:' + str(guess))
toss = ['heads','tails']
tossRandom = toss[random.randint(0,1)]#0为tails ,1为heads
# print("coin is :", tossRandom)
logging.debug('toss is (0 is tails and 1is heads):'+tossRandom)
if tossRandom == guess:
    print("you got it")
else:
    guess = input("nope!guess again:")
    logging.debug('you input is:' + str(guess))
    if guess not in ('heads','tails'):
        print("Guess the coin toss!Enter heads or tails")
        logging.debug('you input is:' + str(guess))
    elif toss == guess:
        print("you got it ")
        logging.debug('you got it')
    else:
        print("Nope! you are really bad at this game")
        logging.debug("Nope! you are really bad at this game")
logging.debug('\n============end of debug============')
