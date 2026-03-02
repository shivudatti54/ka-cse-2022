# ** Datagram Socket Client/Server Program**

## **Table of Contents**

1. [Introduction](#introduction)
2. [Datagram Socket](#datagram-socket)
3. [Client/Server Architecture](#client-server-architecture)
4. [Programming the Client/Server Program](#programming-the-client-server-program)
5. [Example Code](#example-code)

## **1. Introduction**

Datagram sockets are a type of socket that allows for the transmission of data between two devices without guarantee of delivery or order of delivery. They are useful for applications where data is sent in a best-effort manner, such as online gaming or video streaming.

## **2. Datagram Socket**

- Definition: A datagram socket is a type of socket that allows for the transmission of data between two devices without guarantee of delivery or order of delivery.
- Characteristics:
  - Connectionless: No connection is established between the sender and receiver before data is sent.
  - Best-effort delivery: The sender does not guarantee the delivery of data to the receiver.
  - No sequencing: The order of delivery is not guaranteed.

## **3. Client/Server Architecture**

- Definition: A client-server architecture is a type of architecture where one device (the server) provides a service to multiple devices (the clients).
- Components:
  - Server: The server is the device that provides the service.
  - Client: The client is the device that requests the service.
  - Datagram socket: The datagram socket is used for communication between the client and server.

## **4. Programming the Client/Server Program**

To program the client/server program, we will use the following steps:

- Create a server program that listens for incoming datagrams.
- Create a client program that sends datagrams to the server.
- Handle incoming datagrams on the server program.
- Send datagrams from the client program to the server.

## **5. Example Code**

### Server Program

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define PORT 8080
#define BUFFER_SIZE 256

int main() {
    int server_fd, client_fd;
    struct sockaddr_in address;
    int addrlen = sizeof(address);
    char buffer[BUFFER_SIZE] = {0};

    // Create socket
    if ((server_fd = socket(AF_INET, SOCK_DGRAM, 0)) == 0) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    // Bind socket to port
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    printf("Server listening on port %d...\n", PORT);

    while (1) {
        // Receive datagram
        if (recvfrom(server_fd, buffer, BUFFER_SIZE, 0, (struct sockaddr *)&address, &addrlen) < 0) {
            perror("recvfrom failed");
            exit(EXIT_FAILURE);
        }

        printf("Received message: %s\n", buffer);

        // Send response
        char* response = "Hello, client!";
        if (sendto(server_fd, response, strlen(response), 0, (struct sockaddr *)&address, sizeof(address)) < 0) {
            perror("sendto failed");
            exit(EXIT_FAILURE);
        }
    }

    return 0;
}
```

### Client Program

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define PORT 8080
#define BUFFER_SIZE 256

int main() {
    int client_fd;
    struct sockaddr_in address;
    int addrlen = sizeof(address);
    char buffer[BUFFER_SIZE] = {0};

    // Create socket
    if ((client_fd = socket(AF_INET, SOCK_DGRAM, 0)) == 0) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    address.sin_family = AF_INET;
    address.sin_port = htons(PORT);
    inet_pton(AF_INET, "127.0.0.1", &address.sin_addr);

    printf("Client connected to server...\n");

    while (1) {
        // Send datagram
        char* message = "Hello, server!";
        if (sendto(client_fd, message, strlen(message), 0, (struct sockaddr *)&address, sizeof(address)) < 0) {
            perror("sendto failed");
            exit(EXIT_FAILURE);
        }

        // Receive response
        if (recvfrom(client_fd, buffer, BUFFER_SIZE, 0, (struct sockaddr *)&address, &addrlen) < 0) {
            perror("recvfrom failed");
            exit(EXIT_FAILURE);
        }

        printf("Received response: %s\n", buffer);
    }

    return 0;
}
```

This code creates a server program that listens for incoming datagrams and sends a response to the client. The client program sends a message to the server and receives the response. The datagram socket is used for communication between the client and server.
