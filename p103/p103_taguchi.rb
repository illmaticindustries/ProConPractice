n, m, r, graph = 0, 0, 0, []
File.open(ARGV[0]) { |file| file.each_with_index do |line, i|
  case i
  when 0
    n = line.chomp.to_i
  when 1
    m = line.chomp.to_i
  when 2
    r = line.chomp.to_i
  else
    a = line.chomp.split(',')
    hash = {}
    hash[:x] = a[0].to_i
    hash[:y] = a[1].to_i
    hash[:d] = a[2].to_i
    graph << hash
  end
end }

# Union-Find tree
@parent, @rank = [], []

for i in 0..(n + m - 1)
  @parent[i] = i
  @rank[i] = 0
end

def find(u)
  if @parent[u] == u
    u
  else
    @parent[u] = find @parent[u]
  end
end

def same(u, v)
  find(u) == find(v)
end

def unite(u, v)
  u = find u
  v = find v
  return nil if u == v
  if @rank[u] < @rank[v]
    @parent[u] = v
  else
    @parent[v] = u
    if @rank[u] == @rank[v]
      @rank[u] += 1
    end
  end
end

COST = 10_000
edge = []
for i in 0..(r - 1)
  edge << { u: graph[i][:x], v: graph[i][:y] + n, cost: -graph[i][:d] }
end

edge.sort_by! { |e| e[:cost] }
discount = 0
for i in 0..(edge.size - 1)
  if !same(edge[i][:u], edge[i][:v])
    unite(edge[i][:u], edge[i][:v])
    discount += edge[i][:cost]
  end
end
p COST * (n + m) + discount
