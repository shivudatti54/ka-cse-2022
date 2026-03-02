# **Client-Server Program for File Transfer**

## **Overview**

A client-server program is designed to facilitate the transfer of files between a client and a server. The client sends the file name to the server, and the server responds with the contents of the requested file if present.

## **Key Points**

- **Client-Server Model**: A client sends a request to a server, which processes the request and responds with the requested data.
- **Sockets**: Used for establishing a connection between the client and server.
- **TCP/IP**: Protocols used for reliable data transfer between the client and server.
- **File Transfer**: Client sends file name to server, server responds with file contents if present.

## **Server Program**

- **Server Code**:
  ```c
  #include <stdio.h>
  #include <stdlib.h>
  #include <string.h>
  ```

int main() {
int sock;
struct sockaddr_in server_addr, client_addr;
socklen_t client_len = sizeof(client_addr);
char buffer[1024], filename[100];

    // Create socket
    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        perror("socket creation failed");
        exit(1);
    }

    // Set server address
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(8080);
    server_addr.sin_addr.s_addr = INADDR_ANY;

    // Bind socket to address and port
    if (bind(sock, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("bind failed");
        exit(1);
    }

    // Listen for incoming connections
    if (listen(sock, 1) < 0) {
        perror("listen failed");
        exit(1);
    }

    printf("Server listening...\n");

    while (1) {
        // Accept incoming connection
        int new_sock = accept(sock, (struct sockaddr *)&client_addr, &client_len);
        if (new_sock < 0) {
            perror("accept failed");
            exit(1);
        }

        // Receive file name from client
        if (recv(new_sock, filename, 100, 0) < 0) {
            perror("recv failed");
            continue;
        }

        // Check if file exists on server
        FILE *file = fopen(filename, "r");
        if (file == NULL) {
            send(new_sock, "File not found", 100, 0);
            continue;
        }

        // Send file contents to client
        char buffer[1024];
        while (fgets(buffer, 1024, file) != NULL) {
            send(new_sock, buffer, strlen(buffer), 0);
        }

        // Close file and socket
        fclose(file);
        close(new_sock);
    }

    return 0;

}

````

**Client Program**
----------------

* **Client Code**:
  ```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>

int main() {
    int sock;
    struct sockaddr_in server_addr;
    char buffer[1024], filename[100];

    // Create socket
    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        perror("socket creation failed");
        exit(1);
    }

    // Set server address
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(8080);
    server_addr.sin_addr.s_addr = INADDR_ANY;

    // Connect to server
    if (connect(sock, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("connect failed");
        exit(1);
    }

    printf("Connected to server...\n");

    // Receive file name from server (not required in this example)
    // ...

    // Send file name to server
    send(sock, filename, strlen(filename), 0);

    // Close socket
    close(sock);

    return 0;
}
````

## **Theorems and Definitions**

- **TCP Three-Way Handshake**: A set of three handshakes used to establish a connection between the client and server.
- **SYN**: Synchronize packet used to initiate a connection.
- **ACK**: Acknowledgment packet used to acknowledge the receipt of a packet.
- **FIN**: Finish packet used to terminate a connection.

## **Important Formulas**

- **Socket Creation Formula**: `sock = socket(AF_INET, SOCK_STREAM, 0)`
- **Connect Formula**: `if (connect(sock, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) { ... }`
- **Send Formula**: `send(sock, buffer, len, 0)`
- **Receive Formula**: `recv(sock, buffer, len, 0)`

Note: This is a basic summary of the client-server program for file transfer. You may need to modify the code to suit your specific requirements.
