import json
import pandas as pd

# this module takes in a CSV file and parses its elements into a list of JSON objects for batch processing

# Organisations: name, domain_names, details, notes, merchant_id, tags
# Users: name, email, organization_id, role, active, notes, group, api_subscription, employee_id, promotion_code, tags


class ListParser:

    @staticmethod
    def create_orgs(filepath):
        data = pd.read_csv(filepath) # Placeholder filepath

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

    @staticmethod
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

    @staticmethod
    def create_tickets(filepath):
        data = pd.read_csv(filepath)  # Placeholder filepath

        payloads = []
        output = {}
        output['tickets'] = []

        # Tickets: assignee_id, created_at, subject, description, status, submitter_id, requester_id, updated_at, due_at, about,
        #          business name, dept, emp id, product information, start date, subscription, tags

        for row in data.itertuples(index=False):
            page_count = 0
            output['tickets'].append(
                {
                    "assignee_id": int(row[data.columns.get_loc('assignee_id')]) if pd.isnull(row[data.columns.get_loc('assignee_id')]) == False else '',
                    "created_at": row[data.columns.get_loc('created_at')] if pd.isnull(row[data.columns.get_loc('created_at')]) == False else '',
                    "subject": row[data.columns.get_loc('subject')] if pd.isnull(row[data.columns.get_loc('subject')]) == False else '',
                    "description": row[data.columns.get_loc('description')] if pd.isnull(row[data.columns.get_loc('description')]) == False else '',
                    "status": row[data.columns.get_loc('status')] if pd.isnull(row[data.columns.get_loc('status')]) == False else '',
                    "submitter_id": row[data.columns.get_loc('submitter_id')] if pd.isnull(row[data.columns.get_loc('submitter_id')]) == False else '',
                    "requester_id": row[data.columns.get_loc('requester_id')] if pd.isnull(row[data.columns.get_loc('requester_id')]) == False else '',
                    "updated_at": row[data.columns.get_loc('updated_at')] if pd.isnull(row[data.columns.get_loc('updated_at')]) == False else '',
                    "custom_fields": [
                        {"about": row[data.columns.get_loc('about')] if pd.isnull(row[data.columns.get_loc('about')]) == False else ''},
                        {"business name": row[data.columns.get_loc('business name')] if pd.isnull(row[data.columns.get_loc('business name')]) == False else ''},
                        {"dept": row[data.columns.get_loc('dept')] if pd.isnull(row[data.columns.get_loc('dept')]) == False else ''},
                        {"emp id": row[data.columns.get_loc('emp id')] if pd.isnull(row[data.columns.get_loc('emp id')]) == False else ''},
                        {"product information": row[data.columns.get_loc('product information')] if pd.isnull(row[data.columns.get_loc('product information')]) == False else ''},
                        {"start date": row[data.columns.get_loc('start date')] if pd.isnull(row[data.columns.get_loc('start date')]) == False else ''},
                        {"subscription": row[data.columns.get_loc('subscription')] if pd.isnull(row[data.columns.get_loc('subscription')]) == False else ''},
                    ],
                    "tags": row[data.columns.get_loc('tags')] if pd.isnull(row[data.columns.get_loc('tags')]) == False else ''
                }
            )
            if len(output['tickets']) == 100:
                payloads.append(json.dumps(output))
                output = {"tickets": []}
                page_count += 1
                print('payload pagination count is currently ', page_count)

        if output['tickets']:
            payloads.append(json.dumps(output))

        return payloads
        # with open('tickets.json', 'w') as outfile:
        #     json.dump(output, outfile, ensure_ascii=False,indent=4)

    # create_users("V:\\Adulting\\Job Hunting\\ZenDesk\\users.csv")
    # create_tickets("V:\\Adulting\\Job Hunting\\ZenDesk\\tickets.csv")