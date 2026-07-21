# replacing dates with different date formats with standard format
import re

text = "The project started on 3/14/2030. The first review took place on 03-28-2030, followed by another meeting on 2030/4/7. The deadline was moved to 5-12-2030, and the final presentation was scheduled for 2030/06/21. All documents must be submitted by 7/1/2030."

# wrong date formats: 3/14/2030 | 2030/4/7 | 7/1/2030 | 2030/06/21 | 5-12-2030 | 03-28-2030

allDates = re.compile(
    r'(\d{4}).(\d{1,2}).(\d{1,2})'
    r'|'
    r'(\d{1,2}).(\d{1,2}).(\d{4})')


def correctedDates(match):
    if match.group(1):
        year, month, day = match.group(1, 2, 3)
    else:
        month, day, year = match.group(4, 5, 6)
    return f"{int(day):02d}/{int(month):02d}/{int(year):04d}"

allCorrectedDates = allDates.sub(correctedDates, text)
print(allCorrectedDates)

# HOLYYY JESUSSSSSS I DID ITTT OMG


