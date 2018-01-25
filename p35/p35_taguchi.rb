array = []
File.open('./p35_case3.in') { |file| file.each_line { |x| array << x.chomp } }
@yard = array[2..-1].map { |g| g.split('') }

def dfs(x, y)
  @yard[x][y] = '.'
  for dx in -1..1
    for dy in -1..1
      nx = x + dx
      ny = y + dy
      dfs(nx, ny) if 0 <= nx && nx < @yard.length && 0 <= ny && ny < @yard.first.length && @yard[nx][ny] == 'W'
    end
  end
end

@count = 0
for x in 0..(@yard.length - 1) do
  for y in 0..(@yard.first.length - 1) do
    if @yard[x][y] == 'W'
      dfs(x, y)
      @count += 1
    end
  end
end

p @count
