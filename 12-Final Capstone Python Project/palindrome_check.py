# this is a program that checks
# if the inputted string is a 
# palindrome

# get the user to enter a string

# reverse it and compare it to the entered string

# let the user know the results

# ask if they want to play again

again = None
while again != 'n':
    str_in = input('Please enter a word or phrase to check: ')
    str_rev = str_in[::-1]

    if str_rev == str_in:
        print('\nYes! ' + str_in + ' is a palindrome!')
    elif str_rev != str_in:
        print('\nSorry, ' + str_in + ' is not a palindrome.')
    else:
        print('\nOops, something went wrong.')

    again = input('Would you like to try another? y/n').lower()

