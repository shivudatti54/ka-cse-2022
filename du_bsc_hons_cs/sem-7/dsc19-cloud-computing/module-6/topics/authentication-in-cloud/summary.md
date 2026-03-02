# Authentication in Cloud Computing - Summary

## Key Definitions and Concepts

- **Authentication:** The process of verifying the identity of a user, device, or system before granting access to cloud resources
- **Authorization:** The process of determining what actions an authenticated user can perform (complements authentication)
- **MFA (Multi-Factor Authentication):** Requires two or more verification factors for enhanced security
- **IAM (Identity and Access Management):** Policies and technologies managing user identities and access rights
- **SSO (Single Sign-On):** Authentication mechanism allowing access to multiple applications with one set of credentials
- **Federated Identity:** Trust relationship allowing cross-domain authentication
- **Zero Trust:** Security model requiring continuous verification for every access request

## Important Formulas and Protocols

- **OAuth 2.0:** Authorization framework for delegated API access
- **OpenID Connect:** Identity layer built on OAuth 2.0 for authentication
- **SAML:** XML-based standard for exchanging authentication/authorization data

## Authentication Factors
1. **Something You Know:** Passwords, PINs, security questions
2. **Something You Have:** Tokens, smart cards, mobile devices
3. **Something You Are:** Biometrics (fingerprint, facial recognition)

## Key Points

- Cloud authentication operates under the shared responsibility model - providers secure infrastructure, customers configure authentication
- MFA significantly reduces unauthorized access risk even if one factor is compromised
- Major cloud providers offer comprehensive IAM services with built-in MFA support
- OAuth 2.0 is for authorization (what you can do), OpenID Connect adds authentication (who you are)
- SAML remains prevalent in enterprise environments for SSO implementation
- Zero Trust assumes no implicit trust based on network location
- Federation enables cross-organization access without separate credentials

## Common Mistakes to Avoid

- Using single-factor authentication for privileged accounts
- Sharing credentials or using the same password across services
- Failing to enable MFA for administrative accounts
- Not rotating access keys and credentials regularly
- Granting excessive permissions instead of following least privilege

## Revision Tips

1. Practice drawing the authentication flow for OAuth 2.0 and SAML
2. Memorize the three authentication factors with concrete examples
3. Review cloud provider documentation for IAM configuration best practices
4. Understand the differences between OAuth, OIDC, and SAML use cases
5. Focus on why MFA is essential rather than just what MFA is