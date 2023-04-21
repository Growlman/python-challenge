import os
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')

day = []
profit = []
profit_change = []

month = 0
total_profit = 0
total_profit_change = 0
initial_profit = 0

with open(budget_csv) as finances:
	csv_reader = csv.reader(finances, delimiter = ",")
	csv_header = next(csv_reader)

	for row in csv_reader:
		
		month = month + 1

		day.append(row[0])

		profit.append(row[1])
		total_profit = total_profit + int(row[1])

		final_prof = int(row[1])
		monthly_prof_var = final_prof - initial_profit

		profit_change.append(monthly_prof_var)

		total_profit_change = total_profit_change + monthly_prof_var
		initial_profit = final_prof

		avg_change = (total_profit_change/month)

		greatest_inc = max(profit_change)
		greatest_dec = min(profit_change)

		inc_date = day[profit_change.index(greatest_inc)]
		dec_date = day[profit_change.index(greatest_dec)]

	print("----------------------------------------------------------")
	print("Financial Analysis")
	print("----------------------------------------------------------")
	print("Total Months: " + str(month))
	print("Total Profits: " + "$" + str(total_profit))
	print("Average Change: " + "$" + str(int(avg_change)))
	print("Greatest Increase in Profits: " + str(inc_date) + " ($" + str(greatest_inc) + ")")
	print("Greatest Decrease in Profits: " + str(dec_date) + " ($" + str(greatest_dec)+ ")")
	print("----------------------------------------------------------")

output = os.path.join("analysis", "analysis.txt")
with open(output, 'w') as text:
	text.write("----------------------------------------------------------\n")
	text.write("  Financial Analysis"+ "\n")
	text.write("----------------------------------------------------------\n\n")
	text.write("    Total Months: " + str(month) + "\n")
	text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
	text.write("    Average Change: " + '$' + str(int(avg_change)) + "\n")
	text.write("    Greatest Increase in Profits: " + str(inc_date) + " ($" + str(greatest_inc) + ")\n")
	text.write("    Greatest Decrease in Profits: " + str(dec_date) + " ($" + str(greatest_dec) + ")\n")
	text.write("----------------------------------------------------------\n")


