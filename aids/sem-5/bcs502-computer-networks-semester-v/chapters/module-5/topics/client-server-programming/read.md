# Client-Server and HTTP/WWW

## Introduction

The client-server model is a fundamental concept in computer networks, where a client requests services or resources from a server. In this topic, we will explore the client-server model, HTTP (Hypertext Transfer Protocol), and the World Wide Web (WWW).

## Client-Server Model

The client-server model is a distributed application structure that separates the presentation layer (client) from the data storage and processing layer (server). The client requests services or resources from the server, and the server responds with the requested information.

### Characteristics of Client-Server Model

- **Separation of Concerns**: The client and server have different responsibilities, making it easier to maintain and update the system.
- **Scalability**: The client-server model allows for easy scalability, as new clients can be added without affecting the server.
- **Flexibility**: The client-server model supports multiple clients and servers, making it a flexible architecture.

### Types of Client-Server Models

- **One-Tier Architecture**: The client and server are on the same machine.
- **Two-Tier Architecture**: The client and server are on different machines, but the client communicates directly with the server.
- **Three-Tier Architecture**: The client communicates with an application server, which then communicates with a database server.

## HTTP (Hypertext Transfer Protocol)

HTTP is a request-response protocol used for transferring data over the internet. It is a stateless protocol, meaning that each request is independent of the previous one.

### HTTP Request Methods

- **GET**: Retrieves data from the server.
- **POST**: Sends data to the server to create a new resource.
- **PUT**: Updates an existing resource on the server.
- **DELETE**: Deletes a resource from the server.

### HTTP Response Status Codes

- **1xx**: Informational responses
- **2xx**: Successful responses
- **3xx**: Redirection responses
- **4xx**: Client error responses
- **5xx**: Server error responses

## World Wide Web (WWW)

The World Wide Web is a system of interlinked hypertext documents that can be accessed via the internet. The web is built on top of HTTP and uses web browsers to display web pages.

### Web Browsers

- **Google Chrome**: A popular web browser developed by Google.
- **Mozilla Firefox**: A free and open-source web browser developed by Mozilla.
- **Microsoft Edge**: A web browser developed by Microsoft.

### Web Servers

- **Apache HTTP Server**: A popular open-source web server developed by the Apache Software Foundation.
- **Nginx**: A free and open-source web server developed by Igor Sysoev.
- **IIS (Internet Information Services)**: A web server developed by Microsoft.

## Example Use Case

A user wants to access a website using a web browser. The user types the URL of the website in the address bar, and the browser sends an HTTP GET request to the web server. The web server responds with the requested web page, which is then displayed in the browser.

```
+---------------+
|  Web Browser  |
+---------------+
         |
         |  HTTP GET Request
         |
         v
+---------------+
|  Web Server   |
+---------------+
         |
         |  HTTP Response
         |
         v
+---------------+
|  Web Browser  |
+---------------+
         |
         |  Displays Web Page
         |
         v
```

## Comparison of Client-Server Models

|                       | One-Tier Architecture | Two-Tier Architecture | Three-Tier Architecture |
| --------------------- | --------------------- | --------------------- | ----------------------- |
| **Client and Server** | Same machine          | Different machines    | Different machines      |
| **Scalability**       | Limited               | Easy                  | Easy                    |
| **Flexibility**       | Limited               | Good                  | Excellent               |
| **Security**          | Limited               | Good                  | Excellent               |

## Exam Tips

- Understand the client-server model and its characteristics.
- Know the different types of client-server models.
- Understand HTTP and its request methods.
- Know the different HTTP response status codes.
- Understand the World Wide Web and its components.
- Be able to compare different client-server models.
