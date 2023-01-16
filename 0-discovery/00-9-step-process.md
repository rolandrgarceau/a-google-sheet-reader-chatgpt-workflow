### [Workspaces API authentiication and authorization](https://developers.google.com/workspace/guides/auth-overview)

To actually download a file programatically and not simply be browsing to see my reasoning behind authentication refreshers with Google Services, read on.

1. Configure your Google Cloud project and app.

There exists `authorization scopes`. Docs state at above link there are 3 ways in accessing credentials to authenticate your app with:

- API key, 
- end user credential, or 
- service account credential. an API key

Docs doe not discuss the service account impersonation with a limited time token, but I believe it should exist and is safer than long lived service account credentials.

2. Authenticate your app for access

- Registered access credentials are evaluated
- Authenticating as an end user might have a sign in prompt

3. Request resources using relevant scopes of access previously registered.

4. Ask for user consent if authenticating as an end user- OAuth consent screen will ask if we want the app to have access to requested data.

5. Send approved request for resources:

When user consents to the scopes of access, our app bundles the credentials and the user-approved scopes of access into a request to the Google authorization server to obtain an access token.

6. Google returns an access token in which the access token contains a list of granted scopes of access. If the returned list of scopes is more limited than the requested scopes of access, our app disables any features limited by the token.

That sounds as if we need to program our functionality to the token itself. More work needs to be done here.

7. Access requested resources: Our app uses the access token from Google to invoke the relevant APIs and access the resources.

8. Get a refresh token (optional). Find out how to set a TTL- it said a few hours to a few minutes somewhere.

9. Request more resources: If additional access is needed, our app asks the user to grant new scopes of access, resulting in a new request to get an access token (steps 3–6). 

Still sounds too smart for my thought process. Why would my app have to qualify this? Think about asking a user to grant new scopes. Where does this come from? Which client are we referring to? A Google Client or one of our actual customers trying to access something off of Workspaces? 

If an app is not asking for enough permissions from the get go, eventually the request will be denied. If there needs to be more permissions granted, then an app does not figure that out, a developer creates code to request a different scope. 

It may be in the form of an if, elif, with sequentially more needed permissions asking for a release of a new, more encompassing token. When the documentation starts of confusing, the snowball will roll downhill, guaranteed. Not to say this is on purpose, but not everyone needs to be able to enforce authorization workflows.

### Refresh on terms is not necessarily Workspaces terms

Google is not AWS and there may be ambiguity here.

- Principal: Can be a user or an app acting on behalf of a user.

- Authentication: ensures the principal is who they say they are. For Workspaces we have two tpyes:

- User authentication: is signing into the app.

Typically this id done with username and password to verify their identity to the app. It may be incorporated into an actual [Google Signin](https://developers.google.com/identity/gsi/web).

- App Authentication: is the actual application authenticating diretly to service with Google- on behalf of the user running the app. There are usually pre-created credentials in app code. 

Documentation here is not thorough, as we know there may be a .json credential file on a local machine housing this information for the application itself. However, we may be also bundling in this notion of a  user running the app, and their credentials into one or more calls (handshakes, requests, whatever is in the workflow)