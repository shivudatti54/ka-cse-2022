T1: R(A)
T2: R(A)  // Conflict with T1's subsequent W(A)?
T1: W(A)  // This W(A) conflicts with T2's earlier R(A)
T2: W(A)  // This W(A) conflicts with T1's earlier W(A)
T1: Commit
T2: Commit