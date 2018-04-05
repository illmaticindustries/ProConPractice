n, max_weight, weights, values = 0, 0, [], []
File.open(ARGV[0]) { |file| file.each_with_index do |line, i|
  if i == 0
    n = line.chomp.to_i
  elsif i == 1
    max_weight = line.chomp.to_i
  else
    a = line.chomp.split(',')
    weights << a[0].to_i
    values << a[1].to_i
  end
end }

value_table = Array.new(max_weight + 1, 0)
for i in 0..(n - 1) do
  for w in weights[i]..max_weight
    value_table[w] = [
      value_table[w],
      value_table[w - weights[i]] + values[i]
    ].max
  end
end
p value_table[max_weight]
