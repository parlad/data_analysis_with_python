import json
import pandas as pd

path = '/Users/praladneupane/Documents/python/0636920023784/data/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path, 'rb')]

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print(pd.DataFrame(time_zones, columns=["City"]))