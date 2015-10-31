class ShortestPathMaze
  def initialize
    @field = []
    @start = {}
    @goal = {}
    line_num = 0

    File.open('p37.in') do |file|
      file.each_line do |line|
        if line.include?('S')
          @start[:x] = line_num
          @start[:y] = line.index('S')
        end

        @field << line.chomp.split('')
        line_num += 1
      end
    end

    @height = @field.size
    @width = @field.first.size
    @count = 0
    @queue = []
    @next_field_queue = []
  end

  # 現在地を更新する
  def current_field(y, x)
    p "current_field: (#{x}, #{y})"
    # p "@next_field_queue -= [[x, y]]"
    @next_field_queue -= [[x, y]]

    # p @queue << [x, y]

    @field[y][x] = '#'
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    direction.each do |dy, dx|
      # p "dx: #{dx}, dy: #{dy}"
      nx = x + dx
      ny = y + dy

      # p "nx: #{nx}, ny: #{ny}"
      next if nx >= @height || ny >= @width
      # p "next_field: #{@field[ny][nx]}"

      if 0 <= nx && nx < @height && 0 <= ny && ny < @width && @field[ny][nx] == '.'
        # @count += 1
        p "add #{[nx, ny]}"
        @next_field_queue << [nx, ny]
        # p "@next_field_queue: #{@next_field_queue}"
      end

      if 0 <= nx && nx < @height && 0 <= ny && @field[ny][nx] == 'G'
        # p "nx: #{nx}, ny:#{ny}"
        # @count += 1
        p "Goal! #{@queue.size}"
      end
    end

    next_field_queue
  end

  def solve
    current_field(@start[:x], @start[:y])
  end

  def next_field_queue
    p "next_field_queue: #{@next_field_queue}"

    @next_field_queue.each do |nx, ny|
      current_field(ny, nx)
    end

  end
end

shortest_path_maze = ShortestPathMaze.new
shortest_path_maze.solve
