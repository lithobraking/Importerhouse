import requests

def get_endpoint(selection):
    try:
        endpoints = {
            'organizations': 'organizations/create_many',
            'users': 'users/create_many',
            'tickets': 'tickets/create_many'
        }
        return endpoints[selection]
    except LookupError:
        print('That selection does not exist.')

def send_data(datatype, username, password, payloads):
    session = requests.Session()
    url = 'https://z3n-platformdev-noble.zendesk.com/api/v2/' + get_endpoint(datatype)
    session.headers = {'Content-Type': 'application/json'}

    for payload in payloads:
        response = session.post(url, data=payload, auth=(username, password))
        if response.status_code != 200:
            print('Import failed! (Status: {})'.format(response.status_code))
            exit()
        print('Data imported successfully.')


