import array
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
# while date_of_interest[i] >= "01/01/2021" and date_of_interest[i] <= "01/31/2021": 
#   cum_case_count = cum_case_count + case_count[i]
#   cum_mn_case_count = cum_mn_case_count +  cum_mn_case_count[i]
#   i++ 
#   print(date_of_interest[i], cum_case_count, cum_mn_case_count)
#return

pop_nyc = 8804190
pop_mn = 1694263

#open csv
with open("./cases-by-day.csv", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)


def case_count(x,y):
    #set variables
    cum_case_count = 0
    cum_mn_case_count = 0

    #find date indices
    dates = []
    for row in rows:
        dates.append(row["date_of_interest"])

    start = dates.index(x)
    end = dates.index(y)

    #loop
    for i in range(start, end + 1):
        cum_case_count += int(rows[i]["CASE_COUNT"])
        cum_mn_case_count += int(rows[i]["MN_CASE_COUNT"])
    
    print(f"dates_of_interest: {dates[start]}:{dates[end]}, cum_case_count: {cum_case_count}, cum_mn_case_count: {cum_mn_case_count}")
    return (dates[start],dates[end], cum_case_count, cum_mn_case_count)

# calculating a
tup_case_count_jan2021 = case_count("01/01/2021", "01/31/2021")

cum_mn_case_count_jan2021 = tup_case_count_jan2021[3]
p_mn_and_i_jan2021 = cum_mn_case_count_jan2021/pop_nyc
p_mn = pop_mn / pop_nyc

p_i_given_mn_jan2021 = p_mn_and_i_jan2021 / p_mn
print(p_i_given_mn_jan2021) #0.011410861241731655

## (b) - 6 points
cum_case_count_jan2021 = tup_case_count_jan2021[2]
p_mn_and_i_jan2021 = cum_mn_case_count_jan2021/pop_nyc
p_i_jan2021 = cum_case_count_jan2021 / pop_nyc 

p_mn_given_i_jan2021 = p_mn_and_i_jan2021 / p_i_jan2021
print(p_mn_given_i_jan2021) #0.1395048454716668

## (c) - 6 points
p_i2024_given_i2021 = 0.05
p_i2024_given_noti2021 = 0.20
p_i2021_given_i2024 = (p_i2024_given_i2021 * p_i_jan2021)/(p_i2024_given_i2021 * p_i_jan2021 + p_i2024_given_noti2021 * (1-p_i_jan2021))
print(p_i2021_given_i2024) #0.003982154426490655