# Importerhouse

Importerhouse is an application which imports .csv files to a Zendesk instance using Zendesk's API.

To use:
- open ./UI/DataMigrationTool.py
- click "browse" to select the location of the .csv file for import
- select the type of data (Organizations, Users, Tickets) from the dropdown menu
- enter the email address and password associated with your Zendesk account
- all fields are required; make sure they're filled.
- click "submit"

upon completion, you should receive a popup that informs you whether the import was successful or not.

Known issues:
- application crashes when csv fields don't match up with data type selected in dropdown
- doesn't yet handle updating organizations or tickets already found in Zendesk instance
