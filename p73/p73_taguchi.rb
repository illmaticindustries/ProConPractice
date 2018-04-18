n, l, p, a, b = 0, 0, 0, [], []
File.open(ARGV[0]) { |file| file.each_with_index do |line, i|
  case i
  when 0
    n = line.chomp.to_i
  when 1
    l = line.chomp.to_i
  when 2
    p = line.chomp.to_i
  when 3
    a = line.chomp.split(',').map(&:to_i)
  else
    b = line.chomp.split(',').map(&:to_i)
  end
end }

a[n], b[n] = l, 0
n += 1
que = []
ans, pos, tank = 0, 0, p

for i in 0..(n - 1)
  que.sort!
  d = a[i] - pos
  while tank < d do
    if que.empty? 
      ans = -1
      break
    end
    tank += que.pop
    ans += 1
  end
  tank -= d
  pos = a[i]
  que.push b[i]
end
puts ans

