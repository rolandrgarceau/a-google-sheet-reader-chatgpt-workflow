### A Google Sheets Reader in Python

Here is an insight to the way one might attack a problem of unknowns. The prefixing 0x-xxx is discovery. 1-xxx passes authentication, and 2-xxx should satisfy the functional requirements for the not so distributed monolith we are building in real life.

#### Note on git and .gitignore

Coming from a security perspective, after some time not using gitlab or other high level open source distributed code management and Version Control System, to design with security in mind there are some very basic non-functional aspects of branching still not fixed within git itself- mainly in the use of keywords 'main' and 'master' branches when defining and using init from a pre-existing directory not part of VC. 

This should be noted that a git clone and other workflows are to be used when building pipelines, especially with very specific policy in their creation and distribution aspects. One can 'git' down a rabbit hole very quickly here. 

For security, I did not even write into the gitignore sensitive files to omit, as the priority is not on dissecting current git best practices, but to keep client information safe while still allowing outside observation. Files will be pushed from a private location on a need to know Zero Trust basis ;)

#### New School Mindsets and jargon to contemplate

Platform engineering uses a product approach. This enables the right amount of developer self-service and balances the right level of abstraction for individual organizations within teams. To be successful it combines user research, regular feedback and marketing best practices to better understand developers, create a platform that solves common problems and get internal buy-in from key stakeholders.

I keep seeing the this recurring theme today (Q1 2023): Is DevOops dead? People need good vision, proper planning within IT structure, and implementation strategies that complement business objectives. Life in the day with chronic fatigue of scope which a DevOps Professional might experience, could be as time consuming as understanding this repo. How long would it take your staff to get past this hurdle? Chances are a seasoned PM would be screaming about a 1099 for an SRE. I hope you believe in work/life balance and don't just spit it off the tongue to address an elephant in the room. There is a reason [PEMBOK guides](https://www.pmi.org/pmbok-guide-standards/foundational/pmbok) exist.

Topics such as these are for seasoned pros, however most are given the responsibility of it all when they demonstrate the bare minimum to do scopes such as this. Programming is complicated, even when we use AI to forward the package.

So, this directory also contains an initial probe test of ChatGPT to see if AI could fast track an authentication workflow for downloading a Google Sheet from Drive. Theres still a lot of learning to be had on both fronts.

#### TL;DR:

If one is not interested in how discovery might happen in modern development, skip the 0-xxx and everything below this line in this .md file, follow the 1-xxx, and 2-xxx prefixed files for authentication, authorization, and eventual script build to perform the "simple" duty of programmatically downloading a google sheet. 

06b-current-state-overview's first paragraph is a good summary for all the just probing around done before actually installing helpful utilities for interacting with Google.

The prefix 1-sheets-api.md starts my process of exploring the API itself after the python quickstart. That documentation mysteriously made itself available the day stackoverflow posted a response to an inquiry regarding current 403's encountered with OAuth and .credentials for obtaining short lived tokens to Access the sheets API.

### Discovery for Sheets API

The Sheets API offers a [5 step to get started](https://developers.google.com/workspace/guides/get-started) too, worthy of a read in context of what is required at a high level for authentication options. Specifics to functional  requirement completion at this latest update revolve around desktop authentication. More on authentication and authorization for Google Workspace APIs, found [here](https://developers.google.com/workspace/guides/auth-overview) may not pertain to other Google APIs. Follow their 9 step process for Workspaces specifics.

#### Pin Workspaces to console.cloud.google.com navigation

From navigation menu choose 'view all products' > 'Other Google Products' > and click pin the 'Workspaces'.

If we click into the Workspaces navigation we should see at the very top a current project that is selected, and the relative API's that are enabled for  that project.

In the credentials section we should see the enabled credentials that may be used for programmatic access. It should contain a client ID and secret which will be needed to obtain a short lived access token (there are other possibilities here) to be able to access a sheet with.

### Other Client API's 

There exists a `google-api-python-client` that encompasses all of the individual APIs from Google, and the install is larger than 50 MB. Each individual API often has teams that handle a more specific implementation for that API. We may find this useful when moving towards encompassing the whole CRM with GeoPandas and such visualizations and 3D plotting with cartopy.

See the 00-9-step-process.md
If we are moving into the CRM and topographical mapping, we may continue on the following preceding path. AquaTech will appreciate this. Is all of this wasted time if the entire tech an organization uses is located within their old gsuite understandings? This will work for them long term with their business strategy and planning.

The beginning to interact with an API requires a SDK for the language we wish to write in. That gets cost prohibitive in a non tech focused startup. 

AWS has Boto3 for python and friends, Google has a few too. It's probably not a bad idea to start with the latest and greatest authentication/authorization mechanisms. However, we must authorize the Google Cloud CLI to manage Google Cloud resources. Both Google Cloud CLI and Google Cloud use OAuth2 for authentication and authorization.

Oauth/AuthO was there in 2017 when I built some raffle applications with paypal and stripe, so after the ChatGPT answer I started labeling out a numeric workflow of files as brick walls start to be hit. Today there are floating token lengths and all sorts of new ways to handle things beyond JWT's. Why does Redis say they are unsafe today?

It only took a moment to get to the Google CLI and Cloud Client Libraries, which was already in scope, but it's nice to see how their teams document everything around Federated interaction, CORS and such proxy obfuscation with containers today. I'm not getting paid to figure this out. It's purely for fun. Right? Right.

### Types of accounts to authorize the gcloud CLI

To grant authorization to the gcloud CLI to access Google Cloud, we use either a user account or a service account.

A user account is a Google Cloud account that allows end users to authenticate to your application. It is easy to interactively employ the gcloud CLI using a user account. User Account is recommended if using the gcloud CLI from the command line or writing scripts with the gcloud CLI for use on a single machine.

A service account is a Google Cloud account associated with your Google Cloud project and not a specific user. You can use the built-in service account available when using Cloud Functions, App Engine, Compute Engine, or Google Kubernetes Engine. A service account is recommended to run gcloud CLI scripts on multiple machines. This also requires longer term maintenance with incurred costs worth planning policy around.

The Service Account is recommended if installing and setting up the gcloud CLI as part of a machine deployment process in production, or for use on Compute Engine virtual machine instances where all users have access to root.

So as we may build out a minikube version of a CRM for local machine use off the grid, we have to also instill more policy that dictates how context is spread across the network. Let's talk about offline mode if we meet face to face.

For instance, if all functionality (we wont say resources and service requests) happens on a local machine (a docker container or in a pod using something analogous to k8s and k9s to monitor) we can separate what poking outside the "local host" looks like. 

This creates ramifications way deeper than any of the hello worlds out there I have recently ran upon in preliminary investigations. Why? Because they teach best practices and thinking outside this box & requires a lot more planning than most are capable of handling (or willing to shell money out) for a simple download request. Just click and be done with it. Well, how about uninterrupted webhooks?

Remember most development practices are geared around automated deployments into production environments that have lightning fast network connectivity to 0.0.0.0. Anyway, this application is for those in a concrete bunker, in that basement, with the TPS reports- and no wifi or cellular availability; Oh, let that sink in a moment.

### Someone doing this must have Credentials

So first things first, is the configuration file on a local dev machine? With Google it can be discovered. These need to be set up to pass through the initial steps in order to receive data from a Google endpoint. 

If you cannot use user credentials for local development, you can use a service account key. According to Google documentation, service account keys create unnecessary risk and should be avoided whenever possible. 

This is one means to [Provide credentials for Application Default Credentials (ADC)](https://cloud.google.com/docs/authentication/provide-credentials-adc). ADC is explained in more detail momentarily. The gcloud CLI install is needed to provide user credentials to ADC. See installs for more information.

### Cloud Client Libraries

Cloud Client Libraries are used to call the Google APIS, and to work with service metaphors in mind, rather than implementation details or service API concepts. The GitHub Repo page for each language lists the Cloud Platform services/APIs that are supported by that language's Cloud Client Library. For Python it is [here](https://github.com/googleapis/google-cloud-python)

To do a getting-started-python project that builds on kubernetes and on their machines in the cloud, go [here](https://github.com/GoogleCloudPlatform/getting-started-python). We are not going for resources running on instances in the cloud. We  wish to have a local machine without internet access that can handle most CRM tooling for a service industry company. 

It seems the world is all about keeping code off of local machines these days, especially in the world of SOC compliance and DevSecOps today. Maybe we want it to only execute on our machine. How about that offline mode? This is where a compliance lecture herds sheep.

The no code experimental Google APIs Explorer link is [here](https://developers.google.com/apis-explorer), and the link to the Sheets API is [here](https://developers.google.com/sheets/api/reference/rest)

and [the browser interface for API](https://developers.google.com/apis-explorer/#p/sheets/v4/) is using the APIs Explorer for the Google Sheets API.

#### ChatGPT start

Everything below addresses a ChatGPT approach- and it doesn't work! It is a good kickoff to get one's mind brought back up to speed without help from a human. I thought maybe I could try it out and see for myself just what state their learning model is at currently. 

Like most occasions, security through obscurity prevails inadvertently. When the herds are steered through the gates, we see nothing for our offline use case- including human call in support. Sale teams only can sell compute instances, and paid subscriptions to talk to SRE's won't get us there either. They are trained with the same mechanism. They just don't know how to do it, or are trained specifically not to spill beans. Documentation also fails to stay up to date by itself- that too is soon to change with AI I believe- as teams focus on outcomes with key results.

According to ChatGPT, to download a Google Sheets file from Google Drive using Python, we need to use the [google-auth](https://googleapis.dev/python/google-auth/latest/index.html) and the associated [user guide](https://googleapis.dev/python/google-auth/latest/user-guide.html) and google-api-python-client libraries, according to chatGPT. I'm also using a py311 conda environment, so there is that too.

Here's the chatGPT 5 step example of how we might do this:

1. First, install the google-auth and google-api-python-client libraries using pip:

```zsh
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

2. Next, create a new Python script and import the necessary libraries:

```py
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import googleapiclient.errors
```

#### Resources

[google.oauth2.credentials](https://google-auth.readthedocs.io/en/stable/reference/google.oauth2.credentials.html)

[googleapis.github.io](https://googleapis.github.io/google-api-python-client/docs/oauth.html)

3. Then, use the Credentials class to create a new credentials object. This object will allow you to authenticate with the Google Sheets API and access your Google Drive:

```py
# Replace the client_id and client_secret values with your own
creds = Credentials.from_client_secrets_file(
    'client_secret.json', ['https://www.googleapis.com/auth/spreadsheets.readonly']
)
```

#### How to get client_id and client_secret values for google sheets api:

The answer from chatGPT was not sufficient to enable programmatic access to Google Cloud resources, which needed access to the Sheets API. It might go deeper than just that and also require access to Drive API, but we shall see momentarily.

To use the Google Sheets API, we need to create a project in the Google Cloud Console and obtain a client ID and client secret. Here's how to do this (which also did not work from chatGPT):

- Go to the [Google Cloud Console](https://console.cloud.google.com/welcome?project=quickstart-1612637247094&pli=1) and sign in with a Google account.
- Click the "Create project" button to create a new project.
- Give the project a name and click "Create."
- Once the project has been created, click the "Enable APIs and Services" button.  
  * There is no "enable" just API's and Services.  Then click + enable APIs and services. It takes us to the API services page that we can look up the Sheets API with.
- In the search box, type "Sheets API" and click on the "Google Sheets API" result.
- Click the "Enable" button to enable the Google Sheets API for the project.
- Next, click the "Create credentials" button on top right -not on left pane- and select "OAuth client ID" as the type of credentials.

This did not work per instructions. See [02-gcp-new-project.md](./00-9-step-process.md) for details.

- Choose "Other" as the application type and give the client a name.
- Click the "Create" button to create the client ID and secret.
The client ID and secret will be displayed on the next page. Make sure to save these values, as we will need them to authenticate with the Google Sheets API.


4. Next, build a new service object using the build function from the googleapiclient.discovery module. This service object will allow us to access the Google Sheets API:

```py
service = build('sheets', 'v4', credentials=creds)
```

Now, we can use the service object to download the Google Sheets file. To do this, we'll need to know the file ID of the Google Sheets file that you want to download. You can find the file ID by looking at the URL of the file in your Google Drive. The file ID is the long string of characters between /d/ and /edit in the URL. (This is a valid answer so far)

Once you have the file ID, you can use the service.spreadsheets().get() method to download the file:

```py
# Replace the file_id value with the actual file ID of the Google Sheets file
file_id = 'YOUR_FILE_ID'

try:
    # Call the Sheets API to download the file
    sheet = service.spreadsheets().get(spreadsheetId=file_id).execute()

    # Print the file data
    print(sheet)

except HttpError as error:
    print(f'An error occurred: {error}')
    sheet = None
```

This will not download the Google Sheets file and print the file data to the console. It generates an 

AttributeError: type object 'Credentials' has no attribute 'from_client_secrets_file'. Thus the need for being able to dissect dense documentation begins. On to the next numerically indexed .md file please;)