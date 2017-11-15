import calendar
from sys import argv , exit

month_dict = {  '1':'January','2':'February','3':'March','4':'April',
                '5':'May','6':'June','7':'July','8':'August',
                '9':'September','10':'October','11':'November',
                '12':'December'
            }
#Eastern holydays missing
#Only national holydays are calculated
italian_holidays = {'January':['1','6'],'February':[],'March':[],'April':['25'],
                    'May':['1'],'June':['2'],'July':[],'August':['15'],
                    'September':[],'October':[],'November':['1'],
                    'December':['8','25','26']
                    }
try:
    year = int(argv[1])
except:
    print 'usage: {} <year>'.format(argv[0])
    exit(1)

month = 1
yearly_working_days = 0
monthly_working_days = {}
monthly_non_working_days = {}
calendar.setfirstweekday(calendar.MONDAY)
while month < 13:
    month_str = str(month)
    weekend = 0
    holidays_not_weekend = 0
    for day in calendar.monthcalendar(year,month):
        if day[6] != 0 and str(day[6]) not in italian_holidays[month_dict[month_str]]:
            weekend +=1
        if day[5] != 0 and str(day[5]) not in italian_holidays[month_dict[month_str]]:
            weekend +=1
    holidays_not_weekend += len(italian_holidays[month_dict[month_str]])
    yearly_working_days += calendar.monthrange(year,month)[1] - (weekend + holidays_not_weekend)
    monthly_working_days[month_str] = calendar.monthrange(year,month)[1] - (weekend + holidays_not_weekend)
    monthly_non_working_days[month_str] = weekend + holidays_not_weekend
    month +=1

for month in sorted(monthly_working_days.keys(),key=int):
    print month_dict[str(month)],year
    print 'Days             :',calendar.monthrange(year,int(month))[1]
    print 'Working days     :',monthly_working_days[month]
    print 'Non working days :',monthly_non_working_days[month],'\n'
#Workaround for Eastern holiday since it is always a Monday
print 'Total working days in {} : {}'.format(year,yearly_working_days -1)
