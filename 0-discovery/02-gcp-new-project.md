### [Login](https://console.cloud.google.com/apis/dashboard?project=xenon-height-372215)

This was the next logical step attempting to follow chatGPT response- get into GCP (workspaces?) and figure out how to Allow access to Google Sheets API. One option occurred to me was how to just snag a file off drive. That's still on the chopping block, but first let's explore Sheets. 

In reality we should probably following a how to guide for google-auth or the google-api-python-client. That comes momentarily after this Enable Sheets API console is revisited after a year or so. 

### New Project

Creating a new project has tags that get renamed. I named it google-sheets-downloader and after inspection in the left pane after all was said and done the credentials that were generated was under a name like web app 1 or something. This only took about 30 minutes while in a parking lot waiting for my son to get out of a basketball game, so it wasn't a total waste of time.

In order to get to the new projects I searched for new project in search bar and it returned nothing, but then there was a dropdown for it. Way to go with confusing file and paths for recreation Google! This is where most should skip to the hello world version and check out 04_g_auth_test.md. KISS me...

We need to enable the API, but there is no "enable" per instructions, just API's and Services in left pane. Click that then click + enable APIs and services on top. It takes us to the API services page that we can look up the Sheets API in the search bar. Click it and then at top there is a create credentials option.
 
### Creating OAuth Credentials

#### Credential type

Which API are you using?

select Google Sheets API in dropdown menu.

Use the radial button select user data.

Clicking next sends us to OAuth Consent Screen, which popped up a couple different ways.

I skipped all the uri and only selected web app. then clicked create and it gave me a client id. Congradulations yet again google for confusing the hell out of developers!

Then download secret in json format. Checking the Credentials tab to see what existed had the Client ID for Web application with the name Web client 1 that had the matching client ID above and secret downloaded, so I wonder what it was that I wen through? Oh well, yet another security through obscurity?

#### NOTE: Left pane select OAuth Consent Screen looks close, but no cigar

The following did not follow instructions. The left pane now offers OAuth consent screen. It will allow a user type for internal or external. I selected internal, and on left pane selected OAuth Consent Screen. More info [here](https://support.google.com/cloud/answer/10311615#user-type). The create button here will prompt app registration for internal users only. When we go to production using external there will need to be changes made here to access Sheets.

This is where we can view the App Information:

The name of the app asking for consent. 

User support email:

For users to contact you with questions about their consent

App logo: did not try to use one.

There is an App Domain. With an App Homepage, privacy policy link, and terms of service, including developer contact information. The Consent screen does not look like we are down the right path.

#### Conclusion 

I've omitted the actual project information as I was attempting to use the graphical interface. The client secret also is not checked into version control, or the steps to invalidate authentication in this manner.

This was a rabbit hole. The app name and tag information did not match on the main project page of information from what I was creating through all these menus, and was very confusing. I'd say stick to CLI and follow the parameters/arguments for building this out for an automated deployment.

