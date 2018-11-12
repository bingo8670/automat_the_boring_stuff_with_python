while True:
   print('Who are you?')
   name = raw_input()
   if name != 'Joe':
       continue
   print('Hello, Joe. What is the password? (It is a fish.)')
   password = raw_input()
   if password == 'swordfish':
       break
print('Access granted.')
