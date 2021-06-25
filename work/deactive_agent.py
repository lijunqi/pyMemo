
###### To deactivate an Automation Agent so that you can schedule its executions in qTest ######
# POST /api/v3/projects/{projectId}/automation/hosts/{host_server_Id}/agents/{agent_server_id}/deactivate


import requests
from qtest_helper import *


host_server_id = '3297' # stex-dev02

project_id = '86683' # TAF
agent_id = '6775'
#project_id = '91273' # AOP
#agent_id = '6776'
#project_id = '87189' # Common Install
#agent_id = '8247'

full_url = url + f"/api/v3/projects/{project_id}/automation/hosts/{host_server_id}/agents/{agent_id}/deactivate"
with requests.Session() as sess:
    r = sess.post(full_url, headers=headers)
print(r.status_code)
print(r.content)
#print(r.json())