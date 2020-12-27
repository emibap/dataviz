from datetime import datetime
from datetime import date

# Returns the percentage of the year that passed given a date string in YYYY-mm-dd format
# Min and max percentages are optional parameters (to improve visuals)
def get_date_year_percentage(date_str, min_pcn = 0.12, max_pcn = 0.88):

    date_time_obj = datetime.strptime(date_str, "%Y-%m-%d")

    year = date_time_obj.year

    date_year = datetime.combine(date(year, 1, 1), datetime.min.time())
    date_year_plus = datetime.combine(date(year + 1, 1, 1), datetime.min.time())

    days_passed = (date_time_obj - date_year).days

    return min(max((days_passed / (date_year_plus - date_year).days), min_pcn), max_pcn)


def get_year_from_datestr(date_str):
    date_time_obj = datetime.strptime(date_str, "%Y-%m-%d")

    return date_time_obj.year


# https://www.geeksforgeeks.org/insert-row-at-given-position-in-pandas-dataframe/
# Function to insert row in the dataframe 
def insert_row(row_number, df, row_value): 
	# Starting value of upper half 
	start_upper = 0

	# End value of upper half 
	end_upper = row_number 

	# Start value of lower half 
	start_lower = row_number 

	# End value of lower half 
	end_lower = df.shape[0] 

	# Create a list of upper_half index 
	upper_half = [*range(start_upper, end_upper, 1)] 

	# Create a list of lower_half index 
	lower_half = [*range(start_lower, end_lower, 1)] 

	# Increment the value of lower half by 1 
	lower_half = [x.__add__(1) for x in lower_half] 

	# Combine the two lists 
	index_ = upper_half + lower_half 

	# Update the index of the dataframe 
	df.index = index_ 

	# Insert a row at the end 
	df.loc[row_number] = row_value 
	
	# Sort the index labels 
	df = df.sort_index() 

	# return the dataframe 
	return df 

# Let's create a row which we want to insert 
# row_number = 2
# row_value = ['11/2/2011', 'Wrestling', 12000] 

# if row_number > df.index.max()+1: 
# 	print("Invalid row_number") 
# else: 
	
	## Let's call the function and insert the row 
	## at the second position 
	#df = Insert_row(row_number, df, row_value) 

	# Print the updated dataframe 
	#print(df) 