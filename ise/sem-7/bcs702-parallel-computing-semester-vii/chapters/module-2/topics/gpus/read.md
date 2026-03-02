c
// Kernel Function (runs on GPU)
__global__ void vecAdd(float* A, float* B, float* C, int n) {
    int i = threadIdx.x + blockIdx.x * blockDim.x; // Unique thread ID
    if (i < n) {
        C[i] = A[i] + B[i]; // Each thread does one addition
    }
}

// Host Code (runs on CPU)
int main() {
    // ... allocate and initialize host/device arrays A, B, C
    // Copy data from Host (CPU RAM) to Device (GPU VRAM)
    cudaMemcpy(dev_A, A, size, cudaMemcpyHostToDevice);
    // Determine grid and block sizes (e.g., 256 threads per block)
    int threadsPerBlock = 256;
    int blocks = (n + threadsPerBlock - 1) / threadsPerBlock;
    // Launch the kernel on the GPU
    vecAdd<<<blocks, threadsPerBlock>>>(dev_A, dev_B, dev_C, n);
    // Copy result back from Device to Host
    cudaMemcpy(C, dev_C, size, cudaMemcpyDeviceToHost);
}