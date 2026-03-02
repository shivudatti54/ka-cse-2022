# Content Security Policy (CSP) for XSS Mitigation

## 1. Introduction to Content Security Policy (CSP)

**Content Security Policy (CSP)** is a powerful security mechanism implemented via an HTTP response header. It acts as a **whitelist** directive, instructing the browser which sources of content (scripts, styles, images, etc.) are legitimate and allowed to be loaded or executed. Its primary purpose is to mitigate a wide range of content injection attacks, most notably **Cross-Site Scripting (XSS)**.

Traditional XSS defenses, like output encoding, rely on correctly sanitizing every piece of data. CSP takes a different, more robust approach: even if an attacker successfully injects a malicious script, the browser will not execute it unless its source violates the defined policy. This shifts the security model from "allow all except what's bad" to a stricter "deny all except what's explicitly good."

## 2. How CSP Works to Prevent XSS

CSP works by defining a policy via the `Content-Security-Policy` HTTP header. The browser receives this policy along with the HTML document. As it parses the page, it checks every resource it's about to load or every script it's about to execute against this policy. If a resource violates the policy, the browser simply blocks it.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           Web Server                                    │
│                                                                         │
│  HTTP/1.1 200 OK                                                       │
│  Content-Type: text/html                                                │
│  Content-Security-Policy: script-src 'self' https://trusted.cdn.com     │
│                                                                         │
│  <html>                                                                 │
│    <body>                                                               │
│      <script src="https://trusted.cdn.com/valid.js"></script> ✅       │
│      <script>alert('Hello World');</script> ❌ (Blocked: inline)       │
│      <script src="http://evil.com/malicious.js"></script> ❌ (Blocked)  │
│    </body>                                                               │
│  </html>                                                                 │
└─────────────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                           User's Browser                                 │
│                                                                         │
│  1. Receives HTML and CSP header.                                        │
│  2. Parses policy: "Only allow scripts from our own origin and           │
│     https://trusted.cdn.com".                                            │
│  3. Loads valid.js from trusted.cdn.com (Allowed).                       │
│  4. Blocks execution of inline <script> tag.                            │
│  5. Blocks loading of malicious.js from evil.com.                        │
│                                                                         │
│  Result: Page renders safely, XSS payloads are neutralized.             │
└─────────────────────────────────────────────────────────────────────────┘
```

## 3. Key CSP Directives for XSS Mitigation

A CSP policy is composed of multiple directives that control different resource types. For XSS, the most critical directive is `script-src`.

| Directive | Purpose | Example Values |
| :--- | :--- | :--- |
| **`default-src`** | Fallback for most other directives. A good starting point. | `'self'`, `'none'` |
| **`script-src`** | **Crucial for XSS.** Controls which scripts can be executed. | `'self'`, `'unsafe-inline'`, `'nonce-<value>'` |
| `style-src` | Controls sources for stylesheets. | `'self'`, `'unsafe-inline'` |
| `img-src` | Controls sources for images. | `'self'`, `data:` |
| `connect-src` | Controls which URLs can be loaded via scripts (e.g., fetch, XHR). | `'self'`, `https://api.example.com` |
| `form-action` | Restricts which URLs can be used as form `action` attributes. | `'self'` |
| `base-uri` | Restricts the URLs that can be used in a `<base>` element. | `'self'` |
| `frame-ancestors` | Specifies which parents can embed the page (replaces X-Frame-Options). | `'none'` |

### Special Keyword Sources

| Keyword | Meaning |
| :--- | :--- |
| `'none'` | Denies loading any resources for the directive. |
| `'self'` | Allows resources from the same origin (same scheme, host, and port). |
| `'unsafe-inline'` | Allows inline JavaScript/CSS (e.g., `<script>`, `onclick`). **Weakens CSP.** |
| `'unsafe-eval'`| Allows `eval()`, `setTimeout(string)`, etc. **Weakens CSP.** |
| `'strict-dynamic'`| Allows scripts trusted by a already-trusted script (e.g., dynamically loaded). |

## 4. Implementing a Strong CSP: The Journey from 'unsafe-inline' to Nonces

A weak CSP is often worse than none, as it provides a false sense of security. The goal is to move away from allowing `'unsafe-inline'`.

### Phase 1: Report-Only Mode
Always start with `Content-Security-Policy-Report-Only`. This header tells the browser to report policy violations without actually blocking them. This is essential for testing your policy on a live site without breaking functionality.
```
Content-Security-Policy-Report-Only: default-src 'self'; script-src 'self'; report-uri /csp-violation-report-endpoint
```

### Phase 2: Eliminating 'unsafe-inline'
The biggest challenge is dealing with inline scripts. Instead of using `'unsafe-inline'`, use one of these two secure methods:

**1. Using Nonces (Number Used Once)**
A nonce is a random, base64-encoded string generated for each request. The server includes it in the CSP header and in the `nonce` attribute of any inline script tag. The browser will only execute the script if the nonces match.

*   **Server generates header:**
    `Content-Security-Policy: script-src 'nonce-r4nd0mV4lu3'`
*   **Server generates HTML:**
    `<script nonce="r4nd0mV4lu3">console.log("This inline script is allowed");</script>`

An attacker cannot guess the nonce for the next request, making their injected script tag useless.

**2. Using Hashes**
You can specify a hash of the allowed inline script in your policy. The browser will compute the hash of any inline script and only execute it if it matches one in the policy.

*   **Calculate hash:** The SHA256 hash of `console.log("This inline script is allowed");` is `sha256-5LiybI8a...=` (shortened for example).
*   **Server generates header:**
    `Content-Security-Policy: script-src 'sha256-5LiybI8a...='`

This is useful for allowing specific, static inline scripts but becomes cumbersome if scripts change frequently.

### Phase 3: Deploying Enforcement Policy
Once you have addressed all violations found in report-only mode, switch to the enforcing header `Content-Security-Policy`.
```
Content-Security-Policy: default-src 'self'; script-src 'self' https://trusted.cdn.com 'nonce-r4nd0mV4lu3'; img-src 'self' data:; report-uri /csp-violation-report-endpoint
```

## 5. Monitoring and Reporting

The `report-uri` (or newer `report-to`) directive is vital. It tells the browser to POST a JSON report to a specified URL whenever a policy violation is blocked. This allows you to:
*   **Discover bugs** in your CSP implementation during the `Report-Only` phase.
*   **Detect active attacks** in the enforcement phase, as violations could indicate someone trying to probe your site.

## 6. Example CSP Policies

**Strict Policy (Ideal):**
```
Content-Security-Policy:
  default-src 'none';
  script-src 'self' 'nonce-r4nd0mV4lu3';
  style-src 'self';
  img-src 'self';
  connect-src 'self';
  base-uri 'self';
  form-action 'self';
  report-uri /csp-reports;
```
*Denies everything by default. Only allows scripts from self (with a nonce for specific inline code), styles from self, images from self, and API connections to self.*

**Common Policy with trusted CDN:**
```
Content-Security-Policy:
  default-src 'self';
  script-src 'self' https://ajax.googleapis.com;
  style-src 'self' https://fonts.googleapis.com;
  font-src 'self' https://fonts.gstatic.com;
  img-src 'self' data:;
  report-uri /csp-reports;
```
*Allows resources from self and specific trusted CDNs. Allows data URLs for images (e.g., inline SVGs).*

## 7. Limitations and Considerations

*   **Complexity:** Implementing a strong CSP requires effort and can break existing functionality.
*   **Third-party code:** Integrating with external widgets, analytics, or ads can be challenging and may require loosening the policy.
*   **Not a silver bullet:** CSP is highly effective against XSS but does not replace the need for proper output encoding and input validation. It is a **defense-in-depth** control.

## Exam Tips

1.  **CSP is a whitelist mechanism.** Remember it defines what is *allowed*, not what is *blocked*.
2.  **The main header is `Content-Security-Policy`.** `Content-Security-Policy-Report-Only` is used for testing.
3.  **`script-src` is the most important directive for preventing XSS.** Focus on its values: `'self'`, `'unsafe-inline'` (avoid), `'nonce-<value>'`, `'sha256-...'`.
4.  **Using `'unsafe-inline'` significantly weakens CSP against XSS.** The goal is to replace it with nonces or hashes.
5.  **A nonce is a server-generated random value** that must match between the header and the script tag's attribute to allow execution.
6.  **CSP is a defense-in-depth technique.** It should be used **in addition to**, not instead of, proper output encoding.