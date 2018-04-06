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
MAX_N = 100
MAX_V = 100
INF = 1_000_000
weight_table = Array.new(MAX_N + 1).map { Array.new(MAX_N * MAX_N + 1) }
weight_table[0].fill INF
weight_table[0][0] = 0
for i in 0..(n - 1)
  for v in 0..(MAX_N * MAX_N)
    if v < values[i]
      weight_table[i + 1][v] = weight_table[i][v]
    else
      weight_table[i + 1][v] = [
        weight_table[i][v],
        weight_table[i][v - values[i]] + weights[i]
      ].min
    end
  end
end
res = 0
for i in 0..(MAX_N * MAX_N)
  if weight_table[n][i] <= max_weight
    res = i
  end
end
p res 
