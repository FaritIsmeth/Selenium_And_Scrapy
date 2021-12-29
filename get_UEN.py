import pandas
import warnings
warnings.filterwarnings("ignore", 'This pattern has match groups')

counter = counter2 = counter3 = 0
get_filtered_result = ""
get_uen = {}
get_name = {}
df = pandas.read_csv('try_this.csv', dtype=str)
df2 = pandas.read_csv('entities-registered-with-acra.csv', dtype=str)
columns = ['entity_name','uen'] #only select rows from these column headers
df3 = pandas.DataFrame(df2, columns=columns)

while counter != len(df):
	#store all rows from 'main name' into get_name dictionary
	get_name[f'key{counter}'] = df.at[counter, 'main_name']
	counter += 1

while counter3 != len(get_name):
	print(f'Position {counter3}: Finding {get_name.get(f"key{counter3}")}')
	print('\n')
	get_filtered_result = df3[df3['entity_name'].apply(str).str.fullmatch(get_name.get(f"key{counter3}"),na=False,case=False)]
	if not get_filtered_result.empty:
		print(get_filtered_result)
		with open('get_uen.csv', 'a') as myfile:
			myfile.write(f'Result for {get_name.get(f"key{counter3}")}\n')
			myfile.write(f'{get_filtered_result}')
			myfile.write('\n\n\n')
	else:
		print("Not found.. :(")
		with open('get_uen.csv', 'a') as myfile:
			myfile.write(f'Result for {get_name.get(f"key{counter3}")}\n')
			myfile.write("No result")
			myfile.write('\n\n\n')
	print("-"*50)
	print('\n\n\n')
	counter3 += 1
