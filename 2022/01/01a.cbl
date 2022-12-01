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
           01 WS-CurrentCaloriesTotal PIC 9(16).
           01 WS-CurrentMaximum PIC 9(16).
           01 WS-MaximumDisplay PIC Z(16).
           01 WS-EOF PIC Z(1) VALUE 0.
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
                   IF WS-CurrentCaloriesTotal > WS-CurrentMaximum
                     MOVE WS-CurrentCaloriesTotal TO WS-CurrentMaximum
                   END-IF
                   MOVE 0 TO WS-CurrentCaloriesTotal
                 END-IF
             END-READ
           END-PERFORM.
         CLOSE Elves.
         MOVE WS-CurrentMaximum TO WS-MaximumDisplay.
         DISPLAY "Maximum number of calories:" WS-MaximumDisplay.
         STOP RUN.
