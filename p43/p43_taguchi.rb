n, s, t = 0, [], []
File.open(ARGV[0]) { |file| file.each_with_index do |line, i| 
  n = line.chomp.to_i if i == 0
  s << line.chomp.to_i if 0 < i && i <= n 
  t << line.chomp.to_i if n < i
end }
itv = []
for i in 0..(n - 1) do
  a = []
  a << t[i]
  a << s[i]
  itv << a
end
itv.sort!
ans, t = 0, 0
for i in 0..(n - 1) do
  if t < itv[i][1]
    ans += 1
    t = itv[i][0]
  end
end
p ans
