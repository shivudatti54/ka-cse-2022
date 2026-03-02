javascript
// Pseudocode example using Truffle's style
it("should throw an error when trying to transfer more than balance", async function() {
  await expectRevert(
    myWallet.transfer(recipient, 1000), // Attempt to transfer 1000 tokens
    "Insufficient balance" // Expected error message
  );
});