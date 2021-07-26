import json
import pandas as pd

# this module takes in a CSV file and parses its elements into a list of JSON objects for batch processing

# Organisations: name, domain_names, details, notes, merchant_id, tags
# Users: name, email, organization_id, role, active, notes, group, api_subscription, employee_id, promotion_code, tags
# Tickets: assignee_id, created_at, subject, description, status, submitter_id, requester_id, updated_at, due_at, about,
#          business name, dept, emp id, product information, start date, subscription, tags

data = pd.read_csv("V:\Adulting\Job Hunting\ZenDesk\organizations.csv")


payloads = []
output = {

}
output['orgs'] = []

for row in data.itertuples(index=False):
    page_count = 0
    output['orgs'].append(
        {
            "name": row[data.columns.get_loc('name')] if pd.isnull(row[data.columns.get_loc('name')]) == False else '',
            "domain_names": row[data.columns.get_loc('domain_names')] if pd.isnull(row[data.columns.get_loc('domain_names')]) == False else '',
            "details": row[data.columns.get_loc('details')] if pd.isnull(row[data.columns.get_loc('details')]) == False else '',
            "notes": row[data.columns.get_loc('notes')] if pd.isnull(row[data.columns.get_loc('notes')]) == False else '',
            "organization_fields": {
                "merchant_id": row[data.columns.get_loc('merchant_id')] if pd.isnull(row[data.columns.get_loc('merchant_id')]) == False else '',
            },
            "tags": row[data.columns.get_loc('tags')] if pd.isnull(row[data.columns.get_loc('tags')]) == False else '',
        }
    )
    if len(output['orgs']) == 100:
        payloads.append(json.dumps(output))
        output = {"orgs": []}
        page_count += 1
        print('payload pagination count is currently ', page_count)

if output['orgs']:
    payloads.append(json.dumps(output))

print(payloads)
# Users JSON format
#         {
#             "verified": true,
#             "active": true,
#             "email": '',
#             "name": '',
#             "notes": '',
#             "organization_id": '',
#             "role": '',
#             "tags": '',
#             "user_fields": {
#                 "group": '',
#                 "api_subscription": '',
#                 "employee_id": '',
#                 "promotion code": ''
#             }

def create_users():
    # JSON scaffolding
    payload = {}
    payload['users'] = []


tickets = {

}