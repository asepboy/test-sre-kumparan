def test04(n):
  for n in range(1, n+1):
    if n % 3 == 0 and n % 5 == 0:
        print('KumParan')
    elif n % 3 == 0:
        print('Kum')
    elif n % 5 == 0:
        print('Paran')
    else:
        print(n)

test04(100)