solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Counter {
    uint public count;

    constructor(uint _initialCount) {
        count = _initialCount;
    }

    function increment() public {
        count += 1;
    }
}