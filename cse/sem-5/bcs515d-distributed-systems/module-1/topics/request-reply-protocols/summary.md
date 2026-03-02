# Request-Reply Protocols - Summary

## Key Definitions and Concepts

- **Request-Reply Pattern:** A communication paradigm where a client sends a request message to a server and receives a corresponding reply message containing the results or acknowledgment
- **Synchronous Request-Reply:** Client blocks and waits for the server's response before continuing execution
- **Asynchronous Request-Reply:** Client continues processing after sending request; response is handled via callbacks or futures
- **RPC (Remote Procedure Call):** A protocol that enables a program to execute a procedure on a remote computer as if it were a local call
- **Idempotent Operations:** Operations that produce the same result regardless of how many times they are executed, crucial for handling duplicate requests

## Important Formulas and Concepts

- **Message Structure:** Request = Operation Type + Request ID + Parameters + Addressing; Reply = Status Code + Correlation ID + Response Data
- **Timeout Calculation:** timeout = estimated_round_trip_time × safety_factor (typically 2-3×)
- **Retry Strategy:** Exponential backoff with jitter prevents thundering herd problem

## Key Points

1. Request-reply is the simplest client-server communication pattern, forming the basis for HTTP, database queries, and RPC

2. Synchronous mode is simpler but may waste client resources waiting; asynchronous improves throughput but adds complexity

3. Lost requests are handled through timeouts and retries; lost replies may cause duplicate processing

4. Idempotent operations allow safe retries without side effects; non-idempotent operations require duplicate detection

5. RPC abstracts network communication to make remote calls appear like local function calls

6. HTTP is the most widespread request-reply protocol, used for web services and REST APIs

7. Connection management significantly impacts performance; persistent connections reduce overhead

8. Status codes in replies indicate success or failure types (2xx success, 4xx client error, 5xx server error)

## Common Mistakes to Avoid

- Confusing synchronous with connection-oriented protocols; they are different concepts
- Forgetting that retries can cause duplicate processing if operations are not idempotent
- Not handling network failures properly; always implement appropriate timeout and retry logic
- Assuming all request-reply protocols guarantee delivery; some may lose messages

## Revision Tips

1. Draw the request-reply flow diagram repeatedly until you can reproduce it from memory

2. Practice tracing through example scenarios: successful request, lost request, lost reply, server crash

3. Compare HTTP, RPC, and message queue implementations to understand different approaches

4. Review common HTTP status codes and their meanings for practical understanding

5. Remember that request-reply is a pattern, not a specific protocol; it can be implemented in many ways
