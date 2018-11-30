echo "Part 1"
sed "s/[^0-9-]\+/ /g" 12_input | python3 -c "x = input(); print(sum(int(i) for i in x.split()))"
echo "Part 2"
./2015_12.py < 12_input | sed "s/[^0-9-]\+/ /g" | python3 -c "x = input(); print(sum(int(i) for i in x.split()))"
