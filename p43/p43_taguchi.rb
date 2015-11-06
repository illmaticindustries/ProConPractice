def read_file(file_name)
  array = []
  File.open("p43/#{file_name}") do |file|
    file.each_line do |line|
      array << line.chomp.to_i
    end
  end

  @num = array.first
  # 'start_times'
  start_times = array[1..@num.to_i]
  # 'end_times'
  end_times = array[(@num.to_i + 1)..-1]
  times = []
  (0..(@num.to_i - 1)).each do |num|
    times[num] = [start_times[num], end_times[num]]
  end

  # end_timesでソートする
  times = times.sort { |a, b| a[1] <=> b[1] }

  # 戻す
  @start_times = []
  @end_times = []

  times.each do |time|
    @start_times << time[0]
    @end_times  << time[1]
  end
end

# read_file('p43_1.in')
# read_file('p43_2.in')

def jobs(file)
  read_file(file)
  jobs = []

  # 終了時間が早い順にソートする
  end_times = @end_times.sort

  # スタートの位置を終了が一番速い箇所に設定する
  first_end_time_index = @end_times.find_index(@end_times.min)
  start_times = @start_times[first_end_time_index..-1]
  end_times = @end_times.last(start_times.size)
  # 'first jobs'
  jobs << @num - start_times.size + 1

  loop do
    # スタートの配列を終了時間に合わせる
    start_times = start_times.select { |time| time > end_times.first }
    end_times = end_times.last(start_times.size)

    # スタートの位置を終了が一番速い箇所に設定する
    # 'end_times_index'
    end_times_index = end_times.find_index(end_times.min)
    # 'start_times'
    start_times = start_times[end_times_index..-1]
    # 'jobs'
    jobs << @num - start_times.size + 1
    # 'end_times'
    end_times = end_times.last(start_times.size)
    # '---'
    break if end_times.empty? || start_times.select { |time| time > end_times.first }.empty?
  end

  p "Answer: #{jobs.size}"
end

jobs('p43.in')
jobs('p43_1.in')
jobs('p43_2.in')
jobs('p43_3.in')
