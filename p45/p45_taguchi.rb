n, s = 0, ''
File.open(ARGV[0]) { |file| file.each_with_index { |line, i| i == 0 ? n = line.chomp : s = line.chomp } }
reverse_s, t = s.reverse, ''
while !s.empty? do
  if s < reverse_s
    t << s.slice!(0)
    reverse_s.chop!
  else
    t << reverse_s.slice!(0)
    s.chop!
  end
end
p t

