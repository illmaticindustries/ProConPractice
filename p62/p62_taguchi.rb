n, a, m, k = 0, [], [], 0
File.open(ARGV[0]) { |file| file.each_with_index do |line, i|
  case i
  when 0
    n = line.chomp.to_i
  when 1
    a = line.chomp.split(',').map(&:to_i)
  when 2
    m = line.chomp.split(',').map(&:to_i)
  else
    k = line.chomp.to_i
  end
end }
MAX_K = 100_000 
dp = Array.new(MAX_K + 1, -1)
dp[0] = 0
for i in 0..(n - 1)
  for j in 0..k
    if 0 <= dp[j]
      dp[j] = m[i]
    elsif j < a[i] || dp[j - a[i]] <= 0
      dp[j] = -1
    else
      dp[j] = dp[j - a[i]] - 1
    end
  end
end
p (0 <= dp[k])
