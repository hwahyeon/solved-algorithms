'''
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
'''

def create_phone_number(n):
    return '(' + ''.join(map(str, n[:3])) + ') ' + ''.join(map(str, n[3:6])) +'-'+ ''.join(map(str, n[6:]))
