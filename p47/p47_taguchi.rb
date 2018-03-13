n, r, x = 0, 0, []
File.open(ARGV[0]) { |file| file.each_with_index do |line, i|
  n = line.chomp.to_i if i == 0
  r = line.chomp.to_i if i == 1
  x << line.chomp.to_i if 1 < i 
end }

i, ans = 0, 0
while i < n do
  start = x[i]
  while i < n && x[i] <= start + r do i += 1 end
  point = x[i - 1]
  while i < n && x[i] <= point + r do i += 1 end
  ans += 1
end
p ans
