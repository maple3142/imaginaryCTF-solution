import re
s="""
.data:00000000000041A0 off_41A0        dq offset c32           ; DATA XREF: main+27↑o
.data:00000000000041A8                 dq offset c16
.data:00000000000041B0                 dq offset c22
.data:00000000000041B8                 dq offset c19
.data:00000000000041C0                 dq offset c36
.data:00000000000041C8                 dq offset c15
.data:00000000000041D0                 dq offset c35
.data:00000000000041D8                 dq offset c0
.data:00000000000041E0                 dq offset c14
.data:00000000000041E8                 dq offset c25
.data:00000000000041F0                 dq offset c13
.data:00000000000041F8                 dq offset c4
.data:0000000000004200                 dq offset c28
.data:0000000000004208                 dq offset c10
.data:0000000000004210                 dq offset c29
.data:0000000000004218                 dq offset c2
.data:0000000000004220                 dq offset c12
.data:0000000000004228                 dq offset c21
.data:0000000000004230                 dq offset c17
.data:0000000000004238                 dq offset c34
.data:0000000000004240                 dq offset c18
.data:0000000000004248                 dq offset c30
.data:0000000000004250                 dq offset c37
.data:0000000000004258                 dq offset c23
.data:0000000000004260                 dq offset c7
.data:0000000000004268                 dq offset c1
.data:0000000000004270                 dq offset c11
.data:0000000000004278                 dq offset c26
.data:0000000000004280                 dq offset c24
.data:0000000000004288                 dq offset c33
.data:0000000000004290                 dq offset c27
.data:0000000000004298                 dq offset c5
.data:00000000000042A0                 dq offset c38
.data:00000000000042A8                 dq offset c3
.data:00000000000042B0                 dq offset c31
.data:00000000000042B8                 dq offset c8
.data:00000000000042C0                 dq offset c20
.data:00000000000042C8                 dq offset c6
.data:00000000000042D0                 dq offset c9
.data:00000000000042D8                 dq offset c39
"""[1:-1]

for l in s.splitlines():
    m = re.search(r'c(\d+)',l)
    print('&c'+str(m.group(1))+',')
