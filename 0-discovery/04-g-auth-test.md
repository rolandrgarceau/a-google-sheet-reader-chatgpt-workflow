#### High level scope for a simple sheet download app

Its amazing how challenging a "simple" programmatic download of a Google Sheet is. In a nutshell we are simply looking to create a script to download a sheet from a storage device somewhere out there in the great abyss, and get it on a local dev machine, not executing on a thin client or dummy machine on GCP resources, but there is a tutorial for that in a minute. 

There's all sorts of ways to quickly do this. jupyter-naas was high on the search, but low in the following, and less on the stats. So what do we do when the deadline is tomorrow am? Don't take the job? Use AI?  

### [How Application Default Credentials works](https://cloud.google.com/docs/authentication/application-default-credentials)

ADC is a strategy used by the Google authentication libraries to automatically find credentials based on the application environment.

### [google-auth](https://googleapis.dev/python/google-auth/latest/user-guide.html)

From chatGPT we installed a few modules for OAuth credentials to access Google Sheets API. The AI response did not work out of the box, go figure. It's better than a wiki search though.

The documentation begins saying if your application needs specific scopes... this looks like the AI gen params to the non existent method for Credentials object could be close. 

#### Steps to recreate g_auth_test1.py

```py

import google.auth

credentials, project = google.auth.default()

print (credentials)
```

Output could not automagically determine credentials from my environment! That's good. Is it security through obscurity?

```
Please set GOOGLE_APPLICATION_CREDENTIALS or explicitly create credentials and re-run the application. For more information, please see https://cloud.google.com/docs/authentication/getting-started
```

### From output error link above

We need ADC (Application Default Credentials to authenticate an application with Google today). [This](https://cloud.google.com/docs/authentication/provide-credentials-adc) is how to set it up for use by Cloud Client Libraries, Google API Client Libraries, and the REST and RPC APIs in a variety of environments. [Here](How Application Default Credentials works) is how ADC works.

The authentication libraries then make those credentials available to Cloud Client Libraries and Google API Client Libraries. The client libraries use the credentials to authenticate to Google Cloud APIs. When we set up ADC and use a client library, our code can run in either a development or production environment without changing how the application authenticates to Google Cloud services and APIs.

ADC searches for credentials in the following locations:

1. GOOGLE_APPLICATION_CREDENTIALS environment variable
2. User credentials set up with the Google Cloud CLI
3. The attached service account, as provided by the metadata server

#### Low Level Scope

So we need to provide credentials to ADC. How we provide credentials to ADC depends on where our code is running. 

For this we are simply using a local workstation with a local development environment, and the recommended way is with user credentials. We can use the Google Cloud CLI.

#### [Authenticating by using client libraries, the gcloud CLI, or Terraform](https://cloud.google.com/iam/docs/using-workload-identity-federation#generate-automatic)

These 3 can automatically obtain external credentials, and use these credentials to impersonate a service account. To let libraries and tools complete this process, we have to provide a credential configuration file. This file defines the following:

- Where to obtain external credentials from
- Which workload identity pool and provider to use
- Which service account to impersonate

unlike a service account key, a credential configuration file doesn't contain a private key and doesn't need to be kept confidential. Details about the credential configuration file are available at https://google.aip.dev/auth/4117.

#### Conclusion

Yet again, not all necessary for Workspaces API integration, but worth a once over just to re-familiarize with key concepts.