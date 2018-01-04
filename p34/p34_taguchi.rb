array = []
File.open('./p34.in') { |file| file.each_line { |line| array << line.chomp } }
@a = array[1].split(',').map(&:to_i)
@k = array[2].to_i

def check(i, sum)
  if i == @a.count then @k == sum
  elsif check(i + 1, sum + @a[i]) then true
  elsif check(i + 1, sum) then true
  else false
  end
end

check(0, 0) ? p('Yes') : p('No')
