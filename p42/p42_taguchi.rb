def read_file
  @coins_array = []
  File.open('p42/p42.in') do |file|
    file.each_line do |line|
      @coins_array << line.chomp.to_i
    end
  end
end

def coins
  @coins = {}
  @coins[:c1] = @coins_array[0]
  @coins[:c5] = @coins_array[1]
  @coins[:c10] = @coins_array[2]
  @coins[:c50] = @coins_array[3]
  @coins[:c100] = @coins_array[4]
  @coins[:c500] = @coins_array[5]
  @coins[:all] = @coins_array[6]
  p @coins
end

def use
  p '500円'
  p use_c500_count = @coins[:all] / 500
  p use_c500_count = @coins[:c500] if use_c500_count >= @coins[:c500]
  p use_c500_amount = use_c500_count * 500
  p remain_500 = @coins[:all] - use_c500_amount

  p '100円'
  p use_c100_count = remain_500 / 100
  p use_c100_count = @coins[:c100] if use_c100_count >= @coins[:c100]
  p use_c100_amount = use_c100_count * 100
  p remain_100 = remain_500 - use_c100_amount

  p '50円'
  p use_c50_count = remain_100 / 50
  p use_c50_count = @coins[:c50] if use_c50_count >= @coins[:c50]
  p use_c50_amount = use_c50_count * 50
  p remain_50 = remain_100 - use_c50_amount

  p '10円'
  p use_c10_count = remain_50 / 10
  p use_c10_count = @coins[:c10] if use_c10_count >= @coins[:c10]
  p use_c10_amount = use_c10_count * 10
  p remain_10 = remain_50 - use_c10_amount

  p '5円'
  p use_c5_count = remain_10 / 5
  p use_c5_count = @coins[:c5] if use_c5_count >= @coins[:c5]
  p use_c5_amount = use_c5_count * 5
  p remain_5 = remain_10 - use_c5_amount

  p '1円'
  p use_c1_count = remain_5 / 1
  p use_c1_count = @coins[:c1] if use_c1_count >= @coins[:c1]
  p use_c1_amount = use_c1_count * 1
  p remain_1 = remain_5 - use_c1_amount
end

read_file
coins
use
