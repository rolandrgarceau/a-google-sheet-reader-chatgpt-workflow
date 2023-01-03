### Why Identity Federation?

With identity federation, you can use Identity and Access Management (IAM) to grant external identities IAM roles, including the ability to impersonate service accounts.

### Service account impersonation

The token exchange flow returns a federated access token. You can use this token to impersonate a service account and obtain a short-lived OAuth 2.0 access token. The short-lived access token lets you call any Google Cloud APIs that the service account has access to.

### [Custom IAM roles](https://cloud.google.com/iam/docs/understanding-custom-roles)

### [Workload identity federation](https://cloud.google.com/iam/docs/workload-identity-federation) using Federated tokens

Federation lets your workloads access resources directly, using a short-lived access token, and eliminates the maintenance and security burden associated with service account keys.

We can use identity federation with Amazon Web Services (AWS), or with any identity provider that supports OpenID Connect (OIDC), such as Microsoft Azure, or SAML 2.0.

Okta is coming. I love the password-less future. 

AWS has mappings for ARNs.



