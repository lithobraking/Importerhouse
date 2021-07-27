import json
import pandas as pd

# this module takes in a CSV file and parses its elements into a list of JSON objects for batch processing

# Organisations: name, domain_names, details, notes, merchant_id, tags
# Users: name, email, organization_id, role, active, notes, group, api_subscription, employee_id, promotion_code, tags
# Tickets: assignee_id, created_at, subject, description, status, submitter_id, requester_id, updated_at, due_at, about,
#          business name, dept, emp id, product information, start date, subscription, tags

class Data_parser:
    def create_orgs(filepath):
        data = pd.read_csv("V:\Adulting\Job Hunting\ZenDesk\organizations.csv") # Placeholder filepath

        payloads = []
        output = {}
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
                    "tags": row[data.columns.get_loc('tags')] if pd.isnull(row[data.columns.get_loc('tags')]) == False else [],
                }
            )
            if len(output['orgs']) == 100:
                payloads.append(json.dumps(output))
                output = {"orgs": []}
                page_count += 1
                print('payload pagination count is currently ', page_count)

        if output['orgs']:
            payloads.append(json.dumps(output))

        return payloads
    # Users JSON format


    def create_users(filepath):
        data = pd.read_csv(filepath)  # Placeholder filepath

        payloads = []
        output = {}
        output['users'] = []

        for row in data.itertuples(index=False):
            page_count = 0
            output['users'].append(
                {
                    "verified": True,
                    "active": True,
                    "email": row[data.columns.get_loc('email')] if pd.isnull(row[data.columns.get_loc('email')]) == False else '',
                    "name": row[data.columns.get_loc('name')] if pd.isnull(row[data.columns.get_loc('name')]) == False else '',
                    "notes": row[data.columns.get_loc('notes')] if pd.isnull(row[data.columns.get_loc('notes')]) == False else '',
                    "organization_id": row[data.columns.get_loc('organization_id')] if pd.isnull(row[data.columns.get_loc('organization_id')]) == False else '',
                    "role": row[data.columns.get_loc('role')] if pd.isnull(row[data.columns.get_loc('role')]) == False else '',
                    "tags": row[data.columns.get_loc('tags')] if pd.isnull(row[data.columns.get_loc('tags')]) == False else [],
                    "user_fields": {
                        "group": row[data.columns.get_loc('group')] if pd.isnull(row[data.columns.get_loc('group')]) == False else '',
                        "api_subscription": row[data.columns.get_loc('api_subscription')] if pd.isnull(row[data.columns.get_loc('api_subscription')]) == False else '',
                        "employee_id": row[data.columns.get_loc('employee_id')] if pd.isnull(row[data.columns.get_loc('employee_id')]) == False else '',
                        "promotion code": row[data.columns.get_loc('promotion_code')] if pd.isnull(row[data.columns.get_loc('promotion_code')]) == False else ''
                    }
                }
            )
            if len(output['orgs']) == 100:
                payloads.append(json.dumps(output))
                output = {"orgs": []}
                page_count += 1
                print('payload pagination count is currently ', page_count)

        if output['orgs']:
            payloads.append(json.dumps(output))

        return payloads
        # with open('users.json', 'w') as outfile:
        #     json.dump(output, outfile, ensure_ascii=False,indent=4)

