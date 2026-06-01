def show_details(**kwargs):
	for key, value in kwargs.items():
		print( key, ": ",value)
show_details( name="RAFEEF", age=20, city="Calicut")