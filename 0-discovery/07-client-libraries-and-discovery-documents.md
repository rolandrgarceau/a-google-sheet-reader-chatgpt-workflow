### [Cloud Client Libraries](https://cloud.google.com/apis/docs/cloud-client-libraries)

There are two types of client libraries available: Cloud Client Libraries and Google API Client Libraries. Both types support Application Default Credentials. 

The key takeaway here should be that client libraries provide simplifications that significantly reduce the amount of code we need to write.

Cloud Client Libraries use the latest client library model. It provides code that does a common task in a common way, with a consistent style, and even may go as far as handling the low-level details of communication with the server, like authenticating with Google. For python we can use `pip` to install this. Performance benefits may happen by using [gRPC APIs](https://cloud.google.com/apis/docs/client-libraries-explained#grpc_apis). For now just get something functional and worry about optimization later. 

A few Google Cloud APIs don't have Cloud Client Libraries available in all languages. Firebase mobile platform is the new way to steer towards for applications. 

### [Install Client Libraries](https://developers.google.com/sheets/api/guides/libraries#python)

#### [PyDoc reference for the Google Sheets API](https://googleapis.github.io/google-api-python-client/docs/dyn/sheets_v4.html)

#### [Developer's guide for the Google API Client Library for Python](https://developers.google.com/api-client-library/python)

### [Authenticate to Cloud services using client libraries](https://cloud.google.com/docs/authentication/client-libraries)

The link above finally touches on Application Default Credentials (ADC) after seeing that in the original iteration with chatgpt. 

### [Browser interface for API](https://developers.google.com/apis-explorer/#p/sheets/v4/) using the APIs Explorer for the Google Sheets API

### [Discovery Documents](https://developers.google.com/discovery/v1/reference/apis)

Discovery documents are available for specific versions of most APIs. Each API's Discovery Document describes the surface of the API, how to access the API and how API requests and responses are structured. The information provided by the discovery document includes API-level properties such as an API description, resource schemas, authentication scopes, and methods.

The Discovery document focuses on the RESTful method of invoking an API. The discovery.apis.list method returns the list of all APIs supported by the Google APIs Discovery Service including the urls for retrieving the REST-based discovery documents. 

There exists a bit for auth here:
|---|---|---|
auth	|object|	Authentication information.	
auth.oauth2|object|	OAuth 2.0 authentication information.	
auth.oauth2.scopes	|object|	Available OAuth 2.0 scopes.	
auth.oauth2.scopes.(key)	|object|	The scope value.	
auth.oauth2.scopes.(key).description	|string|	Description of scope.