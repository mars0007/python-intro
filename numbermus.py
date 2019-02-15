# function that conversts roman digits into arabic digits
def to_num(letter):
    mapping= {'i' : 1, 'v' : 5, 'x' : 10, 'l' : 50, 'c' : 100, 'm' : 1000}
    return mapping[letter]

# loop the roman numberal and add it up  
def roman_to_arabic(roman_number):
    arabic_number = 0
    previous_digit = 0
    # add the value of the roman digit to the number
    for n in roman_number:
        arabic_number += to_num(n)
        # however if the previous digit was there to substract from the current substrat it's value x 2 
        # one to couter act the addioton in the previous iteration and second to actualy substract it 
        if previous_digit < to_num(n):
            arabic_number -= previous_digit*2
        previous_digit = to_num(n)
    return arabic_number         

the_roman_number='mmxix'

print("roman number {0} in arabic number is {1}".format(the_roman_number,roman_to_arabic(the_roman_number)))