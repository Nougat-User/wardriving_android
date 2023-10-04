sort -u output_raw.txt > output.txt
while IFS= read -r line; do
  cmd="cmd wifi connect-network $line -d"
  echo "$cmd" >> add_network.sh
done < output.txt
rm -f {output.txt,output_raw.txt}
