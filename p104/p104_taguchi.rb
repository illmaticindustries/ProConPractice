@n, @ml, @md, @good, @bad = 0, 0, 0, [], []
File.open(ARGV[0]) { |file| file.each_with_index do |line, i|
  case i
  when 0
    @n = line.chomp.to_i
  when 1
    @ml = line.chomp.to_i
  when 2
    @md = line.chomp.to_i
  else
    a = line.chomp.split(/\),\(/)
    a = a.map do |e| 
      e = e.gsub(/(\(|\))/, '')
      e = e.split(',') 
      hash = {}
      hash[:a] = e[0].to_i
      hash[:b] = e[1].to_i
      hash[:d] = e[2].to_i
      hash
    end
    case i
    when 3
      @good = a
    when 4
      @bad = a 
    end
  end
end }
p @good
p @bad
INF = 1_000_000
def bellmanford
  @n.times do
    @updated = false
    # i + 1 => i, cost: 0
    for i in 0..@n
      if @distance[i + 1] < @distance[i]
        p "@distance[#{i + 1}] < @distance[#{i}]"
        @distance[i] = @distance[i + 1]
        @updated = true
        p "@distance: #{@distance}"
      end
    end
    # al => bl, cost: dl
    for i in 0..(@ml - 1)
      al = @good[i][:a]
      bl = @good[i][:b]
      dl = @good[i][:d]
      if @distance[al - 1] + dl < @distance[bl - 1]
        p "@distance[#{al - 1}] + #{dl} < @distance[#{bl - 1}]"
        @distance[bl - 1] = @distance[al - 1] + dl
        @updated = true
        p "@distance: #{@distance}"
      end
    end
    # bd => ad, cost: -dd
    for i in 0..(@md - 1)
      ad = @bad[i][:a]
      bd = @bad[i][:b]
      dd = @bad[i][:d]
      if @distance[bd - 1] - dd < @distance[ad - 1]
        p "@distance[#{bd - 1}] - #{dd} < @distance[#{ad - 1}]"
        @distance[ad - 1] = @distance[bd - 1] - dd
        @updated = true
        p "@distance: #{@distance}"
      end
    end
  end
end
@distance = Array.new(@n + 2)
@distance.fill 0
p "-----negative closed circuit-----"
bellmanford
if @updated
  p -1
  exit
end
p "-----distance-----"
@distance.fill INF
@distance[0] = 0
bellmanford
p @distance[0, @n]
ans = @distance[@n - 1]
if ans == INF
  ans = -2
end
p ans
