import requests
from datetime import datetime, timezone
import time

# GET /api/v3/automation/hosts/{host_server_Id}/jobs

# Note:
# 1. Only jobs with status PLANNED and NOT RUN are retrieved.
# 2. Request parameters need to be reformatted to yyyy-mm-dd[T]hh:mm:ss+[timezone]. For example: 2015-04-28T17:00:00+0700
# 3. After being reformatted, they need to be encoded.

# Request parameter:
# Parameter     Required    Description
# start_date    false       This is the lower bound for the jobs' scheduled time.
#                           If it is specified, the Automation Host will not retrieve the jobs whose scheduled time is prior to this.
# end_date      yes         This is the upper bound for the jobs' scheduled time.
#                           The Automation Host will only retrieve the jobs whose scheduled time is prior this specified time.


token = "Bearer b44216a0-73ff-42cd-b56d-aaebbbf8c791"
host_server_id = '3297'

headers = {'Authorization': token, 'accept': 'application/json', 'content-type': 'application/json', 'charset': 'UTF-8'}


end_date = datetime.now().replace(microsecond=0).replace(tzinfo=timezone.utc).isoformat()

full_url = f"https://ra.qtestnet.com/api/v3/automation/hosts/{host_server_id}/jobs"
payload = { 'start_date': end_date, 'end_date': end_date}
t1 = time.time()
r = requests.get(full_url, headers=headers, params=payload)
t2 = time.time()
print('Elapsed Time: ', t2 - t1)
print(r.status_code)
print(r.content)
