import re

badchars = (
    "\x00\x0A\x0D"
    "\x2F"
    "\x3A\x3F"
    "\x40"
    "\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8A\x8B\x8C\x8D\x8E\x8F"
    "\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9A\x9B\x9C\x9D\x9E\x9F"
    "\xA0\xA1\xA2\xA3\xA4\xA5\xA6\xA7\xA8\xA9\xAA\xAB\xAC\xAD\xAE\xAF"
    "\xB0\xB1\xB2\xB3\xB4\xB5\xB6\xB7\xB8\xB9\xBA\xBB\xBC\xBD\xBE\xBF"
    "\xC0\xC1\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xCB\xCC\xCD\xCE\xCF"
    "\xD0\xD1\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xDB\xDC\xDD\xDE\xDF"
    "\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF"
    "\xF0\xF1\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9\xFA\xFB\xFC\xFD\xFE\xFF"
)

contents = ""
with open("rop.txt", "r") as f:
    contents = f.read()
lines = contents.split("\n")
print "\nPotential Candidates without Bad Characters\n"

addr_dict = {}

for i in lines:
    if i.count("POP") > 1:
        addr = i.split(",")[0]
        extracted = re.findall(r'0x[0-9A-F]+', addr, re.I)
        for j in extracted:
            if not j in addr_dict:
                addr_dict[j] = i.strip()

for k, v in addr_dict.items():
    seq_addr = k.replace("0x", "")
    tmp_addr = [seq_addr[j:j+2] for j in range(0, len(seq_addr), 2)]
    bad = 0
    for j in tmp_addr:
        addr_byte = int(j, 16)
        #if addr_byte == 0:
        #    continue
        for i in badchars:
            if addr_byte == ord(i):
                bad = 1
                break
    if bad == 0:
        print k + " - " + v