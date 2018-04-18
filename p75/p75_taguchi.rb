n, l = 0, []
File.open(ARGV[0]) { |file| file.each_with_index do |line, i|
  case i
  when 0
    n = line.chomp.to_i
  else
    l = line.chomp.split(',').map(&:to_i)
  end
end }

ans = 0
while 1 < l.length do
  l.sort!
  arry = l.shift 2
  arrysum = arry.inject(:+)
  l.push arrysum
  ans += arrysum 
end
p ans
