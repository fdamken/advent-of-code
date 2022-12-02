       identification division.
           program-id. Day-02a.
       environment division.
           input-output section.
             file-control.
               select Strategy assign to "input.txt"
                 organization is line sequential.
       data division.
           file section.
             fd Strategy.
               01 Strategy-FILE.
                  05 OpponentMove pic A.
                  05 placeholder  pic A.
                  05 PlayerMove   pic A.
           working-storage section.
             01 WS-Strategy.
                05 WS-OpponentMove pic A.
                05 WS-placeholder  pic A.
                05 WS-Outcome      pic A.
             01 WS-PlayerMove    pic A.
             01 WS-Score         pic 9(10) value zeros.
             01 WS-Score-Display pic z(10).
             01 WS-EOF           pic 9 value zero.
       procedure division.
           open input Strategy
             perform until WS-EOF = 1
               read Strategy into WS-Strategy
                 at end move 1 to WS-EOF
                 not at end
                   evaluate WS-OpponentMove also WS-Outcome
      *              we need a draw
                     when "A" also "Y"
                     when "B" also "Y"
                     when "C" also "Y"
                       move WS-OpponentMove to WS-PlayerMove
      *              we need a lose
                     when "A" also "X"
                       move "C" to WS-PlayerMove
                     when "B" also "X"
                       move "A" to WS-PlayerMove
                     when "C" also "X"
                       move "B" to WS-PlayerMove
      *              we need a win
                     when "A" also "Z"
                       move "B" to WS-PlayerMove
                     when "B" also "Z"
                       move "C" to WS-PlayerMove
                     when "C" also "Z"
                       move "A" to WS-PlayerMove
                   end-evaluate
                   evaluate WS-PlayerMove
                     when "A"
                       add 1 to WS-Score
                     when "B"
                       add 2 to WS-Score
                     when "C"
                       add 3 to WS-Score
                   end-evaluate
                   evaluate WS-OpponentMove also WS-PlayerMove
      *              scissors (C) < rock (C)
                     when "C" also "A"
      *              paper (B) < scissors (C)
                     when "B" also "C"
      *              rock (A) < paper (Y)
                     when "A" also "B"
                       add 6 to WS-Score
      *              draw situations
                     when "A" also "A"
                     when "B" also "B"
                     when "C" also "C"
                       add 3 to WS-Score
                   end-evaluate
               end-read
             end-perform
           close Strategy
           move WS-Score to WS-Score-Display
           display "Final score: "WS-Score-Display
           stop run.
