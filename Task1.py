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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def append_unique_item(input_item, input_list):
    """
    Append an input item to a list if it isn't already there, then return
    the new resulted list.
    """

    if input_item not in input_list:
        input_list.append(input_item)

    return input_list


def count_unique_numbers(texts_list, calls_list):
    # Initiate an empty list to hold all different telephone numbers
    unique_numbers_list = []

    # Add numbers from texts records
    for record in texts_list:
        incoming_number = record[0]
        append_unique_item(incoming_number, unique_numbers_list)

        answering_number = record[1]
        append_unique_item(answering_number, unique_numbers_list)

    # Add numbers from calls records
    for record in calls_list:
        incoming_number = record[0]
        append_unique_item(incoming_number, unique_numbers_list)

        answering_number = record[1]
        append_unique_item(answering_number, unique_numbers_list)

    numbers_count = len(unique_numbers_list)

    print("There are {0} different telephone numbers in the records.".format(
        numbers_count))

    return numbers_count


if __name__ == '__main__':
    count_unique_numbers(texts_list=texts, calls_list=calls)
