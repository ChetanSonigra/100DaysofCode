print('Welcome to the tip calculator!')
bill = float(input('What was the total bill? $'))
tip = int(input('How much tip you would like to give? 10, 12 or 15?'))
split_people= int(input('How many people to split the bill?'))
bill_per_person = bill*(1+tip/100)/split_people
print(f'Each people should pay: ${bill_per_person:.2f}')
# or "{:.2f}".format(res)
