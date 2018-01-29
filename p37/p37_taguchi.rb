array = []
File.open('./p37_4.in') { |file| file.each_line { |x| array << x.chomp } }
n, m, maze = array[0].to_i, array[1].to_i, array[2..-1]
start, goal = {}, {}
# Get start/goal Coord
maze.each_with_index { |m, i|  [['S', start], ['G', goal]].each { |h| h[1][:x], h[1][:y] = i, m.index(h[0]) if m.include?(h[0]) } }
INF = 10000
d = Array.new(n).map { Array.new(m, INF) } 
d[start[:x]][start[:y]] = 0
q = []
q.push [start[:x], start[:y]]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
while q.any? do
  current = q.pop
  break if current[0] == goal[:x] && current[1] == goal[:y]
  for i in 0..3
    nx, ny = current[0] + dx[i], current[1] + dy[i]
    if 0 <= nx && nx < n && 0 <= ny && ny < m && maze[nx][ny] != '#' && d[nx][ny] == INF 
      q.push [nx, ny]
      d[nx][ny] = d[current[0]][current[1]] + 1
    end
  end
end
p d[goal[:x]][goal[:y]]
