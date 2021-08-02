from pprint import pprint

import numpy as np

import Switchboard
import ListParser


class DataManger:
    def __init__(self):
        self.email_address = ''
        self.pwd = ''
        self.datatype = ''
        self.filepath = ''
        self.payloads = ''

    def set_auth(self, email, password):
        self.email_address = email
        self.pwd = password

    def set_datatype(self, selection):
        self.datatype = selection

    def set_filepath(self, filepath):
        self.filepath = filepath

    def set_payloads(self):
        self.payloads = None

        if self.datatype == 'Organizations':
            self.payloads = ListParser.create_orgs(self.filepath)
        elif self.datatype == 'Users':
            self.payloads = ListParser.create_users(self.filepath)
        elif self.datatype == 'Tickets':
            self.payloads = ListParser.create_tickets(self.filepath)

    # result = Switchboard.send_data(datatype, user, pwd, payloads)
