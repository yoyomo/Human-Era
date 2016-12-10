##HE true variables
currentYear = 2017

firstYearDiff = 10000
yearWeShouldBeIn = currentYear + firstYearDiff
firstYear = 0

f = open('HE.txt','w')
f.write('Current Gregorian Year: '+str(currentYear)+'\n')
f.write('Year we should be in: '+ str(yearWeShouldBeIn)+'\n')
f.write('\nList of years past in their Human Era(HE) format:\n\n')

##BC to HE
for BC in reversed(range(0,firstYearDiff+1)):
	HE = firstYear + firstYearDiff - BC
	f.write( str(BC)+'BC\t'+ str(HE) +'HE\n')

##AD to HE
for AD in range(0,currentYear+1):
	HE = AD + firstYearDiff
	f.write(str(AD)+'AD\t'+ str(HE) +'HE\n')



