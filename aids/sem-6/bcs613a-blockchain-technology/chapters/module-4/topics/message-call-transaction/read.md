solidity
// Contract A
contract ContractA {
    function doSomething() public {
        // This creates an INTERNAL message call to ContractB
        ContractB(0x5678...).someFunction();
    }
}