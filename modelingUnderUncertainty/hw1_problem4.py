import numpy
import csv

#Problem 4 - Covid19, 23 points
## (a) - 11 points
# Pr(Infected | Lived in Manhattan) = Pr (Lived in Manhattan and was Infected) / Pr (Lived in Manhattan)
# pseudocode
# imports
# import numpy
# import csv file cases-by-day.csv
#
# set variables
# pop_nyc = 8804190
# pop_mn = 1694263
# cum_case_count = 0
# cum_mn_case_count = 0  
# i = 0
# 
# loop  
# while date_of_interest[i] =! "01/31/2021": 
#   cum_case_count = cum_case_count + case_count[i]
#   cum_mn_case_count = cum_mn_case_count +  cum_mn_case_count[i]
#   i++ 
#   print(date_of_interest[i], cum_case_count, cum_mn_case_count)
#return

#set variables
pop_nyc = 8804190
pop_mn = 1694263
cum_case_count = 0
cum_mn_case_count = 0

#open csv
with open("./cases-by-day.csv", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

#loop
i = 0
while rows[i]["date_of_interest"] != "02/01/2021":
    cum_case_count += int(rows[i]["CASE_COUNT"])
    cum_mn_case_count += int(rows[i]["MN_CASE_COUNT"])
    i += 1

# conditional probability
p_mn_and_infected = cum_mn_case_count / pop_nyc
p_mn = pop_mn / pop_nyc
p_infected_given_mn = p_mn_and_infected / p_mn
p_infected = cum_case_count / pop_nyc

#print
print(f"date_of_interest: {rows[i]['date_of_interest']}, cum_case_count: {cum_case_count}, cum_mn_case_count: {cum_mn_case_count}")
print(f"checking by python {p_infected_given_mn}")
print(f"checking by hand {(75017/8804190)/(1694263/8804190)}")


## (b) - 6 points
p_mn_given_infected = p_mn_and_infected / p_infected
print(f"checking by python {p_mn_given_infected}")
print(f"checking by hand {(75017/8804190)/(540124/8804190)}")