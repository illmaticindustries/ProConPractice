n, a = 0, []
File.open(ARGV[0]) { |file| file.each_with_index do |line, i|
  case i
  when 0
    n = line.chomp.to_i
  else
    a = line.chomp.split(',').map(&:to_i)
  end
end }
MAX_N = 1_000
dp = Array.new(MAX_N)
res = 0
for i in 0..(n - 1)
  dp[i] = 1
  for j in 0..(i - 1)
    if a[j] < a[i] 
      dp[i] = [
        dp[i], 
        dp[j] + 1
      ].max
    end
  end
  res = [
    res,
    dp[i]
  ].max
end
p res
