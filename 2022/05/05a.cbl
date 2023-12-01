       identification division.
           program-id. Day-05a.
       environment division.
           input-output section.
             file-control.
               select CargoCrane assign to "input.txt"
                 organization is line sequential.
       data division.
           file section.
             fd CargoCrane.
                01 Line-Str pic A(100).
           working-storage section.
             01 WS-CargoCrane.
                05 WS-Line pic A(100).
             01 WS-PreviousLine   pic A(100).
             01 WS-StacksLineNo   pic 999.
             01 WS-StackCount     pic 999.
             01 WS-StackCount-Str pic AAA.
             01 WS-Stacks
                occurs 0 to 999 times depending on WS-StackCount.
                05 WS-Stack pic A occurs 26 times.
             01 WS-MoveInstrCount pic 9(10).
             01 WS-MoveInstr
                occurs 0 to 1000 times depending on WS-MoveInstrCount.
                05 WS-MoveCount pic 99.
                05 WS-MoveFrom  pic 999.
                05 WS-MoveTo    pic 999.
             01 WS-MoveFromIdx    pic 999.
             01 WS-MoveToIdx      pic 999.
             01 WS-StackLevel     pic 99.
             01 WS-Str            pic A(100).
             01 WS-StrLength      pic 999.
             01 WS-i              pic 999.
             01 WS-j              pic 999.
             01 WS-k              pic 999.
             01 WS-print-i        pic 999.
             01 WS-print-j        pic 999.
             01 WS-print-var      pic A(100).
             01 WS-end            pic 999.
             01 WS-EOF            pic 9 value zero.
             01 placeholder       pic A(100).
       procedure division.
      *    first extract the number of stacks
           open input CargoCrane
             move 0 to WS-EOF
             move 1 to WS-StacksLineNo
             perform varying WS-j from 1 by 1 until WS-EOF = 1
               read CargoCrane into WS-CargoCrane
                 at end move 1 to WS-EOF
                 not at end
                   if WS-Line equals " " then
                     move WS-PreviousLine to WS-Str
                     perform compute-str-length
                     move WS-StrLength to WS-end
                     move WS-StrLength to WS-i
                     move "  " to WS-StackCount-Str
                     perform until WS-i <= 1
                       if function test-numval(WS-PreviousLine(WS-i:1))
                          equals zero then
                         move function concatenate(
                             WS-PreviousLine(WS-i:1),
                             WS-StackCount-Str
                           ) to WS-StackCount-Str
                       else
                         move 1 to WS-i
                       end-if
                       subtract 1 from WS-i
                     end-perform
                     move function numval(WS-StackCount-Str)
                       to WS-StackCount
                     subtract 1 from WS-j giving WS-StacksLineNo
                     move 1 to WS-EOF
                   end-if
                   move WS-Line to WS-PreviousLine
               end-read
             end-perform
           close CargoCrane

           display "stack count: " WS-StackCount

           open input CargoCrane
             move 0 to WS-EOF
             move 1 to WS-StackLevel
             move 0 to WS-MoveInstrCount
             perform varying WS-j from 1 by 1 until WS-EOF = 1
               read CargoCrane into WS-CargoCrane
                 at end move 1 to WS-EOF
                 not at end
                   if WS-j < WS-StacksLineNo then
      *              we are still reading the stack contents
                     move 1 to WS-i
                     perform varying WS-i
                             from 1
                             by 1
                             until WS-i equals WS-StackCount + 1
                       move WS-Line((WS-i - 1) * 4 + 2 : 1)
                         to WS-Stack(
                              WS-i,
                              WS-StacksLineNo - WS-StackLevel
                            )
                     end-perform
                     add 1 to WS-StackLevel
                   else
                     if WS-j > WS-StacksLineNo + 1 then
      *                we are finally reading the move instructions
                       add 1 to WS-MoveInstrCount
                       unstring WS-Line delimited by all space
                         into placeholder
                              WS-MoveCount(WS-MoveInstrCount)
                              placeholder
                              WS-MoveFrom(WS-MoveInstrCount)
                              placeholder
                              WS-MoveTo(WS-MoveInstrCount)
                       end-unstring
                     end-if
                   end-if
               end-read
             end-perform
           close CargoCrane

           perform print-stacks

      *    we read all the data and can start moving stuff around
           perform varying WS-i
                   from 1
                   by 1
                   until WS-i > WS-MoveInstrCount
             perform varying WS-j
                     from 0
                     by 1
                     until WS-j = WS-MoveCount(WS-i)
               display "move " WS-MoveFrom(WS-i) " to " WS-MoveTo(WS-i)
               move 0 to WS-MoveToIdx
               perform varying WS-k from 1 by 1 until WS-k > 26
                 if WS-Stack(WS-MoveFrom(WS-i), WS-k) not equals " "
                   move WS-k to WS-MoveFromIdx
                 end-if
                 if WS-MoveToIdx equals 0 then
                   if WS-Stack(WS-MoveTo(WS-i), WS-k) equals " " then
                     move WS-k to WS-MoveToIdx
                   end-if
                 end-if
               end-perform
               move WS-Stack(WS-MoveFrom(WS-i), WS-MoveFromIdx)
                 to WS-Stack(WS-MoveTo(WS-i), WS-MoveToIdx)
               move " " to WS-Stack(WS-MoveFrom(WS-i), WS-MoveFromIdx)
      *        perform print-stacks
             end-perform
           end-perform

           display "----- MOVING FINISHED -----"
           perform print-stacks

           stop run.


           compute-str-length.
             move 1 to WS-i
             move 0 to WS-StrLength
             perform until WS-i = function length(WS-Str)
               if WS-Str(WS-i:1) not equals " " then
                 move WS-i to WS-StrLength
               end-if
               add 1 to WS-i
             end-perform
           .

           print-stacks.
             display "stacks (top-down reversed):"
             perform varying WS-print-j
                     from 1
                     by 1
                     until WS-print-j > 26
               move " " to WS-print-var
               perform varying WS-print-i
                       from WS-StackCount
                       by -1
                       until WS-print-i = 0
                 move function concatenate(
                     WS-Stack(WS-print-i, WS-print-j),
                     WS-print-var
                   ) to WS-print-var
               end-perform
               if WS-print-var not equals " " then
                 display "  " WS-print-var
               end-if
             end-perform
           .
