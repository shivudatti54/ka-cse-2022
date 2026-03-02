# Electronic Mail (Email) - Summary

## Key Definitions and Concepts

- **Email (Electronic Mail):** A method of exchanging digital messages between users over a network using standardized protocols.
- **MUA (Mail User Agent):** Client application used to compose, send, and read emails (e.g., Outlook, Gmail).
- **MTA (Mail Transfer Agent):** Server software that routes and transfers emails between servers using SMTP.
- **MDA (Mail Delivery Agent):** Component that delivers incoming emails to recipient's mailbox on the server.
- **MRA (Mail Retrieval Agent):** Intermediary that retrieves emails from server to client using POP3/IMAP.
- **MIME (Multipurpose Internet Mail Extensions):** Standard that extends email to support non-text content like images, audio, and attachments.

## Important Formulas and Protocols

| Protocol | Port | Purpose           | Key Feature                 |
| -------- | ---- | ----------------- | --------------------------- |
| SMTP     | 25   | Sending emails    | Server-to-server transfer   |
| POP3     | 110  | Retrieving emails | Downloads and deletes       |
| IMAP     | 143  | Managing emails   | Synchronizes across devices |

## Key Points

- Email operates as a store-and-forward distributed system using client-server architecture.
- SMTP is the standard protocol for sending and forwarding emails between mail servers.
- POP3 is simple but deletes messages from server after download (single-device use).
- IMAP allows management of emails on the server, ideal for multi-device synchronization.
- Email addresses follow format: username@domainname, where domain maps to DNS MX records.
- RFC 822 defines basic email format; MIME extends it for multimedia content.
- SMTP communication uses text-based commands (HELO, MAIL FROM, RCPT TO, DATA, QUIT).
- Email header contains metadata: From, To, Subject, Date, Message-ID, MIME-Version.

## Common Mistakes to Avoid

- Confusing SMTP with POP3/IMAP - SMTP sends, POP3/IMAP retrieve
- Assuming POP3 keeps emails on server - it typically deletes after download
- Forgetting that email addresses are case-insensitive but domain names matter
- Overlooking that MIME encoding is necessary for binary attachments

## Revision Tips

1. Practice tracing the complete email flow from sender to recipient, identifying each component and protocol involved.
2. Memorize the SMTP command sequence: HELO → MAIL FROM → RCPT TO → DATA → QUIT.
3. Remember the port numbers: SMTP=25, POP3=110, IMAP=143 (secure versions add 1 to last digit).
4. Use comparison tables to differentiate POP3 vs IMAP characteristics for quick recall during exams.
5. Review sample email headers to identify different fields and understand their purposes.
