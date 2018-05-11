n, graph = 0, [[]]
File.open(ARGV[0]) { |file| file.each_with_index do |line, i|
  case i
  when 0
    n = line.chomp.to_i
  when 1 
  else
    a = []
    graph << line.chomp.split(',').map do |a|
      a = a.split(':')
      hash = {}
      hash[:to] = a[0].to_i
      hash[:cost] = a[1].to_i
      hash
    end
  end
end }
INF = 1_000_000
best_distance = Array.new(n + 1, INF) 
second_distance = Array.new(n + 1, INF)
queue = []
queue.push({ distance: 0, vertex: 1 })
while !queue.empty?
  pop_queue = queue.pop
  distance = pop_queue[:distance]
  vertex = pop_queue[:vertex]
  # Don't need to check 
  next if second_distance[vertex] < distance
  for i in 0..(graph[vertex].size - 1)
    # Next target  
    edge = graph[vertex][i]
    # Distance to next 
    next_distance = distance + edge[:cost]
    # Update best distance 
    if next_distance < best_distance[edge[:to]]
      best_distance[edge[:to]] = next_distance
      next_distance = best_distance[edge[:to]]
      # Push next vertex and sum of distance to queue 
      queue.push({ distance: best_distance[edge[:to]], vertex: edge[:to] })
    end
    # Update second distance
    if best_distance[edge[:to]] < next_distance &&
       next_distance < second_distance[edge[:to]]
      second_distance[edge[:to]] = next_distance
      # Push next vertex and sum of distance to queue
      queue.push({ distance: second_distance[edge[:to]], vertex: edge[:to] })
    end
  end
end
puts second_distance[n]

