import json
from datetime import datetime

with open('C:\\suryas\\tech_stack_eol_tracking\\eol_tracking\\informatica.json') as f:
    data = json.load(f)

d = datetime.strptime(data[0]['minimum_support_period'], '%B %d, %Y')
print(d.strftime('%Y-%m-%d'))