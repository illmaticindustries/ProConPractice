n, m, lm = 0, 0, 0
File.open(ARGV[0]) { |file| file.each_with_index do |line, i|
  case i
  when 0
    n = line.chomp.to_i
  when 1
    m = line.chomp.to_i
  else
    lm = line.chomp.to_i
  end
end }
MAX_M, MAX_N = 1_000, 1_000
dp = Array.new(MAX_M).map { Array.new(MAX_N) }
dp[0].fill 0
dp[0][0] = 1
for i in 1..m
  for j in 0..n
    if i <= j
      dp[i][j] = (dp[i - 1][j] + dp[i][j - i]) % lm
    else
      dp[i][j] = dp[i - 1][j]
    end
  end
end
p dp[m][n]
