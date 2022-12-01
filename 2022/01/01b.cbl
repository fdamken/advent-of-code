       IDENTIFICATION DIVISION.
         PROGRAM-ID. Day-01.
       ENVIRONMENT DIVISION.
         INPUT-OUTPUT SECTION.
           FILE-CONTROL.
             SELECT Elves ASSIGN TO "input.txt"
               ORGANIZATION IS LINE SEQUENTIAL.
       DATA DIVISION.
         FILE SECTION.
           FD Elves.
              01 Elves-FILE.
                 05 Calories-Str PIC A(8).
         WORKING-STORAGE SECTION.
           01 WS-Elves.
              05 WS-Calories-Str PIC A(8).
           01 WS-Calories PIC 9(16).
           01 WS-EOF PIC Z(1) VALUE 0.
           01 WS-CurrentCaloriesTotal PIC 9(16) VALUE 0.
           01 WS-NumberOfElves PIC 9(8) VALUE 0.
           01 WS-Elve-Table.
              05 WS-ElveCalories PIC 9(8)
                 OCCURS 0 TO 1000 TIMES DEPENDING ON WS-NumberOfElves.
           01 WS-TotalCalories PIC 9(16) VALUE 0.
           01 WS-TotalCalories-Display PIC Z(16).
       PROCEDURE DIVISION.
         OPEN INPUT Elves.
           PERFORM UNTIL WS-EOF = 1
             READ Elves INTO WS-Elves
               AT END MOVE 1 TO WS-EOF
               NOT AT END
                 MOVE FUNCTION NUMVAL(WS-Calories-Str) TO WS-Calories
                 IF WS-Calories > 0
                   ADD WS-Calories TO WS-CurrentCaloriesTotal
                 ELSE
                   ADD 1 TO WS-NumberOfElves
                   MOVE WS-CurrentCaloriesTotal
                     TO WS-ElveCalories(WS-NumberOfElves)
                   MOVE 0 TO WS-CurrentCaloriesTotal
                 END-IF
             END-READ
           END-PERFORM.
           SORT WS-ElveCalories ON DESCENDING KEY WS-ElveCalories.
           ADD WS-ElveCalories(1) WS-ElveCalories(2) WS-ElveCalories(3)
             TO WS-TotalCalories.
           MOVE WS-TotalCalories TO WS-TotalCalories-Display.
           DISPLAY "Top three calories:" WS-TotalCalories-Display.
         CLOSE Elves.
         STOP RUN.
