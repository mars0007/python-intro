#1.  given: pets = {'bird':3.5,'cat':5.0,'dog':7.25,'gerbil':1.5} <-- load it from a file pet.txt
#    ask user for a pet and give them the price
#    if invalid pet is selected let the user pick agin


pets = {}

with open("pets.txt") as in_file:
    for line in in_file:
        line = line.strip()
        pet_line = line.split(':')
        pet = pet_line[0]
        price = pet_line[1]
        pets[pet] = float(price)

pet_name=''

while True:
    pet_name = input('Please enter pet for costing, or quit to exit:')
    if pet_name == 'quit':
        print("quiting...")
        break
    elif pet_name not in pets.keys():
        print('we don\'t have that pet, please pick agin')
    else:
        print('{0} costs {1}'.format(pet_name,pets[pet_name]))
    