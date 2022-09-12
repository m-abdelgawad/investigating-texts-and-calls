"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone 
during September 2016.".
"""


def print_longest_time(calls_list):
    # Create a list of dictionaries to hold the numbers and their total calls
    # duration during September 2016.
    numbers_dict = {}

    # Loop over the calls re cords
    for record in calls_list:

        # Extract the record timestamp
        record_timestamp = record[2]

        # Extract the month of the record timestamp
        record_month = record_timestamp[3:5]

        # Extract the year of the record timestamp
        record_year = record_timestamp[6:10]

        # Check if the current record occurred at September 2016
        if record_month == '09' and record_year == '2016':

            # Extract the incoming number
            incoming_number = record[0]

            # Extract the answering number
            answering_number = record[1]

            # Extract current record duration
            duration = int(record[3])

            # Check if the incoming number already exists in the
            # numbers_dict dictionary
            if incoming_number in numbers_dict.keys():
                # If it exists, increment the duration
                numbers_dict[incoming_number] += duration
            else:
                # If it doesn't exist, add it with the current duration
                numbers_dict[incoming_number] = duration

            # Do the same for the answering number

            # Check if the answering number already exists in the
            # numbers_dict dictionary
            if answering_number in numbers_dict.keys():
                # If it exists, increment the duration
                numbers_dict[answering_number] += duration
            else:
                # If it doesn't exist, add it with the current duration
                numbers_dict[answering_number] = duration

    # Extract the longest duration and the number from the numbers_dict
    # dictionary
    longest_number = max(numbers_dict, key=numbers_dict.get)
    longest_duration = numbers_dict[longest_number]

    print(
        "{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(
            longest_number, longest_duration))


if __name__ == '__main__':
    print_longest_time(calls_list=calls)
