       identification division.
           program-id. Day-04b.
       environment division.
           input-output section.
             file-control.
               select Assignments assign to "input.txt"
                 organization is line sequential.
       data division.
           file section.
             fd Assignments.
                01 Assignments-File.
                   05 Assignment pic A(100).
           working-storage section.
             01 WS-Assignments.
                05 WS-Assignment pic A(100).
             01 WS-AssignmentElve1Lo    pic 9(10).
             01 WS-AssignmentElve1Hi    pic 9(10).
             01 WS-AssignmentElve2Lo    pic 9(10).
             01 WS-AssignmentElve2Hi    pic 9(10).
             01 WS-OverlapA             pic 9(10) occurs 2 times.
             01 WS-OverlapB             pic 9(10) occurs 2 times.
             01 WS-Overlap              pic 9.
             01 WS-OverlapTotal         pic 9(10) value zeros.
             01 WS-OverlapTotal-Display pic z(10).
             01 WS-EOF                  pic 9 value zero.
       procedure division.
           open input Assignments
             perform until WS-EOF = 1
               read Assignments into WS-Assignments
                 at end move 1 to WS-EOF
                 not at end
                   unstring WS-Assignment
                     delimited by "," or "-"
                     into WS-AssignmentElve1Lo
                          WS-AssignmentElve1Hi
                          WS-AssignmentElve2Lo
                          WS-AssignmentElve2Hi
                   move WS-AssignmentElve1Lo to WS-OverlapA(1)
                   move WS-AssignmentElve1Hi to WS-OverlapA(2)
                   move WS-AssignmentElve2Lo to WS-OverlapB(1)
                   move WS-AssignmentElve2Hi to WS-OverlapB(2)
                   perform has-overlap
                   add WS-Overlap to WS-OverlapTotal
               end-read
             end-perform
           close Assignments
           move WS-OverlapTotal to WS-OverlapTotal-Display
           display "total no. pairs: " WS-OverlapTotal-Display
           stop run.

           has-overlap.
             if WS-OverlapA(1) <= WS-OverlapB(2) and
                WS-OverlapB(1) <= WS-OverlapA(2) then
               move 1 to WS-Overlap
               exit paragraph
             end-if
             move 0 to WS-Overlap
           .
