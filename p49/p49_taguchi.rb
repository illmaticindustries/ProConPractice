l = []
File.open(ARGV[0]) { |file| file.each_with_index { |line, i| i == 0 ? n = line.chomp.to_i : l << line.chomp.to_i } }

ans = 0
while l.length > 1 do
  l.sort!
  t = 0
  2.times { t += l.shift }
  ans += t
  l.push t 
end
p ans
