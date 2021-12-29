import pandas
import warnings
warnings.filterwarnings("ignore", 'This pattern has match groups')

i=0
get_data={}
get_data2={}
counter=counter2=counter3=0
df = pandas.read_csv('entities-registered-with-acra.csv', dtype=str)
df2 = pandas.read_csv('input.csv', dtype=str)
columns = ['entity_name','reg_postal_code']
newdf = pandas.DataFrame(df, columns=columns)

while counter2 != len(df2):
	get_data2[f'key{counter2}'] = df2.at[counter2, 'main_name']
	counter2 +=1


while counter3 != len(get_data2):
	get_filter = newdf[newdf['entity_name'].str.contains(get_data2.get(f"key{counter3}"),na=False,case=False)]
	print(f'Position {counter3}: Finding {get_data2.get(f"key{counter3}")}')
	with open('get_postal_code.csv', 'a') as myfile:
		myfile.write(f'Finding {get_data2.get(f"key{counter3}")}\n\n')
	split_key=get_data2.get(f'key{counter3}').split()
	if get_filter.empty and len(split_key) > 3:
		retry=" ".join(split_key[0:3])
		new_retry=retry.replace("(","(")
		if "(" in new_retry and new_retry.count(")") == 0:
			new_retry+=")"
		else:
			new_retry=retry.replace(")",")")
		print(f'\n\nNot Found: {get_data2.get(f"key{counter3}")}. Searching for {new_retry} instead.\n\n')
		get_filter2 = newdf[newdf['entity_name'].str.contains(f'{new_retry}',na=False,case=False)]
		if get_filter2.empty:
			retry_again=" ".join(split_key[0:2])
			new_retry_again=retry_again.replace("(","(")
			if "(" in new_retry_again and new_retry_again.count(")") == 0:
				new_retry_again+=")"
			else:
				new_retry_again=retry_again.replace(")",")")
			print(f'\n\nNot Found: {retry}. Searching for {new_retry_again} instead.\n\n')
			get_filter_again = newdf[newdf['entity_name'].str.contains(f'{new_retry_again}',na=False,case=False)]
			if get_filter_again.empty:
				print(f'Not Found\n\n\n')
				with open('get_postal_code.csv', 'a') as myfile:
					myfile.write(f'Not Found\n\n\n')
			else:
				print(f'Found {get_filter_again}\n\n\n')
				with open('get_postal_code.csv', 'a') as myfile:
					myfile.write(f'Found {get_filter_again}\n\n\n')
		else:
			print(f'Found {get_filter2}\n\n\n')
			with open('get_postal_code.csv', 'a') as myfile:
				myfile.write(f'Found: {get_filter2}\n\n\n')
	elif get_filter.empty and len(split_key) == 3:
		retry_a=" ".join(split_key[0:2])
		new_retry_a=retry_a.replace("(","(")
		if "(" in new_retry_a and new_retry_a.count(")") == 0:
			new_retry_a+=")"
		else:
			new_retry_a=retry_a.replace(")",")")
		print(f'\n\nNot Found: {get_data2.get(f"key{counter3}")}. Searching for {new_retry_a} instead.\n\n')
		get_filter_a = newdf[newdf['entity_name'].str.contains(f'{new_retry_a}',na=False,case=False)]
		if get_filter_a.empty:
			print(f'Not Found\n\n\n')
			with open('get_postal_code.csv', 'a') as myfile:
				myfile.write(f'Not Found\n\n\n')
		else:
			print(f'Found {get_filter_a}\n\n\n')
			with open('get_postal_code.csv', 'a') as myfile:
				myfile.write(f'Found: {get_filter_a}\n\n\n')
	elif get_filter.empty and len(split_key) == 2:
		retry3=" ".join(split_key[0:1])
		new_retry_3=retry3.replace("(","(")
		if "(" in new_retry_3 and new_retry_3.count(")") == 0:
			new_retry_3+=")"
		else:
			new_retry_3=retry3.replace(")",")")
		print(f'\n\nNot Found: {get_data2.get(f"key{counter3}")}. Searching for {new_retry_3} instead.\n\n')
		get_filter4 = newdf[newdf['entity_name'].str.contains(f'{new_retry_3}',na=False,case=False)]
		if get_filter4.empty:
			print(f'Not Found\n\n\n')
			with open('get_postal_code.csv', 'a') as myfile:
				myfile.write(f'Not Found\n\n\n')
		else:
			print(f'Found {get_filter4}\n\n\n')
			with open('get_postal_code.csv', 'a') as myfile:
				myfile.write(f'Found: {get_filter4}\n\n\n')
	elif get_filter.empty and len(split_key) == 1:
		print(f'Not Found: {get_filter}\n\n\n')
	else:
		print(f'Found: {get_filter}\n\n\n')
		with open('get_postal_code.csv', 'a') as myfile:
			myfile.write(f'Found: {get_filter}\n\n\n')
	counter3 +=1
