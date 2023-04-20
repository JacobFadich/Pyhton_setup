def hello()
    print('Greetings')

hello()

def pack(one,two,three):
    return [one,two,three]

print(pack('clothes','charger','computer'))

def eat_lunch(lunch):
  if len(lunch) == 0:
    print("My lunchbox is empty!")
  else:
    for x in range(len(lunch)):
      if x == 0:
        print(f"First I eat {lunch[0]}")
      else:
        print(f"Next I eat {lunch[x]}")

eat_lunch(['pizza'])