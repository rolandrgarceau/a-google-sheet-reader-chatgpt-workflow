### Why Identity Federation?

With identity federation, you can use Identity and Access Management (IAM) to grant external identities IAM roles, including the ability to impersonate service accounts.

### Service account impersonation

The token exchange flow returns a federated access token. You can use this token to impersonate a service account and obtain a short-lived OAuth 2.0 access token. The short-lived access token lets you call any Google Cloud APIs that the service account has access to.

### [Create short-lived credentials for service account](https://cloud.google.com/iam/docs/create-short-lived-credentials-direct)

Some system architectures are designed around privilege-bearing service accounts, which are designed to be used together. In this case, you might need to create your credentials for multiple service accounts.

These short-lived creds (few hours or less) authenticate calls to Google Cloud APIs, other Google APIs, and non-Google APIs for limited access to trusted service accounts, with less risk than long lived service account keys.

We can create the following types of short-lived credentials by impersonating a service account:

- [OAuth 2.0 access tokens](https://cloud.google.com/docs/authentication/token-types#access): these are the most common.
- [ID tokens](https://cloud.google.com/docs/authentication/token-types#id): ID tokens follow the OpenID Connect (OIDC) specification, and are supported by a limited number of services and applications.

- [Self-signed JSON Web Tokens (JWTs)](https://cloud.google.com/docs/authentication/token-types#self-signed)

You can use self-signed JWTs to authenticate to some Google APIs without getting an access token from the Authorization Server. APIs deployed with API Gateway require them.

Is Sheets API deployed with API Gateway?


### [Custom IAM roles](https://cloud.google.com/iam/docs/understanding-custom-roles)

### [Workload identity federation](https://cloud.google.com/iam/docs/workload-identity-federation) using Federated tokens

Federation lets your workloads access resources directly, using a short-lived access token, and eliminates the maintenance and security burden associated with service account keys.

We can use identity federation with Amazon Web Services (AWS), or with any identity provider that supports OpenID Connect (OIDC), such as Microsoft Azure, or SAML 2.0.

Okta is coming. I love the password-less future. 

AWS has mappings for ARNs.



