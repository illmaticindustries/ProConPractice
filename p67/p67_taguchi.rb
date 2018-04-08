n, m, a, lm = 0, 0, [], 0
File.open(ARGV[0]) { |file| file.each_with_index do |line, i|
  case i
  when 0
    n = line.chomp.to_i
  when 1
    m = line.chomp.to_i
  when 2
    a = line.chomp.split(',').map(&:to_i)
  else
    lm = line.chomp.to_i
  end
end }
MAX_N, MAX_M = 1_000, 1_000
dp = Array.new(MAX_N + 1).map { Array.new(MAX_M + 1) }
dp[0].fill 0
for i in 0..n
  dp[i][0] = 1
end
for i in 0..(n - 1)
  for j in 1..m
    if 0 <= j - 1 - a[i]
      dp[i + 1][j] = (dp[i + 1][j - 1] + dp[i][j] - dp[i][j - 1 - a[i]] + lm) % lm
    else
      dp[i + 1][j] = (dp[i + 1][j - 1] + dp[i][j]) % lm
    end
  end
end
p dp[n][m]
