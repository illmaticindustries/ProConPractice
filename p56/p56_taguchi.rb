n, m, s, t = 0, 0, '', ''
File.open(ARGV[0]) { |file| file.each_with_index do |line, i|
  case i
  when 0
    n = line.chomp.to_i
  when 1
    m = line.chomp.to_i
  when 2
    s = line.chomp
  else
    t = line.chomp
  end
end }

length_table = Array.new(n + 1).map { Array.new(m + 1, 0) }
for i in 0..(n - 1)
  for j in 0..(m - 1)
    length_table[i + 1][j + 1] = s[i] == t[j] ? length_table[i][j] + 1 : [length_table[i + 1][j], length_table[i][j + 1]].max
  end
end
p length_table[n][m]

