# Network Attack Detection - Summary

## Key Definitions and Concepts
- **IDS**: System monitoring network for malicious activities  
- **True Positive Rate**: Proportion of attacks correctly identified  
- **Zero-Day Attack**: Exploit for which no signature exists  
- **Feature Engineering**: Creating input parameters for ML models from raw PCAP data  

## Important Formulas and Theorems
- **Entropy Calculation**: H(X) = -Σ p(x_i)log₂p(x_i) for detecting scan attacks  
- **SVM Decision Boundary**: w·x - b = 0 where w is normal vector  
- **LSTM Cell**: f_t = σ(W_f · [h_{t-1}, x_t] + b_f) (Forget gate equation)  
- **F1 Score**: 2*(Precision*Recall)/(Precision+Recall)  

## Key Points
- Hybrid systems reduce false positives by 40% compared to single-method approaches  
- Graph Neural Networks effectively detect lateral movement in APT attacks  
- QUIC protocol presents new challenges for encrypted traffic analysis  
- Adversarial training improves ML model robustness against evasion attacks  
- FPGA-based detection achieves 100Gbps throughput for real-time processing  
- Federated learning enables privacy-preserving collaborative detection  
- MITRE ATT&CK framework is essential for attack pattern analysis  

## Common Mistakes to Avoid
- Using accuracy alone as detection performance metric (imbalanced datasets)  
- Neglecting feature normalization before applying SVM/RF algorithms  
- Overlooking timestamp granularity in flow-based detection  
- Failing to update threat intelligence feeds in signature-based systems  

## Revision Tips
1. Create comparison tables: Snort vs. Suricata vs. Zeek capabilities  
2. Practice ROC curve plotting for different threshold values  
3. Study IETF RFCs related to NETCONF/YANG for SDN-based detection  
4. Implement simple autoencoder for KDDCUP99 dataset using PyTorch  
5. Review latest CVE entries to understand current attack patterns