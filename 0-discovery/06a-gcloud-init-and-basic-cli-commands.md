### [gcloud init](https://cloud.google.com/sdk/gcloud/reference/init)

The first initial setup of the cli uses default configuration for just one project setup. Run again we can choose via cli the project that is created within workspaces, or we can use the cli in the future to make new projects.

General first time running `gcloud init`:

```zsh
# options:
# --skip diagnostics
# --no-browser, deprecated are these 2: --console-only, --no-launch-browser

# reinitializing an existing configuration will remove all its existing properties!
gcloud init # there is also gcloud alpha init and beta 
```

We may be headless and now wish to use a browser, or run diagnostics. This will handle the default, single account set up. 

```zsh
# The gcloud auth login command authorizes access by using workload identity federation, which provides access to external workloads, or by using a service account key. This exposes potential security vulnerabilities.
gcloud auth login
```

We may want multiple accounts to work with.

```zsh
# To switch between configurations use `activate` (like conda envs).
gcloud config configurations activate my-config 
```

Run `gcloud help config` for more information.

#### [gcloud topic configurations](https://cloud.google.com/sdk/gcloud/reference/topic/configurations)

The link here will help navigate between projects. Things like structured logs (show_structured_logs) and project (by id) can be viewed here with the `gcloud topic configurations` command. 

We modify with `gcloud config set` and `gcloud config unset` commands. We can see auth information like `access_token_file` or `disable_credentials` needed behind a proxy that adds authentication to requests. More on this when kubernetes/docker gets involved. There is the `impersonate_service_account`, but company policy may be enforceable here, so beware.

### [Region and Zones](https://cloud.google.com/compute/docs/regions-zones)

selecting region and zone:

us-east1-b is south carolina and offers E2, N2, N2D, T2D, N1, M1, C2, A2.

us-east1-c is also south carolina ands offers C2D. us-east1-d is exactly the same as us-east1-c. us-east4-a offers all the above plus M2.

Output of the init suggests to go to [docs](https://cloud.google.com/compute/docs/gcloud-compute) and choose to set the --region and --zone manually. 

It also says that the gcloud init can do this the next time it is run but we have to enable the Compute Engine API for the project [here](https://console.developers.google.com/apis).

### [gcloud topic configurations](https://cloud.google.com/sdk/gcloud/reference/topic/configurations) 

- Separate configuration for each project
- Use different user and service accounts

#### named configurations

Name it for configuring separate usages for gcloud. There is a builtin configuration named NONE that has no properties set.

Configuration data is typically stored in $HOME/.config/gcloud, however watch out for the .boto file if you also develop with AWS. There might need to be policy defined as to procedures to have this on developer workstations that are ran with thin clients or otherwise.

Property information stored in named configurations are readable by all gcloud commands and may be modified by gcloud config set and gcloud config unset. Override this location by setting the environment variable CLOUDSDK_CONFIG, and is particularly useful if $HOME points to a read only filesystem or running commands inside docker.

```zsh
#  create new empty config named my-config
gcloud config configurations create my-config

# figure out what path the active current config is using
gcloud info --format="get(config.paths.active_config_path)"
# >>> ~/.config/gcloud/configurations/config_default

# see active config
gcloud config list

# current available accounts
gcloud auth list

# usage statistics reporting for a better google experience
gcloud config set disable_usage_reporting false # this will make it send to google

# allow you to to list, activate, describe, and delete configurations that may or may not be active.
gcloud config configurations 

```

#### Run the gcloud CLI as a Docker image

Eventually we will probably have to go [here](https://cloud.google.com/sdk/docs/downloads-docker) when the time comes.

#### Manage gcloud CLI

gcloud components for apt-get and yum installations are different here. Use those for management instead.

After installing the gcloud CLI, you can use commands in the gcloud components command group to manage your installation. This includes viewing installed components, adding and removing components, and upgrading to a new version or downgrading to a specific version of the gcloud CLI.

#### console output on a `gcloud init`

[https://cloud.google.com/storage/docs/gsutil/commands/config]

