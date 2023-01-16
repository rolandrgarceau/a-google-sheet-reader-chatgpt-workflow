### Installs

Which one do we do first? Well we need a CLI for Google. Maybe it will work for Workspaces too.

Don't jump the gun until we know what installs what today. Phone a friend. Call 844-613-7589 and only use it for business use. Personal use is not here. Tech support will kick you out. Upgrade account will get us to sales, and Nelson might tell you we sell servers in the cloud, and good luck at your offline mode development. 

developers.google.com website tab for community developers group might be a resource to tap when the time is right. 

### [Cloud SDK](https://cloud.google.com/sdk)

### [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)

google-cloud-sdk is what the CLI page is talking about.

The google install includes the gcloud, gsutil and bq command-line tools.  For a list of gcloud CLI features go [here](https://cloud.google.com/sdk#all-features).


```zsh
brew install --cask google-cloud-sdk
```

The brew install output says to add this to zsh config:

for zsh users:
    source "/usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/path.zsh.inc"

brew's website says:

source "$(brew --prefix)/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/path.zsh.inc"
    
Follow brew install [here](https://jansutris10.medium.com/install-google-cloud-sdk-using-homebrew-on-mac-2952c9c7b5a1)

the medium site adds completion to the config:

source "$(brew --prefix)/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/completion.zsh.inc"

however Source [/usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/completion.zsh.inc] in your profile to enable shell command completion for gcloud came from shell output in case the --prefix isn't right on your machine.

After brew install:

```zsh
# check it:
gcloud version
# Authenticate Google Cloud Developer account
gcloud auth login
```

This launches the browser to select the account to login with. Afterwords, success redirects [here](https://cloud.google.com/sdk/auth_success), with a few tutorials we could start with. Make your applications and services available to your users with Cloud DNS isone that may become useful sooner than later.

#### gcloud CLI [guide](https://cloud.google.com/sdk/gcloud)
#### [Accessing services with the CLI](https://cloud.google.com/sdk/cloudplatform)

The command authorizing the SDK tools to access Google Cloud Platform using your user account credentials and setting up the default SDK configuration:

```
gcloud init
```

But mine looked like it already had picked up my account info. See the 06a-gcloud-init.md for more info on the gcp settings.

### [Python Cloud Client Libraries](https://cloud.google.com/python/docs/reference)

We are getting closer.