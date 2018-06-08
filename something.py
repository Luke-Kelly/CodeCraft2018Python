print("What year were you born?")
born = raw_input()
born = int(born)
print("What year would you like to see your age?")
year = raw_input()
year = int(year)
ageIn2050 = year - born
print("In " + str(year) + " you will be " + str(ageIn2050) + " years old!")
