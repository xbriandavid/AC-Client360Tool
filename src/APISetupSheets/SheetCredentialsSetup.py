from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
import json

class SheetsCredentialConnectorService:

    def __init__(self, configFile):
        self.configfile = configFile

    def credentialSetUp(self):
        billing_project_credential_json = open(self.configfile)
        billing_project_account = json.load(billing_project_credential_json)
        credentials = service_account.Credentials.from_service_account_info(billing_project_account)
        scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/spreadsheets'])
        return scoped_credentials

class SheetsCredentialConnectorConsumer:

    def __init__(self, CredentialConnector):
        self.credentialconnector = CredentialConnector
    def activate(self):
        
        credentials = self.credentialconnector.credentialSetUp()
        try:
            service = build('sheets', 'v4', credentials=credentials)
            return service
        except HttpError as error:
            return None