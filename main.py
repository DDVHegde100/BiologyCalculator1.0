print("Welcome to Dhruv's Biology Calculator")
bio=str(input('Enter the calculation(no capital letters(single word)): '))

if(bio=='ph'):
    concentration=float(input('Enter the hydrogen concentration:'))
    ph=-log(concentration)
    print('%0.3f is the pH.' %(ph))
