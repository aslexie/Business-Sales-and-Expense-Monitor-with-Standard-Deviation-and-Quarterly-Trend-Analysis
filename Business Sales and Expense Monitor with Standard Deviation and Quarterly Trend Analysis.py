# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:02:51 2024

@author: alexandria 
"""

import pandas as pd
import statistics
excel_file = input("Enter the path of the Excel file: ")
try:
file = pd.read_excel(excel_file)
if "Jan_Sales" in file.columns and "Jan_Expenses" in
file.columns:
# Calculate current month values
jan_sales_data =
file[file["Jan_Sales"].notna()]["Jan_Sales"]
jan_sales = file["Jan_Sales"].sum()
jan_expenses = file["Jan_Expenses"].sum()
jan_net_income = jan_sales - jan_expenses
jan_average_sales = round(jan_sales_data.mean(),2)
jan_sales_std =
round(statistics.stdev(jan_sales_data),2)
print("\nMonth of January: ")
print("Total sales: $", jan_sales)
print("Total expenses: $", jan_expenses)
print("Net Income: $", jan_net_income)
print("Average sale For Day: ", jan_average_sales)
print("Standard Deviation of sales: ", jan_sales_std)
if "Feb_Sales" in file.columns and "Feb_Expenses" in
file.columns:
# Get previous month's values
feb_sales = file["Feb_Sales"].sum()
feb_expenses = file["Feb_Expenses"].sum()
feb_sales_data =
file[file["Feb_Sales"].notna()]["Feb_Sales"]
feb_expenses_data =
file[file["Feb_Expenses"].notna()]["Feb_Expenses"]
feb_net_income = feb_sales_data.sum() -
feb_expenses_data.sum()
feb_sales_std =
round(statistics.stdev(feb_sales_data),2)
feb_average_sales = round(feb_sales_data.mean(),2)
# Calculate monthly changes
feb_sales_change = feb_sales - jan_sales
feb_expenses_change = feb_expenses - jan_expenses
feb_net_income_change = feb_sales - feb_expenses -
(jan_sales - jan_expenses)
# Calculate percentage changes
feb_sales_percentage_change =
round((feb_sales_change / jan_sales) * 100,2)
feb_expenses_percentage_change =
round((feb_expenses_change / jan_expenses) * 100,2)
feb_net_income_percentage_change =
round((feb_net_income_change / (jan_sales - jan_expenses)) *
100,2)
print("\nMonth of February:")
print("Total sales: $", feb_sales)
print("Total expenses: $", feb_expenses)
print("Net Income: $", feb_net_income)
print("Average sale For Day: ", feb_average_sales)
print("Standard Deviation of sales: ",
feb_sales_std)
if feb_sales_change > 0:
print("\nFebruary sales increased by",
feb_sales_percentage_change,"% compared to the month of
January.")
elif feb_sales_change < 0:
print("\nFebruary sales decreased by",
feb_sales_percentage_change,"% compared to the month of
January.")
else:
print("\nFebruary sales remained the same
compared to the month of January.")
if feb_expenses_change > 0:
print("February expenses increased by",
feb_expenses_percentage_change,"% compared to the month of
January.")
elif feb_expenses_change < 0:
print("February expenses decreased by",
feb_expenses_percentage_change,"% compared to the month of
January.")
else:
print("February expenses remained the same
compared to the month of January.")
if feb_net_income_change > 0:
16
print("February Net income increased by",
feb_net_income_percentage_change,"% compared to the month of
January.")
elif feb_net_income_change < 0:
print("February Net income decreased by",
feb_net_income_percentage_change,"% compared to the month of
January.")
else:
print("February Net income remained the same
compared to the month of January.")
if "Mar_Sales" in file.columns and "Mar_Expenses" in
file.columns:
# Get previous month's values
mar_sales = file["Mar_Sales"].sum()
mar_expenses = file["Mar_Expenses"].sum()
mar_sales_data =
file[file["Mar_Sales"].notna()]["Mar_Sales"]
mar_expenses_data =
file[file["Mar_Expenses"].notna()]["Mar_Expenses"]
mar_net_income = mar_sales_data.sum() -
mar_expenses_data.sum()
mar_sales_std =
round(statistics.stdev(mar_sales_data),2)
mar_average_sales =
round(mar_sales_data.mean(),2)
# Calculate monthly changes
mar_sales_change = mar_sales - feb_sales
mar_expenses_change = mar_expenses -
feb_expenses
mar_net_income_change = mar_sales - mar_expenses
- (feb_sales - feb_expenses)
# Calculate percentage changes
mar_sales_percentage_change =
round((mar_sales_change / feb_sales) * 100,2)
mar_expenses_percentage_change =
round((mar_expenses_change / feb_expenses) * 100,2)
mar_net_income_percentage_change =
round((mar_net_income_change / (feb_sales - feb_expenses)) *
100,2)
print("\nMonth of March:")
17
print("Total sales: $", mar_sales)
print("Total expenses: $", mar_expenses)
print("Net Income: $", mar_net_income)
print("Average sale For Day: ",
mar_average_sales)
print("Standard Deviation of sales: ",
mar_sales_std)
if mar_sales_change > 0:
print("\nMarch sales increased by",
mar_sales_percentage_change, "compared to the month of
February.")
elif mar_sales_change < 0:
print("\nMarch sales decreased by",
mar_sales_percentage_change, "compared to the month of
February.")
else:
print("\nMarch sales remained the same
compared to the month of February.")
if mar_expenses_change > 0:
print("March expenses increased by",
mar_expenses_percentage_change, "compared to the month of
February.")
elif mar_expenses_change < 0:
print("March expenses decreased by",
mar_expenses_percentage_change, "compared to the month of
February.")
else:
print("March expenses remained the same
compared to the month of February.")
if mar_net_income_change > 0:
print("March Net income increased by",
mar_net_income_percentage_change, "compared to the month of
February.")
elif mar_net_income_change < 0:
print("March Net income decreased by",
mar_net_income_percentage_change, "compared to the month of
February.")
else:
print("March Net income remained the same
compared to the month of February.")
if "Apr_Sales" in file.columns and
"Apr_Expenses" in file.columns:
18
# Get previous month's values
apr_sales = file["Apr_Sales"].sum()
apr_expenses = file["Apr_Expenses"].sum()
apr_sales_data =
file[file["Apr_Sales"].notna()]["Apr_Sales"]
apr_expenses_data =
file[file["Apr_Expenses"].notna()]["Apr_Expenses"]
apr_net_income = apr_sales_data.sum() -
apr_expenses_data.sum()
apr_sales_std =
round(statistics.stdev(apr_sales_data),2)
apr_average_sales =
round(apr_sales_data.mean(),2)
# Calculate monthly changes
apr_sales_change = apr_sales - mar_sales
apr_expenses_change = apr_expenses -
mar_expenses
apr_net_income_change = apr_sales -
apr_expenses - (mar_sales - mar_expenses)
# Calculate percentage changes
apr_sales_percentage_change =
round((apr_sales_change / mar_sales) * 100,2)
apr_expenses_percentage_change =
round((apr_expenses_change / mar_expenses) * 100,2)
apr_net_income_percentage_change =
round((apr_net_income_change / (mar_sales - mar_expenses)) *
100,2)
print("\nMonth of April:")
print("Total sales: $", apr_sales)
print("Total expenses: $", apr_expenses)
print("Net Income: $", apr_net_income)
print("Average sale For Day: ",
apr_average_sales)
print("Standard Deviation of sales: ",
apr_sales_std)
if apr_sales_change > 0:
print("\nApril sales increased by",
apr_sales_percentage_change,"% compared to the month of March.")
elif apr_sales_change < 0:
19
print("\nApril sales decreased by",
apr_sales_percentage_change,"% compared to the month of March.")
else:
print("\nApril sales remained the same
compared to the month of March.")
if apr_expenses_change > 0:
print("April expenses increased by",
apr_expenses_percentage_change,"% compared to the month of
March.")
elif apr_expenses_change < 0:
print("April expenses decreased by",
apr_expenses_percentage_change,"% compared to the month of
March.")
else:
print("April expenses remained the same
compared to the month of March.")
if apr_net_income_change > 0:
print("April Net income increased by",
apr_net_income_percentage_change,"% compared to the month of
March.")
elif apr_net_income_change < 0:
print("April Net income decreased by",
apr_net_income_percentage_change,"% compared to the month of
March.")
else:
print("April Net income remained the
same compared to the month of March.")
if "May_Sales" in file.columns and
"May_Expenses" in file.columns:
# Get previous month's values
may_sales = file["May_Sales"].sum()
may_expenses =
file["May_Expenses"].sum()
may_sales_data =
file[file["May_Sales"].notna()]["May_Sales"]
may_expenses_data =
file[file["May_Expenses"].notna()]["May_Expenses"]
may_net_income = may_sales_data.sum() -
may_expenses_data.sum()
may_sales_std =
round(statistics.stdev(may_sales_data),2)
20
may_average_sales =
round(may_sales_data.mean(),2)
# Calculate monthly changes
may_sales_change = may_sales - apr_sales
may_expenses_change = may_expenses -
apr_expenses
may_net_income_change = may_sales -
may_expenses - (apr_sales - apr_expenses)
# Calculate percentage changes
may_sales_percentage_change =
round((may_sales_change / apr_sales) * 100,2)
may_expenses_percentage_change =
round((may_expenses_change / apr_expenses) * 100,2)
may_net_income_percentage_change =
round((may_net_income_change / (apr_sales - apr_expenses)) *
100,2)
print("\nMonth of May:")
print("Total sales: $", may_sales)
print("Total expenses: $", may_expenses)
print("Net Income: $", may_net_income)
print("Average sale For Day: ",
may_average_sales)
print("Standard Deviation of sales: ",
may_sales_std)
if may_sales_change > 0:
print("\nMay sales increased by",
may_sales_percentage_change,"% compared to the month of April.")
elif may_sales_change < 0:
print("\nMay sales decreased by",
may_sales_percentage_change,"% compared to the month of April.")
else:
print("\nMay sales remained the same
compared to the month of April.")
if may_expenses_change > 0:
print("May expenses increased by",
may_expenses_percentage_change,"% compared to the month of
April.")
elif may_expenses_change < 0:
print("May expenses decreased by",
may_expenses_percentage_change,"% compared to the month of
April.")
21
else:
print("May expenses remained the
same compared to the month of April.")
if may_net_income_change > 0:
print("May Net income increased by",
may_net_income_percentage_change,"% compared to the month of
April.")
elif may_net_income_change < 0:
print("May Net income decreased by",
may_net_income_percentage_change,"% compared to the month of
April.")
else:
print("May Net income remained the
same compared to the month of April.")
if "Jun_Sales" in file.columns and
"Jun_Expenses" in file.columns:
# Get previous month's values
jun_sales = file["Jun_Sales"].sum()
jun_expenses =
file["Jun_Expenses"].sum()
jun_sales_data =
file[file["Jun_Sales"].notna()]["Jun_Sales"]
jun_expenses_data =
file[file["Jun_Expenses"].notna()]["Jun_Expenses"]
jun_net_income =
jun_sales_data.sum() - jun_expenses_data.sum()
jun_sales_std =
round(statistics.stdev(jun_sales_data),2)
jun_average_sales =
round(jun_sales_data.mean(),2)
# Calculate monthly changes
jun_sales_change = jun_sales -
may_sales
jun_expenses_change = jun_expenses -
may_expenses
jun_net_income_change = jun_sales -
jun_expenses - (may_sales - may_expenses)
# Calculate percentage changes
jun_sales_percentage_change =
round((jun_sales_change / may_sales) * 100,2)
22
jun_expenses_percentage_change =
round((jun_expenses_change / may_expenses) * 100,2)
jun_net_income_percentage_change =
round((jun_net_income_change / (may_sales - may_expenses)) *
100,2)
print("\nMonth of June:")
print("Total sales: $", jun_sales)
print("Total expenses: $",
jun_expenses)
print("Net Income: $",
jun_net_income)
print("Average sale For Day: ",
jun_average_sales)
print("Standard Deviation of sales:
", jun_sales_std)
if jun_sales_change > 0:
print("\nJune sales increased
by", jun_sales_percentage_change,"% compared to the month of
May.")
elif jun_sales_change < 0:
print("\nJune sales decreased
by", jun_sales_percentage_change,"% compared to the month of
May.")
else:
print("\nJune sales remained the
same compared to the month of May.")
if jun_expenses_change > 0:
print("June expenses increased
by", jun_expenses_percentage_change,"% compared to the month of
May.")
elif jun_expenses_change < 0:
print("June expenses decreased
by", jun_expenses_percentage_change,"% compared to the month of
May.")
else:
print("June expenses remained
the same compared to the month of May.")
if jun_net_income_change > 0:
print("June Net income increased
by", jun_net_income_percentage_change,"% compared to the month
of May.")
elif jun_net_income_change < 0:
23
print("June Net income decreased
by", jun_net_income_percentage_change,"% compared to the month
of May.")
else:
print("June Net income remained
the same compared to the month of May.")
if "Jul_Sales" in file.columns and
"Jul_Expenses" in file.columns:
# Get previous month's values
jul_sales =
file["Jul_Sales"].sum()
jul_expenses =
file["Jul_Expenses"].sum()
jul_sales_data =
file[file["Jul_Sales"].notna()]["Jul_Sales"]
jul_expenses_data =
file[file["Jul_Expenses"].notna()]["Jul_Expenses"]
jul_net_income =
jul_sales_data.sum() - jul_expenses_data.sum()
jul_sales_std =
round(statistics.stdev(jul_sales_data),2)
jul_average_sales =
round(jul_sales_data.mean(),2)
# Calculate monthly changes
jul_sales_change = jul_sales -
jun_sales
jul_expenses_change =
jul_expenses - jun_expenses
jul_net_income_change =
jul_sales - jul_expenses - (jun_sales - jun_expenses)
# Calculate percentage changes
jul_sales_percentage_change =
round((jul_sales_change / jun_sales) * 100,2)
jul_expenses_percentage_change =
round((jul_expenses_change / jun_expenses) * 100,2)
jul_net_income_percentage_change
= round((jul_net_income_change / (jun_sales - jun_expenses)) *
100,2)
print("\nMonth of July:")
print("Total sales: $",
jul_sales)
24
print("Total expenses: $",
jul_expenses)
print("Net Income: $",
jul_net_income)
print("Average sale For Day: ",
jul_average_sales)
print("Standard Deviation of
sales: ", jul_sales_std)
if jul_sales_change > 0:
print("\nJuly sales
increased by", jul_sales_percentage_change,"% compared to the
month of June.")
elif jul_sales_change < 0:
print("\nJuly sales
decreased by", jul_sales_percentage_change,"% compared to the
month of June.")
else:
print("\nJuly sales remained
the same compared to the month of June.")
if jul_expenses_change > 0:
print("July expenses
increased by", jul_expenses_percentage_change,"% compared to the
month of June.")
elif jul_expenses_change < 0:
print("July expenses
decreased by", jul_expenses_percentage_change,"% compared to the
month of June.")
else:
print("July expenses
remained the same compared to the month of June.")
if jul_net_income_change > 0:
print("July Net income
increased by", jul_net_income_percentage_change,"% compared to
the month of June.")
elif jul_net_income_change < 0:
print("July Net income
decreased by", jul_net_income_percentage_change,"% compared to
the month of June.")
else:
print("July Net income
remained the same compared to the month of June.")
25
if "Aug_Sales" in file.columns
and "Aug_Expenses" in file.columns:
# Get previous month's
values
aug_sales =
file["Aug_Sales"].sum()
aug_expenses =
file["Aug_Expenses"].sum()
aug_sales_data =
file[file["Aug_Sales"].notna()]["Aug_Sales"]
aug_expenses_data =
file[file["Aug_Expenses"].notna()]["Aug_Expenses"]
aug_net_income =
aug_sales_data.sum() - aug_expenses_data.sum()
aug_sales_std =
round(statistics.stdev(aug_sales_data),2)
aug_average_sales =
round(aug_sales_data.mean(),2)
# Calculate monthly changes
aug_sales_change = aug_sales
- jul_sales
aug_expenses_change =
aug_expenses - jul_expenses
aug_net_income_change =
aug_sales - aug_expenses - (jul_sales - jul_expenses)
# Calculate percentage
changes
aug_sales_percentage_change
= round((aug_sales_change / jul_sales) * 100,2)
aug_expenses_percentage_change = round((aug_expenses_change /
jul_expenses) * 100,2)
aug_net_income_percentage_change = round((aug_net_income_change
/ (jul_sales - jul_expenses)) * 100,2)
print("\nMonth of August:")
print("Total sales: $",
aug_sales)
print("Total expenses: $",
aug_expenses)
print("Net Income: $",
aug_net_income)
26
print("Average sale For Day:
", aug_average_sales)
print("Standard Deviation of
sales: ", aug_sales_std)
if aug_sales_change > 0:
print("\nAugust sales
increased by", aug_sales_percentage_change,"% compared to the
month of July.")
elif aug_sales_change < 0:
print("\nAugust sales
decreased by", aug_sales_percentage_change,"% compared to the
month of July.")
else:
print("\nAugust sales
remained the same compared to the month of July.")
if aug_expenses_change > 0:
print("August expenses
increased by", aug_expenses_percentage_change,"% compared to the
month of July.")
elif aug_expenses_change <
0:
print("August expenses
decreased by", aug_expenses_percentage_change,"% compared to the
month of July.")
else:
print("August expenses
remained the same compared to the month of July.")
if aug_net_income_change >
0:
print("August Net income
increased by", aug_net_income_percentage_change,"% compared to
the month of July.")
elif aug_net_income_change <
0:
print("August Net income
decreased by", aug_net_income_percentage_change,"% compared to
the month of July.")
else:
print("August Net income
remained the same compared to the month of July.")
if "Sep_Sales" in
file.columns and "Sep_Expenses" in file.columns:
27
# Get previous month's
values
sep_sales =
file["Sep_Sales"].sum()
sep_expenses =
file["Sep_Expenses"].sum()
sep_sales_data =
file[file["Sep_Sales"].notna()]["Sep_Sales"]
sep_expenses_data =
file[file["Sep_Expenses"].notna()]["Sep_Expenses"]
sep_net_income =
sep_sales_data.sum() - sep_expenses_data.sum()
sep_sales_std =
round(statistics.stdev(sep_sales_data),2)
sep_average_sales =
round(sep_sales_data.mean(),2)
# Calculate monthly
changes
sep_sales_change =
sep_sales - aug_sales
sep_expenses_change =
sep_expenses - aug_expenses
sep_net_income_change =
sep_sales - sep_expenses - (aug_sales - aug_expenses)
# Calculate percentage
changes
sep_sales_percentage_change = round((sep_sales_change /
aug_sales) * 100,2)
sep_expenses_percentage_change = round((sep_expenses_change /
aug_expenses) * 100,2)
sep_net_income_percentage_change = round((sep_net_income_change
/ (aug_sales - aug_expenses)) * 100,2)
print("\nMonth of
September:")
print("Total sales: $",
sep_sales)
print("Total expenses:
$", sep_expenses)
28
print("Net Income: $",
sep_net_income)
print("Average sale For
Day: ", sep_average_sales)
print("Standard
Deviation of sales: ", sep_sales_std)
if sep_sales_change > 0:
print("\nSeptember
sales increased by", sep_sales_percentage_change,"% compared to
the month of August.")
elif sep_sales_change <
0:
print("\nSeptember
sales decreased by", sep_sales_percentage_change,"% compared to
the month of August.")
else:
print("\nSeptember
sales remained the same compared to the month of August.")
if sep_expenses_change >
0:
print("September
expenses increased by", sep_expenses_percentage_change,"%
compared to the month of August.")
elif sep_expenses_change
< 0:
print("September
expenses decreased by", sep_expenses_percentage_change,"%
compared to the month of August.")
else:
print("September
expenses remained the same compared to the month of August.")
if sep_net_income_change
> 0:
print("September Net
income increased by", sep_net_income_percentage_change,"%
compared to the month of August.")
elif
aug_net_income_change < 0:
print("September Net
income decreased by", sep_net_income_percentage_change,"%
compared to the month of August.")
else:
29
print("September Net
income remained the same compared to the month of August.")
if "Oct_Sales" in
file.columns and "Oct_Expenses" in file.columns:
# Get previous
month's values
oct_sales =
file["Oct_Sales"].sum()
oct_expenses =
file["Oct_Expenses"].sum()
oct_sales_data =
file[file["Oct_Sales"].notna()]["Oct_Sales"]
oct_expenses_data =
file[file["Oct_Expenses"].notna()]["Oct_Expenses"]
oct_net_income =
oct_sales_data.sum() - oct_expenses_data.sum()
oct_sales_std =
round(statistics.stdev(oct_sales_data),2)
oct_average_sales =
round(oct_sales_data.mean(),2)
# Calculate monthly
changes
oct_sales_change =
oct_sales - sep_sales
oct_expenses_change
= oct_expenses - sep_expenses
oct_net_income_change = oct_sales - oct_expenses - (sep_sales -
sep_expenses)
# Calculate
percentage changes
oct_sales_percentage_change = round((oct_sales_change /
sep_sales) * 100,2)
oct_expenses_percentage_change = round((oct_expenses_change /
oct_expenses) * 100,2)
oct_net_income_percentage_change = round((oct_net_income_change
/ (sep_sales - sep_expenses)) * 100,2)
30
print("\nMonth of
September:")
print("Total sales:
$", oct_sales)
print("Total
expenses: $", oct_expenses)
print("Net Income:
$", oct_net_income)
print("Average sale
For Day: ", oct_average_sales)
print("Standard
Deviation of sales: ", oct_sales_std)
if oct_sales_change
> 0:
print("\nOctober
sales increased by", oct_sales_percentage_change,"% compared to
the month of September.")
elif
oct_sales_change < 0:
print("\nOctober
sales decreased by", oct_sales_percentage_change,"% compared to
the month of September.")
else:
print("\nOctober
sales remained the same compared to the month of September.")
if
oct_expenses_change > 0:
print("October
expenses increased by", oct_expenses_percentage_change,"%
compared to the month of September.")
elif
oct_expenses_change < 0:
print("October
expenses decreased by", oct_expenses_percentage_change,"%
compared to the month of September.")
else:
print("October
expenses remained the same compared to the month of September.")
if
oct_net_income_change > 0:
print("October
Net income increased by", oct_net_income_percentage_change,"%
compared to the month of September.")
31
elif
oct_net_income_change < 0:
print("October
Net income decreased by", oct_net_income_percentage_change,"%
compared to the month of September.")
else:
print("October
Net income remained the same compared to the month of
September.")
if "Nov_Sales" in
file.columns and "Nov_Expenses" in file.columns:
# Get previous
month's values
nov_sales =
file["Nov_Sales"].sum()
nov_expenses =
file["Nov_Expenses"].sum()
nov_sales_data =
file[file["Nov_Sales"].notna()]["Nov_Sales"]
nov_expenses_data =
file[file["Nov_Expenses"].notna()]["Nov_Expenses"]
nov_net_income =
nov_sales_data.sum() - nov_expenses_data.sum()
nov_sales_std =
round(statistics.stdev(nov_sales_data),2)
nov_average_sales = round(nov_sales_data.mean(),2)
# Calculate
monthly changes
nov_sales_change
= nov_sales - oct_sales
nov_expenses_change = nov_expenses - oct_expenses
nov_net_income_change = nov_sales - nov_expenses - (oct_sales -
oct_expenses)
# Calculate
percentage changes
nov_sales_percentage_change = round((nov_sales_change /
oct_sales) * 100,2)
32
nov_expenses_percentage_change = round((nov_expenses_change /
oct_expenses) * 100,2)
nov_net_income_percentage_change = round((nov_net_income_change
/ (oct_sales - oct_expenses)) * 100,2)
print("\nMonth
of November:")
print("Total
sales: $", nov_sales)
print("Total
expenses: $", nov_expenses)
print("Net
Income: $", nov_net_income)
print("Average
sale For Day: ", nov_average_sales)
print("Standard
Deviation of sales: ", nov_sales_std)
if
nov_sales_change > 0:
print("\nNovember sales increased by",
nov_sales_percentage_change,"% compared to the month of
October.")
elif
nov_sales_change < 0:
print("\nNovember sales decreased by",
nov_sales_percentage_change,"% compared to the month of
October.")
else:
print("\nNovember sales remained the same compared to the month
of October.")
if
nov_expenses_change > 0:
print("November expenses increased by",
nov_expenses_percentage_change,"% compared to the month of
October.")
elif
nov_expenses_change < 0:
33
print("November expenses decreased by",
nov_expenses_percentage_change,"% compared to the month of
October.")
else:
print("November expenses remained the same compared to the month
of October.")
if
nov_net_income_change > 0:
print("November Net income increased by",
nov_net_income_percentage_change,"% compared to the month of
October.")
elif
nov_net_income_change < 0:
print("November Net income decreased by",
nov_net_income_percentage_change,"% compared to the month of
October.")
else:
print("November Net income remained the same compared to the
month of October.")
if "Dec_Sales"
in file.columns and "Oct_Expenses" in file.columns:
# Get
previous month's values
dec_sales =
file["Dec_Sales"].sum()
dec_expenses
= file["Dec_Expenses"].sum()
dec_sales_data = file[file["Dec_Sales"].notna()]["Dec_Sales"]
dec_expenses_data =
file[file["Dec_Expenses"].notna()]["Dec_Expenses"]
dec_net_income = dec_sales_data.sum() - dec_expenses_data.sum()
dec_sales_std = round(statistics.stdev(dec_sales_data),2)
dec_average_sales = round(dec_sales_data.mean(),2)
34
# Calculate
monthly changes
dec_sales_change = dec_sales - nov_sales
dec_expenses_change = dec_expenses - nov_expenses
dec_net_income_change = dec_sales - dec_expenses - (nov_sales -
nov_expenses)
# Calculate
percentage changes
dec_sales_percentage_change = round((dec_sales_change /
nov_sales) * 100,2)
dec_expenses_percentage_change = round((dec_expenses_change /
nov_expenses) * 100,2)
dec_net_income_percentage_change = round((dec_net_income_change
/ (nov_sales - nov_expenses)) * 100,2)
print("\nMonth of December:")
print("Total
sales: $", dec_sales)
print("Total
expenses: $", dec_expenses)
print("Net
Income: $", dec_net_income)
print("Average sale For Day: ", dec_average_sales)
print("Standard Deviation of sales: ", dec_sales_std)
if
dec_sales_change > 0:
print("\nDecember sales increased by",
dec_sales_percentage_change,"% compared to the month of
Novemeber.")
elif
dec_sales_change < 0:
print("\nDecember sales decreased by",
35
dec_sales_percentage_change,"% compared to the month of
November.")
else:
print("\nDecember sales remained the same compared to the month
of November.")
if
dec_expenses_change > 0:
print("December expenses increased by",
dec_expenses_percentage_change,"% compared to the month of
November.")
elif
dec_expenses_change < 0:
print("December expenses decreased by",
dec_expenses_percentage_change,"% compared to the month of
November.")
else:
print("December expenses remained the same compared to the month
of November.")
if
dec_net_income_change > 0:
print("December Net income increased by",
dec_net_income_percentage_change,"% compared to the month of
November.")
elif
dec_net_income_change < 0:
print("December Net income decreased by",
dec_net_income_percentage_change,"% compared to the month of
November.")
else:
print("Decmber Net income remained the same compared to the
month of Novemebr.")
else:
print("\nDec_Sales or Dec_Expenses columns not found in the
Excel file.")
else:
36
print("\nNov_Sales
or Nov_Expenses columns not found in the Excel file.")
else:
print("\nSep_Sales or
Sep_Expenses columns not found in the Excel file.")
else:
print("\nAug_Sales or
Aug_Expenses columns not found in the Excel file.")
else:
print("\nJul_Sales or
Jul_Expenses columns not found in the Excel file.")
else:
print("\nJune_Sales or
June_Expenses columns not found in the Excel file.")
else:
print("\nMay_Sales or May_Expenses
columns not found in the Excel file.")
else:
print("\nApr_Sales or Apr_Expenses columns
not found in the Excel file.")
else:
print("\nMar_Sales or Mar_Expenses columns not
found in the Excel file.")
else:
print("\nFeb_Sales or Feb_Expenses columns not found
in the Excel file.")
else:
print("\nJan_Sales or Jan_Expenses columns not found in
the Excel file.")
except FileNotFoundError:
print("File not found.")
except Exception as e:
print("An error occurred:", str(e))
if jan_sales and jan_expenses is None or feb_sales and
feb_expenses is None or mar_sales and mar_expenses is None:
print("Warning: missing data for one or more months")
37
else:
quarter_one_sales = jan_sales + feb_sales + mar_sales
quarter_one_expenses = jan_expenses + feb_expenses +
mar_expenses
quarter_one_net_profit = quarter_one_sales -
quarter_one_expenses
print("\nQuarter 1 Report")
print("\nTotal Sales:", quarter_one_sales)
print("Total Expenses:", quarter_one_expenses)
print("Net Profit:", quarter_one_net_profit)
if apr_sales and apr_expenses is None or may_sales and
may_expenses is None or jun_sales and jun_expenses is None:
print("Warning: missing data for one or more months")
else:
quarter_two_sales = apr_sales + may_sales + jun_sales
quarter_two_expenses = apr_expenses + may_expenses +
jun_expenses
quarter_two_net_profit = quarter_two_sales -
quarter_two_expenses
print("\nQuarter 2 Report")
print("\nTotal Sales:", quarter_two_sales)
print("Total Expenses:", quarter_two_expenses)
print("Net Profit:", quarter_two_net_profit)
# Calculate monthly changes
quarter_two_sales_change = quarter_two_sales -
quarter_one_sales
quarter_two_expenses_change = quarter_two_expenses -
quarter_one_expenses
quarter_two_net_income_change = quarter_two_net_profit -
quarter_one_net_profit
# Calculate percentage changes
quarter_two_sales_percentage_change =
round((quarter_two_sales_change / quarter_one_sales) * 100,2)
quarter_two_expenses_percentage_change =
round((quarter_two_expenses_change / quarter_one_expenses) *
100,2)
quarter_two_net_income_percentage_change =
round(quarter_two_net_income_change /( quarter_one_net_profit) *
100,2)
if quarter_two_sales_change > 0:
print("\nQuarter 2 sales increased by",
quarter_two_sales_percentage_change,"% compared to the Quarter
1.")
38
elif quarter_two_sales_change < 0:
print("\nQuarter 2 sales decreased by",
quarter_two_sales_percentage_change,"% compared to the Quarter
1.")
else:
print("\nQuarter 2 sales remained the same compared to the
Quarter 1.")
if quarter_two_expenses_change > 0:
print("Quarter 3 expenses increased by",
quarter_two_expenses_percentage_change,"% compared to the
Quarter 1.")
elif quarter_two_expenses_change< 0:
print("Quarter 2 expenses decreased by",
quarter_two_expenses_percentage_change,"% compared to the
Quarter 1.")
else:
print("Quarter 2 expenses remained the same compared to the
Quarter 1.")
if quarter_two_net_income_change > 0:
print("Quarter 2 Net income increased by",
quarter_two_net_income_percentage_change,"% compared to the
Quarter 1.")
elif quarter_two_net_income_change < 0:
print("Quarter 2 Net income decreased by",
quarter_two_net_income_percentage_change,"% compared to the
Quarter 1.")
else:
print("Quarter 2 Net income remained the same compared to
the Quarter 1.")
if jul_sales and jul_expenses is None or aug_sales and
aug_expenses is None or sep_sales and sep_expenses is None:
print("Warning: missing data for one or more months")
else:
quarter_three_sales = jul_sales + aug_sales + sep_sales
quarter_three_expenses = jul_expenses + aug_expenses +
sep_expenses
quarter_three_net_profit = quarter_three_sales -
quarter_three_expenses
print("\nQuarter 3 Report")
print("\nTotal Sales:", quarter_three_sales)
print("Total Expenses:", quarter_three_expenses)
print("Net Profit:", quarter_three_net_profit)
39
# Calculate monthly changes
quarter_three_sales_change = quarter_three_sales -
quarter_two_sales
quarter_three_expenses_change = quarter_three_expenses -
quarter_two_expenses
quarter_three_net_income_change = quarter_three_net_profit -
quarter_two_net_profit
# Calculate percentage changes
quarter_three_sales_percentage_change =
round((quarter_three_sales_change / quarter_two_sales) * 100,2)
quarter_three_expenses_percentage_change =
round((quarter_three_expenses_change / quarter_two_expenses) *
100,2)
quarter_three_net_income_percentage_change =
round(quarter_three_net_income_change /( quarter_two_net_profit)
* 100,2)
if quarter_three_sales_change > 0:
print("\nQuarter 3 sales increased by",
quarter_three_sales_percentage_change,"% compared to the Quarter
2.")
elif quarter_three_sales_change < 0:
print("\nQuarter 3 sales decreased by",
quarter_three_sales_percentage_change,"% compared to the Quarter
2.")
else:
print("\nQuarter 3 sales remained the same compared to the
Quarter 2.")
if quarter_three_expenses_change > 0:
print("Quarter 3 expenses increased by",
quarter_three_expenses_percentage_change,"% compared to the
Quarter 2.")
elif quarter_three_expenses_change< 0:
print("Quarter 3 expenses decreased by",
quarter_three_expenses_percentage_change,"% compared to the
Quarter 2.")
else:
print("Quarter 3 expenses remained the same compared to the
Quarter 2.")
if quarter_three_net_income_change > 0:
print("Quarter 3 Net income increased by",
quarter_three_net_income_percentage_change,"% compared to the
Quarter 2.")
elif quarter_three_net_income_change < 0:
40
print("Quarter 3 Net income decreased by",
quarter_three_net_income_percentage_change,"% compared to the
Quarter 2.")
else:
print("Quarter 3 Net income remained the same compared to
the Quarter 2.")
if oct_sales and oct_expenses is None or nov_sales and
nov_expenses is None or dec_sales and dec_expenses is None:
print("Warning: missing data for one or more months")
else:
quarter_four_sales = oct_sales + nov_sales + dec_sales
quarter_four_expenses = oct_expenses + nov_expenses +
dec_expenses
quarter_four_net_profit = quarter_four_sales -
quarter_four_expenses
print("\nQuarter 4 Report")
print("\nTotal Sales:", quarter_four_sales)
print("Total Expenses:", quarter_four_expenses)
print("Net Profit:", quarter_four_net_profit)
# Calculate monthly changes
quarter_four_sales_change = quarter_four_sales -
quarter_three_sales
quarter_four_expenses_change = quarter_four_expenses -
quarter_three_expenses
quarter_four_net_income_change = quarter_four_net_profit -
quarter_three_net_profit
# Calculate percentage changes
quarter_four_sales_percentage_change =
round((quarter_four_sales_change / quarter_three_sales) * 100,2)
quarter_four_expenses_percentage_change =
round((quarter_four_expenses_change / quarter_three_expenses) *
100,2)
quarter_four_net_income_percentage_change =
round(quarter_four_net_income_change /(
quarter_three_net_profit) * 100,2)
if quarter_four_sales_change > 0:
print("\nQuarter 4 sales increased by",
quarter_four_sales_percentage_change,"% compared to the Quarter
3.")
elif quarter_four_sales_change < 0:
41
print("\nQuarter 4 sales decreased by",
quarter_four_sales_percentage_change,"% compared to the Quarter
3.")
else:
print("\nQuarter 4 sales remained the same compared to the
Quarter 3.")
if quarter_four_expenses_change > 0:
print("Quarter 4 expenses increased by",
quarter_four_expenses_percentage_change,"% compared to the
Quarter 3.")
elif quarter_four_expenses_change< 0:
print("Quarter 4 expenses decreased by",
quarter_four_expenses_percentage_change,"% compared to the
Quarter 3.")
else:
print("Quarter 4 expenses remained the same compared to the
Quarter 3.")
if quarter_four_net_income_change > 0:
print("Quarter 4 Net income increased by",
quarter_four_net_income_percentage_change,"% compared to the
Quarter 3.")
elif quarter_four_net_income_change < 0:
print("Quarter 4 Net income decreased by",
quarter_four_net_income_percentage_change,"% compared to the
Quarter 3.")
else:
print("Quarter 4 Net income remained the same compared to the Quarter 3 .")