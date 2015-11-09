def read_file(file_name)
  array = []
  File.open("p45/#{file_name}") do |file|
    file.each_line do |line|
      array << line.chomp
    end
  end
  @n = array[0]
  @s = array[1]
end

def jobs(file)
  read_file(file)
  s = @s
  reverse_s = @s.reverse
  t = ''
  p "s: #{s}"

  loop do
    if s < reverse_s
      t << s.slice!(0)
      reverse_s.chop!
    else
      t << reverse_s.slice!(0)
      s.chop!
    end
    p "t: #{t}"
    p '---'
    p "s: #{s}"
    break if s.empty?
  end

  p "t: #{t}"
end

jobs('p45.in')
jobs('p45_1.in')
jobs('p45_2.in')
jobs('p45_3.in')
