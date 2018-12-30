
import datetime

answer_format = '%m/%d'
link_format = "%b_%d"
link = 'https://en.wikipedia.org/wiki/{}'

while True:
    answer = input("what date would you like? Please use the MM/DD format. Enter 'quit' to exit.")
    if answer.upper() == 'QUIT':
        break
    try:
        date = datetime.datetime.strptime(answer, answer_format)
        output = link.format(date.strftime(link_format))
        print(output)
    except ValueError:
        print("That's not a valid date. Please try again")

# import datetime
# date_str = '29/12/2017' # The date - 29 Dec 2017
# format_str = '%d/%m/%Y' # The format
# datetime_obj = datetime.timedelta.strptime(date_str, format_str)
# print(datetime_obj.date())




# # https://ugoproto.github.io/ugo_py_doc/Datetime/



import datetime

answer_format = '%m/%d'
link_format = '%b_%d'
link = 'https://en.wikipedia.org/wiki/{}'

while True:
    answer = input("What date would you like? Please use the MM/DD format. Enter 'q' to quit.")
    answer2 = str(answer)
    if answer2.upper() == 'Q':
        break

    try:
        date = datetime.datetime.strptime(answer, answer_format)
        output = link.format(date.strftime(link_format))
        print(output)
        file = open('output.txt', 'w')
        file.write(output)
        file.close()
    except:
        print("That's not a valid date. Please try again.")
        break