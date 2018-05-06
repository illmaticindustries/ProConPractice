n = 0
File.open(ARGV[0]) { |file| file.each_with_index do |line, i|
  n = line.chomp.to_i
end }
@colors = Array.new(n, 0)
def paint(vertex, color)
  @colors[vertex] = color
  next_vertex = @colors[vertex + 1] ? @colors[vertex + 1] : @colors[0]
  return false if @colors[vertex - 1] == color || next_vertex == color
  return false if next_vertex == 0 && !paint(vertex + 1, -color)
  return true
end
puts !paint(0, 1) ? 'No' : 'Yes'
