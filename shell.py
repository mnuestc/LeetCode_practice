cat file.txt | awk '{if (NR==10){print $0}}'
sed -n "10p" file.txt

count=0
while read line; do
  ((++count))
  if [ "${count}" -eq 10 ]; then
    echo "${line}"
  fi
done < file.txt