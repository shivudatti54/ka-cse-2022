# Content Security Policy (CSP) Implementation

## Introduction to Content Security Policy

Content Security Policy (CSP) is a crucial security header that provides an additional layer of protection against various web attacks, particularly Cross-Site Scripting (XSS) and data injection attacks. It operates on a whitelist principle, allowing developers to specify which domains are approved for loading resources like scripts, stylesheets, images, fonts, and more.

CSP works by instructing the browser to only execute or render resources from trusted sources. When a CSP is properly implemented, even if an attacker manages to inject malicious code into your website, the browser will refuse to execute it if it doesn't originate from an approved source.

## How CSP Works

CSP is implemented through an HTTP response header that the server sends to the browser. The browser then enforces the policy directives specified in the header.

```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Security-Policy: default-src 'self'; script-src 'self' https://trusted.cdn.com
```

The basic flow of CSP enforcement can be visualized as:

```
+----------------+     +----------------+     +-----------------+
|   Web Server   | --> | HTTP Response  | --> |    Browser      |
|   (Sends CSP   |     |  with CSP      |     |  (Enforces      |
|    Header)     |     |  Header)       |     |   Policy)       |
+----------------+     +----------------+     +-----------------+
         |                                              |
         |                                              v
         |                                    +-------------------+
         +----------------------------------> |  Resource Loading |
                                              |  (Allowed/Blocked)|
                                              +-------------------+
```

## CSP Directives and Syntax

### Core Directives

CSP uses various directives to control different types of resources:

- **default-src**: Serves as fallback for other resource types
- **script-src**: Controls JavaScript execution
- **style-src**: Controls CSS stylesheets
- **img-src**: Controls image loading
- **font-src**: Controls web font loading
- **connect-src**: Controls XMLHttpRequest, WebSocket, and EventSource connections
- **frame-src**: Controls iframe embedding
- **media-src**: Controls audio and video elements
- **object-src**: Controls plugins like Flash
- **form-action**: Controls form submission targets

### Source Values

Directives accept various source values:

- **'none'**: Blocks all resources of this type
- **'self'**: Allows resources from the same origin
- **'unsafe-inline'**: Allows inline scripts/styles (use cautiously)
- **'unsafe-eval'**: Allows eval() and similar functions (use cautiously)
- **https:** Allows resources from any HTTPS source
- **example.com**: Allows resources from specific domain
- **data:** Allows data: URIs

## Implementing CSP

### Basic Implementation Example

A simple CSP header might look like:

```http
Content-Security-Policy: default-src 'self'; script-src 'self' https://apis.google.com; style-src 'self' 'unsafe-inline'
```

This policy:
- Allows resources from the same origin by default
- Allows scripts only from same origin and Google APIs
- Allows styles from same origin and inline styles

### Reporting Violations

CSP can be configured to report policy violations:

```http
Content-Security-Policy: default-src 'self'; report-uri /csp-violation-report-endpoint
```

Alternatively, you can use report-only mode for testing:

```http
Content-Security-Policy-Report-Only: default-src 'self'; report-uri /csp-violation-report-endpoint
```

## CSP Levels and Browser Support

### CSP Levels Comparison

| CSP Level | Key Features | Browser Support |
|-----------|-------------|-----------------|
| **Level 1** | Basic directives, XSS protection | Widely supported |
| **Level 2** | Additional directives, base-uri, form-action | Modern browsers |
| **Level 3** | Strict-dynamic, worker-src, manifest-src | Latest browsers |

### Browser Compatibility Table

| Browser | CSP Support | Notes |
|---------|------------|-------|
| Chrome | Full support | Includes latest Level 3 features |
| Firefox | Full support | Good Level 2 and 3 support |
| Safari | Good support | Some Level 3 features may be limited |
| Edge | Full support | Based on Chromium |

## Deployment Strategies

### Phased Implementation Approach

1. **Report-Only Mode**: Start with Content-Security-Policy-Report-Only to monitor potential issues
2. **Gradual Restrictions**: Begin with loose policies and gradually tighten them
3. **Violation Analysis**: Use violation reports to identify necessary adjustments
4. **Full Enforcement**: Switch to full enforcement once confident

### Common Implementation Patterns

**Strict Policy:**
```http
Content-Security-Policy: default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self'; connect-src 'self'; font-src 'self'; frame-ancestors 'none'
```

**E-commerce Site Policy:**
```http
Content-Security-Policy: default-src 'self'; script-src 'self' https://payment.processor.com; style-src 'self' 'unsafe-inline'; img-src 'self' data: https://cdn.example.com; connect-src 'self' https://api.example.com
```

## CSP and Modern Web Development

### Nonce-based CSP for Modern Applications

Modern applications often use nonces (number used once) for inline scripts:

```http
Content-Security-Policy: script-src 'nonce-2726c7f26c89'; default-src 'self'
```

With corresponding HTML:
```html
<script nonce="2726c7f26c89">
  // This inline script will execute
</script>
```

### Hash-based CSP

Alternatively, you can use hashes of allowed scripts:

```http
Content-Security-Policy: script-src 'sha256-abc123...'
```

## Common Challenges and Solutions

### Dealing with Third-Party Content

| Challenge | Solution |
|-----------|----------|
| Third-party scripts | Whitelist specific domains |
| CDN resources | Use subresource integrity (SRI) |
| Analytics tools | Specific domain allowances |
| Social media widgets | Frame-src directives |

### Legacy Application Considerations

Older applications might require:

```http
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'
```

However, this should be temporary while refactoring to eliminate unsafe practices.

## Advanced CSP Techniques

### CSP with Web Workers

```http
Content-Security-Policy: default-src 'self'; worker-src 'self'
```

### CSP and Service Workers

```http
Content-Security-Policy: default-src 'self'; script-src 'self'; connect-src 'self'
```

### CSP with Strict-Dynamic

Level 3 CSP introduces 'strict-dynamic' for more flexible policies:

```http
Content-Security-Policy: script-src 'nonce-abc123' 'strict-dynamic'
```

## Testing and Validation

### CSP Testing Tools

- **Browser Developer Tools**: Check console for CSP violations
- **Online Validators**: Tools like CSP Evaluator
- **Automated Scanners**: Include CSP checks in security testing

### Common Testing Scenarios

1. Test all functionality with CSP enabled
2. Verify third-party integrations work correctly
3. Check that violation reports are being captured
4. Test in report-only mode before full enforcement

## Exam Tips

1. **Remember the syntax**: CSP directives use semicolons to separate policies
2. **Understand source values**: 'self', 'none', 'unsafe-inline', etc.
3. **Know the difference**: Between Content-Security-Policy and Content-Security-Policy-Report-Only headers
4. **Prioritize security**: Always start with restrictive policies and loosen only as needed
5. **Practice deployment**: Understand the phased approach from report-only to enforcement
6. **Recognize common pitfalls**: Inline scripts and eval() are common CSP blockers
7. **Know browser support**: Different CSP levels have varying browser compatibility