import Switchboard
import ListParser


class DataManger:
    def __init__(self):
        self.email_address = ''
        self.pwd = ''
        self.datatype = ''
        self.filepath = ''
        self.payloads = ''
        self.last_response = None

    def set_auth(self, email, password):
        self.email_address = email
        self.pwd = password

    def set_datatype(self, selection):
        self.datatype = selection

    def set_filepath(self, filepath):
        self.filepath = filepath

    def set_payloads(self):
        self.payloads = None

        # this could probably refactored in a way that takes advantage of a lambda function, but this
        # is good enough for reaching MVP for now
        if self.datatype == 'Organizations':
            self.payloads = ListParser.create_orgs(self.filepath)
        elif self.datatype == 'Users':
            self.payloads = ListParser.create_users(self.filepath)
        elif self.datatype == 'Tickets':
            self.payloads = ListParser.create_tickets(self.filepath)

    def send_to_api(self):
        # TODO - needs proper error handling in case of malformed data
        if not self.last_response is None:
            self.last_response = None

        self.last_response = Switchboard.send_data(self.datatype, self.email_address, self.pwd, self.payloads)

    def get_last_response(self):
        return self.last_response
