def read_file(file_name)
  array = []
  File.open("p47/#{file_name}") do |file|
    file.each_line do |line|
      array << line.chomp
    end
  end
  p @r = array[1].to_i
  p @x = array[2..-1].map(&:to_i)
end

def count(file)
  read_file(file)
  x_array = @x
  r = @r
  count = 0

  loop do
    r_point = x_array.first + @r
    break if x_array.select! { |x| x > r_point }.empty?
    # 最初の印を見つける
    # p x_array.select! { |x| x > r_point }
    count += 1
  end
  p count
end

count('p47.in')
count('p47_1.in')
count('p47_2.in')
count('p47_3.in')
