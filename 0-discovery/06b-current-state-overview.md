### At this point

So far we have read into Google documentation of varying contexts regarding authentication and authorization. We installed the chatGPT recommended libraries before gcloud CLI, but this did not seem to come with negative consequences (so far, fingers crossed). 

Prior to the CLI install we specified a project created in a browser from workspaces where we enabled Sheets API, creating a client id and secret which was downloaded as a .json file. There were tag issues with names and automatically made ones- see the 02_ document...

We have accomplished:

- Installed gcloud CLI 
- ran a `glcoud init` 
- performed a gcloud config list which outputted:
```
[core]
account = rudy@rudy-garceau.info
disable_usage_reporting = True
project = xenon-height-372215
```

It is not clear if this process was sufficient to use in a python script to attach credentials to forward to a gateway that would allow an actual sheet to be downloaded yet. 

Output of the init also mentioned a .boto configuration file was created and to check storage configuration for Google Cloud. It may be worth noting what the boto3 core configuration file is for AWS so we do not have conflicts moving forward.

Speaking of AWS, if we need to access resources from a workload that runs outside of Google Cloud, such as on Amazon Web Services (AWS) or Microsoft Azure, consider using workload identity federation instead of service account keys. 

#### Federated option worth mentioning

Federation lets your workloads access resources directly, using a short-lived access token, and eliminates the maintenance and security burden associated with service account keys.

### Auth from a bigger picture

There are several ways to create, save, retrieve, and use credentials. Spread out documentation is challenging sometimes to draw solutions from.

Permissions to access Sheets API may not be granted in the same way we grant access to Google Cloud.

To grant authorization to the gcloud CLI to access Google Cloud, we use either a user account or a service account. However we seen above there is Federated ways to issue short lived tokens instead of managing service keys. We need to verify this is possible with the Sheets API.

For applications we also can appreciate the default credentials. These all fall under an umbrella of having permissions to perform things like GET and POST, however without a seasoned vet that has been doing this very thing on GCP or more specifically through workspaces and/or gdrive for the past 12 months, we have to dig for more answers.

### [Provide credentials for Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc)

This may not at all involve service account keys. We need to fact check this.

ADC is the strategy that Google authentication libraries automatically use to find credentials based on the application environment. The authentication libraries then make those credentials available to Cloud Client Libraries and Google API Client Libraries. 

The client libraries use the credentials to authenticate to Google Cloud APIs. When setting up ADC and use a client library, your code can run in either a development or production environment without changing how your application authenticates to Google Cloud services and APIs.

```zsh
gcloud auth application-default login
```

#### Service Account 

The browser means to enable service accounts start at the iam-admin page selecting the project in question. 

There is a separate page to follow to [create a service account key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating). The script 06c_creste_service_account_key.py may have encountered a silent fail due to not having the IAM API enabled yet.

[Create and manage service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)

#### Other helpful commands

To authorize gcloud CLI to access Google Cloud using an existing service account while also specifying a project, run:

```zsh
gcloud auth activate-service-account SERVICE_ACCOUNT@DOMAIN.COM --key-file=/path/key.json --project=PROJECT_ID

```
To allow gcloud (and other tools in Google Cloud CLI) to use service account credentials to make requests, use this command to import these credentials from a file that contains a private authorization key, and activate them for use in gcloud. gcloud auth activate-service-account serves the same function as gcloud auth login but uses a service account rather than Google user credentials.