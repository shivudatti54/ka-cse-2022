solidity
function vote(uint candidateId) public {
    require(!hasVoted[msg.sender], "You have already voted.");
    hasVoted[msg.sender] = true;
    votesReceived[candidateId]++;
}