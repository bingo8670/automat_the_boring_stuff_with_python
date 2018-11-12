import sys
while True:
    print('Type exit to exit.')
    response = raw_input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
