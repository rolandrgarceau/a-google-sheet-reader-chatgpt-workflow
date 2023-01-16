### Python Quickstart [here]()

Get a working basic script first, then modify for short lived expiries.

### [OAuth client ID Credentials](https://developers.google.com/workspace/guides/create-credentials#desktop-app)

Apps running on multiple platforms need a separate client ID for each platform. The test2.py file flow is for desktop applications, and credentials will need to be created for this workflow. 

### Sheets API exploration

If allowing Google APIs Explorer, we may wish to disable this feature in the future, as to not allow access to drive information.

- Login to console.cloud.google.com.
- pin workspaces to navigation pane.
- click into workspaces navigation section, and make sure the current project we have created is selected up top.
- verify credentials exist for the project.
- gcloud auth application-default login should present a successful login https://cloud.google.com/sdk/auth_success
- In product Library click into the Sheet API.


### Sheets [Samples](https://developers.google.com/sheets/api/samples)

Don't handle Python.

#### How to use [gRPC Transcoding](https://google.aip.dev/127) for requests

#### gcloud auth application-default login

Saves credentials at ~/.config/gcloud/application_default_credentials.json 

These credentials will be used by any library that requests Application Default Credentials (ADC).

#### Scope

```raise HttpError(resp, content, uri=self.uri)
googleapiclient.errors.HttpError: <HttpError 403 when requesting https://sheets.googleapis.com/v4/spreadsheets/1234567long_spreadsheet_id/values/A1%3AY1?alt=json returned "Request had insufficient authentication scopes.". Details: "[{'@type': 'type.googleapis.com/google.rpc.ErrorInfo', 'reason': 'ACCESS_TOKEN_SCOPE_INSUFFICIENT', 'domain': 'googleapis.com', 'metadata': {'service': 'sheets.googleapis.com', 'method': 'google.apps.sheets.v4.SpreadsheetsService.GetValues'}}]"
```
Found [here](https://developers.google.com/identity/protocols/oauth2/scopes), This is a scope:

https://www.googleapis.com/auth/spreadsheets.readonly


