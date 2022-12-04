       identification division.
           program-id. Day-04a.
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
             01 WS-AssignmentElve1Lo     pic 9(10).
             01 WS-AssignmentElve1Hi     pic 9(10).
             01 WS-AssignmentElve2Lo     pic 9(10).
             01 WS-AssignmentElve2Hi     pic 9(10).
             01 WS-ContainmentA          pic 9(10) occurs 2 times.
             01 WS-ContainmentB          pic 9(10) occurs 2 times.
             01 WS-Contains              pic 9.
             01 WS-ContainsTotal         pic 9(10) value zeros.
             01 WS-ContainsTotal-Display pic z(10).
             01 WS-EOF                   pic 9 value zero.
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
                   move WS-AssignmentElve1Lo to WS-ContainmentA(1)
                   move WS-AssignmentElve1Hi to WS-ContainmentA(2)
                   move WS-AssignmentElve2Lo to WS-ContainmentB(1)
                   move WS-AssignmentElve2Hi to WS-ContainmentB(2)
                   perform is-contained
                   add WS-Contains to WS-ContainsTotal
               end-read
             end-perform
           close Assignments
           move WS-ContainsTotal to WS-ContainsTotal-Display
           display "total no. pairs: " WS-ContainsTotal-Display
           stop run.

           is-contained.
             if WS-ContainmentA(1) <= WS-ContainmentB(1) and
                WS-ContainmentB(2) <= WS-ContainmentA(2) then
               move 1 to WS-Contains
               exit paragraph
             end-if
             if WS-ContainmentB(1) <= WS-ContainmentA(1) and
                WS-ContainmentA(2) <= WS-ContainmentB(2) then
               move 1 to WS-Contains
               exit paragraph
             end-if
             move 0 to WS-Contains
           .
