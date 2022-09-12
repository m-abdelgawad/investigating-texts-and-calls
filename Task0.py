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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at 
time <time>".
"Last record of calls, <incoming number> calls <answering number> at 
time <time>, lasting <during> seconds".
"""


def print_first_text(texts_list):

    # First Text Record
    first_text = texts_list[0]

    # The incoming number of the first text record
    first_text_incoming = first_text[0]

    # The answering number of the first text record
    first_text_answering = first_text[1]

    # The timestamp of the first text record
    first_text_timestamp = first_text[2]

    # Print the results of the first text record
    print("First record of texts, {0} texts {1} at time {2}".format(
        first_text_incoming, first_text_answering, first_text_timestamp))


def print_first_call(calls_list):

    # Last Call Record
    last_call = calls_list[-1]
    last_call_incoming = last_call[0]
    last_call_answering = last_call[1]
    last_call_timestamp = last_call[2]
    last_call_duration = last_call[3]

    # Print the results of the first call record
    print(
        "Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds".format(
            last_call_incoming, last_call_answering, last_call_timestamp,
            last_call_duration))


if __name__ == '__main__':
    print_first_text(texts)
    print_first_call(calls)
