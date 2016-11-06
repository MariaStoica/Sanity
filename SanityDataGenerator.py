# Sanity Data Generator for development purposes
from datetime import datetime
import random

# data
numberOfTimepieces = 5
daysInEachTimepiece = [46, 34, 12, 32, 56]
maxNumberOfActivitiesInADat = 14
daysInAYear = 365

results = ['Satya called to thank me',
		   'Invitation to speak',
		   'Received the ABIE Award',
		   'Anna Patterson invited me for coffee',
		   'Investors keep calling to offer me money']

moodCodes = ['trigger',
			 'happy',
			 'default',
			 'frustrated',
			 'chaos',
			 'sad',
			 'pit']

# helper methods
def ToMyDate(dayOfYear):
	return datetime.strptime('2016 '+str(dayOfYear), '%Y %j').strftime('%d %b %Y')

# let the generation begin!
destinationFilePath = './SanityData.xml'
generated = "<Root>"
indexDay = 3

for index in range(numberOfTimepieces):
	generated += '<Timepiece name="Timepiece {0}">\n'.format(index)

	generated += '\t<StartDate date="{0}"/>\n'.format(ToMyDate(indexDay))
	generated += '\t<EndDate date="{0}"/>\n'.format(ToMyDate(indexDay + daysInEachTimepiece[index]))
	generated += '\t<Activities>\n'

	for day in range(daysInEachTimepiece[index]):
		generated += '\t\t<Day date="{0}">\n'.format(ToMyDate(indexDay + day))

		generated += '\t\t\t<Mood code="{0}"/>\n'.format(moodCodes[random.randint(0,6)])

		for a in range(random.randint(1,maxNumberOfActivitiesInADat)):
			typeOfActivity = random.randint(1,3)
			if typeOfActivity == 1:
				generated += '\t\t\t<Activity name="activity {0}"/>\n'.format(a)
			elif typeOfActivity == 2:
				generated += '\t\t\t<ImportantActivity name="imp activity {0}"/>\n'.format(a)
			elif typeOfActivity == 3:
				generated += '\t\t\t<Result name="{0}"/>\n'.format(results[a % 5])
		
		generated += '\t\t</Day>\n'
	
	generated += '\t</Activities>\n'
	
	generated += "</Timepiece>\n"
	indexDay += daysInEachTimepiece[index] + 14

generated += "</Root>"
print(generated)

destinationFile = open(destinationFilePath, 'w')
destinationFile.write(generated)
destinationFile.close()


