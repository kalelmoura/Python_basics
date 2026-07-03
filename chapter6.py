#script 1
# cat_names = []
# while True:
#     print('Enter the name of cat ' + str(len(cat_names) + 1) +
#       ' (Or enter nothing to stop.):')
#     name = input()
#     if name == '':
#         break
#     cat_names = cat_names + [name]  # List concatenation
# print('The cat names are:')
# for name in cat_names:
#     print('  ' + name)

# sript 2
# import random, sys, time

# WIDTH = 70  # The number of columns

# try:
#     # For each column, when the counter is 0, no stream is shown.
#     # Otherwise, it acts as a counter for how many times a 1 or 0
#     # should be displayed in that column.
#     columns = [0] * WIDTH 
#     while True:
#         # Loop over each column:
#         for i in range(WIDTH):
#             if random.random() < 0.02:
#                 # Restart a stream counter on this column.
#                 # The stream length is between 4 and 14 characters long.
#                 columns[i] = random.randint(4, 14)

#             # Print a character in this column:
#             if columns[i] == 0:
#                 # Change this ' '' to '.' to see the empty spaces:
#                 print(' ', end='')
#             else:
#                 # Print a 0 or 1:
#                 print(random.choice([0, 1]), end='')
#                 columns[i] -= 1  # Decrement the counter for this column.
#         print()  # Print a newline at the end of the row of columns.
#         time.sleep(0.1)  # Each row pauses for one tenth of a second.
# except KeyboardInterrupt:
#     sys.exit()  # When Ctrl-C is pressed, end the program.

# practice questions
# spam = ['apples', 'bananas', 'tofu', 'cats']

# def list_to_string(lists):
#     result = "result: "
#     for i in range(len(lists)):
#         if i == len(lists) - 1:
#             result = result + " and " + lists[i]
#         elif i == len(lists) - 2:
#               result = result + lists[i]  
#         else:
#             result = result + lists[i] + ", "
#     print(result)

# list_to_string(spam)