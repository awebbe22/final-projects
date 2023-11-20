import datetime
account = [['Date', 'Credit', 'Debit', 'Balance']]
 
def transaction():
    now = datetime.datetime.now()
    dayMonthYear = str(now.day)+'/'+str(now.month)+'/'+str(now.year)
    validInput = False
    while validInput == False:
        creditQ = input('Do you want to credit your account in this transaction? Y/N').lower()
        if (creditQ == 'y'):
            validInput = True
            credit = float(input('How much do you want to credit your account? '))
            if len(account) > 1:
                lastRow = account[len(account) - 1]
                newRow = [dayMonthYear, credit, 0, credit + lastRow[3]]
                account.append(newRow)
                print('Added ', credit, 'to your account.')
                print('Your new balance is: ', account[len(account)-1][3])
            else: 
                newRow = [dayMonthYear, credit, 0, credit]
                account.append(newRow)
                print('Added ', credit, 'to your account.')
                print('Your new balance is: ', account[len(account)-1][3])
        elif(creditQ == 'n'):
            validInput = True
        else:
            print('Please enter a valid input.')
 
    validInput = False
    while validInput == False:
        debitQ = input('Do you want to debit your account in this transaction? Y/N').lower()
        if (debitQ == 'y'):
            validInput = True
            debit = float(input('How much do you want to debit your account? '))
            if len(account) > 1:
                lastRow = account[len(account) - 1]
                newRow = [dayMonthYear, 0, debit, lastRow[3] - debit]
                account.append(newRow)
                print('Subtracted ', debit, 'from your account.')
                print('Your new balance is: ', account[len(account)-1][3])
            else: 
                newRow = [dayMonthYear, 0, debit, -debit]
                account.append(newRow)
                print('Subtracted ', debit, 'from your account.')
                print('Your new balance is: ', account[len(account)-1][3])
        elif (debitQ == 'n'):
            validInput = True
        else: 
            print('Please enter a valid input.')
    print('Thank you for the transaction. Have a nice day.')

userQuestion = input('Do you still want to run the program? Y/N ').lower()
while (userQuestion == 'y'):
    transaction()
    print('Your new account looks like this: ')
    for i in account: 
        print (i)
    userQuestion = input('Do you still want to run the program? Y/N ').lower()

    #Bubble Search
    test0 = [3, 22, 14, 434, 501, 11, 9, 1230, 304, 123, 5412, 381923, 302, -3, 1]
 
test1 = [43, 12, 7, 9, 22, 1, 104]
 
test2 = [100, 0, 0, -20, 30, -5]
 
test3  = [28, 4, 17, 666, 1001, 52, 61, 30]


def bubble_sort(list_of_numbers):
    for i in range(len(list_of_numbers)):
        for j in range(1, len(list_of_numbers)-i):
            if list_of_numbers[j-1] > list_of_numbers[j]: 
                temp = list_of_numbers[j-1]
                list_of_numbers[j-1] = list_of_numbers[j]
                list_of_numbers[j] = temp

    return list_of_numbers


print(test0)
print(bubble_sort(test0))

print(test1)
print(bubble_sort(test1))

print(test2)
print(bubble_sort(test2))

print(test3)
print(bubble_sort(test3))

#Binary Search
def binary_search(list_of_numbers, query_item):
    index_first = 0
    index_last = len(list_of_numbers)-1
    found = False

    while index_first <= index_last and not found:         
        middle_index = (index_first+index_last)//2 
        if query_item == list_of_numbers[middle_index]:   
            found = True
            break
        else:
            if query_item < list_of_numbers[middle_index]:
	            index_last = middle_index - 1 
            else:
                index_first = middle_index + 1
    
    return found


test0 = [-3, 1, 3, 9, 11, 14, 22, 123, 302, 304, 434, 501, 1230, 5412, 381923]
print(binary_search(test0, 13))

test1 = [1, 7, 9, 12, 22, 43, 104]
print(binary_search(test1, 9))
 
test2 = [-20, -5, 0, 0, 30, 100]
print(binary_search(test2, 31))
 
test3 = [4, 17, 28, 30, 52, 61, 666, 1001]
print(binary_search(test3, 666))
