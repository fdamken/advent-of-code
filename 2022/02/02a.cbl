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
                05 WS-PlayerMove   pic A.
             01 WS-Score         pic 9(10) value zeros.
             01 WS-Score-Display pic z(10).
             01 WS-EOF           pic 9 value zero.
       procedure division.
           open input Strategy
             perform until WS-EOF = 1
               read Strategy into WS-Strategy
                 at end move 1 to WS-EOF
                 not at end
                   evaluate WS-PlayerMove
                     when "X"
                       add 1 to WS-Score
                     when "Y"
                       add 2 to WS-Score
                     when "Z"
                       add 3 to WS-Score
                     when other
                       display "Invalid player move: "WS-PlayerMove
                   end-evaluate
                   evaluate WS-OpponentMove also WS-PlayerMove
      *              scissors (C) < rock (X)
                     when "C" also "X"
      *              paper (B) < scissors (Z)
                     when "B" also "Z"
      *              rock (A) < paper (Y)
                     when "A" also "Y"
                       add 6 to WS-Score
      *              draw situations
                     when "A" also "X"
                     when "B" also "Y"
                     when "C" also "Z"
                       add 3 to WS-Score
                   end-evaluate
                   display WS-Score
               end-read
             end-perform
           close Strategy
           move WS-Score to WS-Score-Display
           display "Final score: "WS-Score-Display
           stop run.
