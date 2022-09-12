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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order 
with no duplicates.
"""

"""
Pseudocode:
1. create empty list to hold telemarketers numbers.
2. create empty list to hold unique incoming calls numbers.
3. create empty list to hold unique answering calls numbers.
4. create empty list to hold unique incoming text numbers.
5. create empty list to hold unique answering text numbers.
6. for each number in incoming calls numbers:
    append number to telemarketers list if number doesn't already exist and
    not in the following lists:
        a. answering calls numbers.
        b. incoming text numbers.
        c. answering text numbers.
7. print results.
"""


def append_unique_item(input_list, input_item):
    """
    Append an input item to a list if it isn't already there, then return
    the new resulted list.
    """

    if input_item not in input_list:
        input_list.append(input_item)

    return input_list


def identify_telemarketers(calls_list, texts_list):
    telemarketers_list = []
    incoming_call_list = []
    answering_call_list = []
    incoming_text_list = []
    answering_text_list = []

    # Fill both lists: incoming_call_list and answering_call_list
    for record in calls_list:
        incoming_call = record[0]
        incoming_call_list = append_unique_item(incoming_call_list,
                                                incoming_call)
        answering_call = record[1]
        answering_call_list = append_unique_item(answering_call_list,
                                                 answering_call)

    # Fill both lists: incoming_call_list and answering_call_list
    for record in texts_list:
        incoming_text = record[0]
        incoming_text_list = append_unique_item(incoming_text_list,
                                                incoming_text)
        answering_text = record[1]
        answering_text_list = append_unique_item(answering_text_list,
                                                 answering_text)

    # Detect telemarketers numbers
    for number in incoming_call_list:
        if number not in answering_call_list and \
                number not in incoming_text_list and \
                number not in answering_text_list:
            telemarketers_list = append_unique_item(telemarketers_list, number)

    # Print Results:
    print("These numbers could be telemarketers: ")
    for number in sorted(telemarketers_list):
        print(number)


if __name__ == '__main__':
    identify_telemarketers(calls_list=calls, texts_list=texts)
