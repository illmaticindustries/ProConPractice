def read_file(file_name)
  @coins_array = []
  File.open("p42/#{file_name}") do |file|
    file.each_line do |line|
      @coins_array << line.chomp.to_i
    end
  end
end

def coins
  [
    [1, @coins_array[0]],
    [5, @coins_array[1]],
    [10, @coins_array[2]],
    [50, @coins_array[3]],
    [100, @coins_array[4]],
    [500, @coins_array[5]]
  ]
end

def count(file_name)
  read_file(file_name)
  price = @coins_array[6]

  result = []
  coins.reverse.each do |coin|
    use_count = (price / coin[0] >= coin[1]) ? coin[1] : price / coin[0]
    price -= use_count * coin[0]
    result << "#{coin[0]}円#{use_count}枚"
  end

  p "#{@coins_array[6]}円: " + result.join(', ')
end

count('p42.in')
count('p42_1.in')
