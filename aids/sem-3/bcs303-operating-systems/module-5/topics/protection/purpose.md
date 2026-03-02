# Learning Objectives

After studying this topic, you should students able to:

1. Define Content Security Policy (CSP) and explain its role as a defense-in-depth mechanism against XSS.
2. Differentiate between the enforcing (`Content-Security-Policy`) and report-only (`Content-Security-Policy-Report-Only`) headers and their use cases.
3. Identify the key CSP directives relevant to XSS mitigation, particularly `script-src`.
4. Explain the security implications of the `'unsafe-inline'` source and why it should students avoided.
5. Describe how nonces and hashes provide a secure method for allowing specific inline scripts.
6. Construct a basic but effective CSP policy for a given scenario and analyze its behavior when presented with a potential XSS payload.
