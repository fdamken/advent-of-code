       identification division.
           program-id. Day-03a.
       environment division.
           input-output section.
             file-control.
               select Rucksacks assign to "input.txt"
                 organization is line sequential.
       data division.
           file section.
             fd Rucksacks.
                01 Rucksacks-FILE.
                   05 Item pic A(50).
           working-storage section.
             01 WS-Rucksacks.
                05 WS-Item pic A(50).
                05 WS-Item-Table
                   redefines WS-Item
                   pic A
                   occurs 50 times.
             01 WS-ItemLength pic 99.
             01 WS-Group pic 9.
             01 WS-GroupItems pic A(50) occurs 3 times.
             01 WS-GroupItemLengths pic 99 occurs 3 times.
             01 WS-Str pic A(50).
             01 WS-Str-Table redefines WS-Str pic A occurs 50 times.
             01 WS-StrLength pic 99.
             01 WS-Duplicate pic A.
             01 WS-DuplicatePriority pic 9(10).
             01 WS-TotalPriority pic 9(10) value zero.
             01 WS-TotalPriority-Display
                redefines WS-TotalPriority
                pic Z(10).
             01 WS-i pic 9(10).
             01 WS-j pic 9(10).
             01 WS-k pic 9(10).
             01 WS-EOF pic 9 value zero.
             01 WS-OrdBaseLower pic 9(19).
             01 WS-OrdBaseUpper pic 9(19).
       procedure division.
           move function ord("a") to WS-OrdBaseLower
           move function ord("A") to WS-OrdBaseUpper
           subtract 1 from WS-OrdBaseLower
           subtract 1 from WS-OrdBaseUpper

           open input Rucksacks
             move 1 to WS-Group
             perform until WS-EOF = 1
               read Rucksacks into WS-Rucksacks
                 at end move 1 to WS-EOF
                 not at end
                   move WS-Item to WS-GroupItems(WS-Group)
                   move WS-GroupItems(WS-Group) to WS-Str
                   perform compute-str-length
                   move WS-StrLength to WS-GroupItemLengths(WS-Group)
                   if WS-Group = 3
                     perform find-duplicates
                     perform compute-priority
                     add WS-DuplicatePriority to WS-TotalPriority
                     move 1 to WS-Group
                   else
                     add 1 to WS-Group
                   end-if
               end-read
             end-perform
           close Rucksacks
           display WS-TotalPriority-Display
           stop run.

           compute-str-length.
             move 1 to WS-i
             perform until WS-Str-Table(WS-i) = " "
               add 1 to WS-i
             end-perform
             move WS-i to WS-StrLength
           .

           find-duplicates.
             move 1 to WS-i
             perform until WS-i = WS-GroupItemLengths(1)
               move WS-GroupItems(1)(WS-i:1) to WS-Duplicate
               move 1 to WS-j
               perform until WS-j = WS-GroupItemLengths(2)
                 if WS-Duplicate = WS-GroupItems(2)(WS-j:1) then
                   move 1 to WS-k
                   perform until WS-k = WS-GroupItemLengths(3)
                     if WS-Duplicate = WS-GroupItems(3)(WS-k:1) then
                       exit paragraph
                     end-if
                     add 1 to WS-k
                   end-perform
                 end-if
                 add 1 to WS-j
               end-perform
               add 1 to WS-i
             end-perform
             display "no duplicate found"
           .

           compute-priority.
             move function ord(WS-Duplicate) to WS-DuplicatePriority
             if function lower-case(WS-Duplicate) = WS-Duplicate then
               subtract WS-OrdBaseLower from WS-DuplicatePriority
             else
               subtract WS-OrdBaseUpper from WS-DuplicatePriority
               add 26 to WS-DuplicatePriority
             end-if
           .
