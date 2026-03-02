solidity
function purchaseItem() public payable {
    require(msg.value == 1 ether, "Must send exactly 1 Ether");
    balances[msg.sender] += 1; // Give the sender an item
}