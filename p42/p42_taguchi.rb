def read_file(file_name)
  @coins_array = []
  File.open("p42/#{file_name}") do |file|
    file.each_line do |line|
      @coins_array << line.chomp.to_i
    end
  end
end

def coins
  @coins = [
    [1, @coins_array[0]],
    [5, @coins_array[1]],
    [10, @coins_array[2]],
    [50, @coins_array[3]],
    [100, @coins_array[4]],
    [500, @coins_array[5]]
  ]
  @price = @coins_array[6]
end

def count(file_name)
  read_file(file_name)
  coins

  @result = []
  @coins.reverse.each do |coin|
    coin
    use_count = @price / coin[0]
    use_count = coin[1] if use_count >= coin[1]
    use_amount = use_count * coin[0]
    @price = @price - use_amount
    @result << "#{coin[0]}円#{use_count}枚"
  end
  @result
end

count('p42.in')
count('p42_1.in')
