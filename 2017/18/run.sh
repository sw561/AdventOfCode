go build
./18 input > o 2> /dev/null
head -n 1 o > out
tail -n 1 o >> out
rm o
cat out
rm out
go clean
