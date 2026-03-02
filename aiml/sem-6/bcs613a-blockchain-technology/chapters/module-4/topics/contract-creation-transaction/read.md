json
{
  "from": "0x742d35Cc6634C893292...", // Sender's address
  "nonce": 5,                       // Transaction sequence number
  "gasPrice": "20000000000",         // Price per unit of gas (in wei)
  "gas": "2000000",                  // Max gas allotted for execution
  "value": "0",                      // Ether sent to the new contract (can be >0)
  "data": "0x6060604052341561000f57...", // The crucial part: Contract Bytecode
  "to": null                         // This is left EMPTY for creation tx
}