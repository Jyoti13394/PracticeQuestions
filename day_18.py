import datetime
# Reverse list

def reverse(list_1):
    reversed_list = sorted(list_1, reverse=True)
    return reversed_list


list_1 = [66, 67.34, 90, 67, 35, 78, 57]

print(reverse(list_1))

# DATE TIME MODULE

today_date = datetime.datetime.today().date()

todays_date = datetime.datetime.today()
formatted_date = todays_date.strftime('%Y-%m-%d-%H-%M-%S')
print(todays_date)
print(today_date)
print(formatted_date)

