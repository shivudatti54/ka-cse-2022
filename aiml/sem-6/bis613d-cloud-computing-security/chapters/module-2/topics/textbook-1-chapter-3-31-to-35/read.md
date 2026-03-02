# **Textbook 1: Chapter 3: 3.1 to 3.5**

## **3.1: Introduction to Virtualization**

### Definition

Virtualization is the process of creating a virtual environment that mimics the physical environment, allowing multiple virtual machines (VMs) to run on a single physical host.

### Types of Virtualization

- **Hardware Virtualization**: Uses a hypervisor to create multiple VMs on a single physical host.
- **Software Virtualization**: Uses software to create multiple VMs on a single physical host.

### Benefits of Virtualization

- **Improved Resource Utilization**: VMs can be allocated specific resources, improving utilization and reducing waste.
- **Increased Flexibility**: VMs can be easily created, cloned, and migrated, improving flexibility.
- **Disaster Recovery**: VMs can be easily backed up and restored, improving disaster recovery.

### Example

- A company has a physical server with 4 CPUs, 8 GB of RAM, and 2 TB of storage. By using hardware virtualization, the company can create 4 VMs, each with 2 CPUs, 2 GB of RAM, and 500 GB of storage.

## **3.2: Virtual Machine (VM) Architecture**

### Components of a VM

- **Hypervisor**: The software that creates and manages VMs.
- **VM Monitor**: The software that manages the VM's hardware resources.
- **Guest Operating System**: The operating system that runs inside the VM.
- **Device Drivers**: Software that enables the VM to interact with the physical host's hardware.

### Types of VMs

- **Type 1 VMs**: Also known as bare-metal VMs, these VMs run directly on the host machine.
- **Type 2 VMs**: Also known as hosted VMs, these VMs run on top of an existing operating system.

### Example

- A company has a physical server with a Type 1 hypervisor installed. The company can create a Type 1 VM, which will run directly on the host machine.

## **3.3: Virtual Machine (VM) Migration**

### Types of VM Migration

- **Live Migration**: The VM is migrated while it is running.
- **Cold Migration**: The VM is shut down on the source host and restarted on the destination host.

### Benefits of VM Migration

- **Improved Resource Utilization**: VMs can be allocated specific resources, improving utilization and reducing waste.
- **Increased Flexibility**: VMs can be easily created, cloned, and migrated, improving flexibility.
- **Disaster Recovery**: VMs can be easily backed up and restored, improving disaster recovery.

### Example

- A company has a physical server with a live migration capability. The company can migrate a VM from one host to another, without shutting down the VM.

## **3.4: Virtualized Cluster Architecture**

### Types of Virtualized Clusters

- **Single-Host Clusters**: A single host machine is used to create multiple VMs.
- **Multi-Host Clusters**: Multiple host machines are used to create multiple VMs.

### Benefits of Virtualized Clusters

- **Improved Resource Utilization**: VMs can be allocated specific resources, improving utilization and reducing waste.
- **Increased Flexibility**: VMs can be easily created, cloned, and migrated, improving flexibility.
- **Disaster Recovery**: VMs can be easily backed up and restored, improving disaster recovery.

### Example

- A company has a multi-host cluster with 4 host machines. The company can create multiple VMs on each host machine, improving resource utilization and flexibility.

## **3.5: Virtualized Data Center Architecture**

### Types of Virtualized Data Centers

- **Single-Host Data Centers**: A single host machine is used to create multiple VMs.
- **Multi-Host Data Centers**: Multiple host machines are used to create multiple VMs.

### Benefits of Virtualized Data Centers

- **Improved Resource Utilization**: VMs can be allocated specific resources, improving utilization and reducing waste.
- **Increased Flexibility**: VMs can be easily created, cloned, and migrated, improving flexibility.
- **Disaster Recovery**: VMs can be easily backed up and restored, improving disaster recovery.

### Example

- A company has a multi-host data center with 16 host machines. The company can create multiple VMs on each host machine, improving resource utilization and flexibility.
