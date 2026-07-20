# replacing dates with different date formats with standard format
import re

text = "The project started on 3/14/2030. The first review took place on 03-28-2030, followed by another meeting on 2030/4/7. The deadline was moved to 5-12-2030, and the final presentation was scheduled for 2030/06/21. All documents must be submitted by 7/1/2030."

# wrong date formats: 3/14/2030 | 04-14-2030 | 2030/3/14 | 14.03.2030

patternObj = re.compile(r'(\d\d?\d?\d?).(\d\d?\d?\d?).(\d\d?\d?\d?)') # or \d{1,4}

formatedDates = patternObj.sub(r'\1/\2/\3', text)
print(formatedDates)


