xxd -p original.txt | fold -w 2 > original.hex
cat 618d0e51213fa164d93bd92ca5e099c3.txt | cut -d ' ' -f -16 | tr -d ' ' | fold -w 2 > modified.hex
diff -y --suppress-common-lines *.hex > diff.txt
cat diff.txt | cut -f 1 | tr '\n' ' ' > flag.txt
python
for i in open('flag.txt').readline().split():
  print(chr(int(i, 16)), end='')