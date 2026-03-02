solidity
// PSEUDO-CODE - For conceptual understanding only
contract EscrowTemplate {
    address public buyer;
    address public seller;
    uint public amount;
    bool public goodsReceived;

    // Constructor function acts as the parameterizer
    constructor(address _seller) payable {
        buyer = msg.sender; // The deployer is the buyer
        seller = _seller;
        amount = msg.value; // Ether sent with deployment
        goodsReceived = false;
    }

    function confirmReceipt() public {
        require(msg.sender == buyer, "Only buyer can confirm");
        goodsReceived = true;
        payable(seller).transfer(amount); // Release funds to seller
    }

    function abort() public {
        require(msg.sender == buyer, "Only buyer can abort");
        payable(buyer).transfer(amount); // Return funds to buyer
    }
}