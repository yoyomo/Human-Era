currentYear = 2017
yearWeShouldBeIn = 12017
firstYearDiff = yearWeShouldBeIn - currentYear
firstYear = 0
for BC in reversed(range(0,10000+1)):
	HE = firstYear + firstYearDiff - BC
	print str(BC)+'BC\t'+ str(HE) +'HE'





