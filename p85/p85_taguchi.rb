n, k, info = 0, 0, []
File.open(ARGV[0]) { |file| file.each_with_index do |line, i|
  case i
  when 0
    n = line.chomp.to_i
  when 1
    k = line.chomp.to_i
  else
    arry = line.chomp.split(',')
    hash = {}
    hash[:type] = arry[0].to_i
    hash[:x]    = arry[1].to_i
    hash[:y]    = arry[2].to_i
    info << hash
  end
end }

class UnionFind
  def initialize(n)
    @par, @rank = [], []
    for i in 0..(n - 1)
      @par[i] = i
      @rank[i] = 0
    end
  end

  def find(x) 
    if @par[x] == x
      x
    else
      @par[x] = find(@par[x])
    end
  end

  def same?(x, y)
    find(x) == find(y)
  end

  def unite(x, y)
    x, y = find(x), find(y)
    return if x == y

    if @rank[x] < @rank[y]
      @par[x] = y
    else
      @par[y] = x
      if @rank[x] == @rank[y]
        @rank[x] += 1
      end
    end
  end
end

uf = UnionFind.new(n * 3)
ans = 0
for i in 0..(k - 1)
  x, y, type = info[i][:x], info[i][:y], info[i][:type]
  if x < 0 || n <= x || y < 0 || n <= y
    ans += 1
    next
  end

  if type == 1
    if uf.same?(x, y + n) || uf.same?(x, y + 2 * n)
      ans += 1
    else
      uf.unite(x, y)
      uf.unite(x + n, y + n)
      uf.unite(x + 2 * n, y + 2 * n)
    end
  else
    if uf.same?(x, y) || uf.same?(x, y + 2 * n)
      ans += 1
    else
      uf.unite(x, y + n)
      uf.unite(x + n, y + 2 * n)
      uf.unite(x + 2 * n, y)
    end
  end
end
p ans
