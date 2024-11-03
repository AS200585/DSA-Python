"""
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
"""

month_expense = [2200, 2350, 2600, 2130, 2190]
month_name = ["January", "February", "March", "April", "May"]

print("Extra dollars spent on February than January : " + str(month_expense[1] - month_expense[0])) #1

print("Total expense of first quarter : " + str(sum(month_expense[0 : 3])))  #2

print("Spent 2000$ in any month? ", 2000 in month_expense)  #3

month_expense.append(1980)
month_name.append("June")
print("Updated list : ", month_expense, month_name)  #4

month_expense[3] = month_expense[3] - 200
print("Expenses after 200$ return in April:" ,month_expense)  #5

print("New list:" ,month_expense, month_name)