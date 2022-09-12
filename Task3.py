"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

"""
Pseudocode:
1. create empty list to hold unique codes.
2. initiate counter of incoming calls from numbers starting with "(080)"
3. initiate counter of incoming calls from numbers starting with "(080)" to
        answering numbers also starting with "(080)"
4. for each record in calls:
        a. Extract incoming and answering numbers from current record.
        b. Extract code from incoming and answering numbers.
        c. Insert answering code into unique codes list if not already exists.
        d. If incoming code is 080, increment incoming_fixed_counter.
        e. If incoming and answering codes are 080, increment both_fixed_counter.
5. calculate percentage of 080 calls.
6. print results.
"""

import re


def search_area_code(number):
    """
    Search for area code in the input number
    """
    # Search for area code
    ar_code = re.match("^\(0\d*\)", number)
    if ar_code:
        ar_code = ar_code.group()
        # Remove parentheses
        ar_code = ar_code[1:-1]
        return ar_code
    else:
        return None


def search_mobile_code(number):
    """
    Search for mobile code in the input number
    """

    # Search for mobile number code along with the following digit and space
    mob_code = re.match("^(7|8|9)\d{4}\s", number)
    if mob_code:
        mob_code = mob_code.group()
        # Remove last digit and the following space
        mob_code = mob_code[:-2]
        return mob_code
    else:
        return None


def search_telemarketers_code(number):
    """
    Search for telemarketers code in the input number
    """
    # Search for Telemarketers code
    tele_code = re.match("^140", number)
    if tele_code:
        tele_code = tele_code.group()
        return tele_code
    else:
        return None


def extract_number_code(number):
    """
    Extract the code of the input number
    """

    # Search for area code in answering number
    area_code = search_area_code(number)

    if area_code:
        return area_code
    else:
        # Search for mobile number code in answering number
        mobile_code = search_mobile_code(number)

    if mobile_code:
        return mobile_code
    else:
        # Search for Telemarketers code in answering number
        telemarketers_code = search_telemarketers_code(number)

    if telemarketers_code:
        return telemarketers_code


def append_unique_item(input_list, input_item):
    """
    Append an input item to a list if it isn't already there, then return
    the new resulted list.
    """

    if input_item not in input_list:
        input_list.append(input_item)

    return input_list


def main(calls_list):
    codes_list = []
    incoming_fixed_counter = 0
    both_fixed_counter = 0

    for record in calls_list:

        record_incoming = record[0]
        record_answering = record[1]

        incoming_code = extract_number_code(record_incoming)
        answering_code = extract_number_code(record_answering)

        # Append found answering code to codes list
        codes_list = append_unique_item(codes_list, answering_code)

        if incoming_code == '080':
            incoming_fixed_counter += 1

        if incoming_code == '080' and answering_code == '080':
            both_fixed_counter += 1

    # Fixed Percentage
    fixed_percentage = (both_fixed_counter / incoming_fixed_counter) * 100

    # Fixed Percentage with two decimal digits
    fixed_percentage = '{:.2f}'.format(fixed_percentage)

    # Sort codes list in Lexicographic order (sort in place)
    codes_list.sort()

    # Print part1 results
    print("The numbers called by people in Bangalore have codes:")
    for code in codes_list:
        print(code)

    # Print part2 results
    print(
        "{0} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
            fixed_percentage))


if __name__ == '__main__':
    main(calls_list=calls)
