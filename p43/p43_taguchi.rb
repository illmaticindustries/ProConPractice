def read_file(file_name)
  array = []
  File.open("p43/#{file_name}") do |file|
    file.each_line do |line|
      array << line.chomp.to_i
    end
  end

  @num = array.first
  @start_times = array[1..@num.to_i]
  @end_times = array[(@num.to_i + 1)..-1]
end

# read_file('p43_1.in')
# read_file('p43_2.in')

def jobs(file)
  read_file(file)
  jobs = []

  # スタートの位置を終了が一番速い箇所に設定する
  first_end_time_index = @end_times.find_index(@end_times.min)
  start_times = @start_times[first_end_time_index..-1]
  end_times = @end_times.last(start_times.size)
  p 'first jobs'
  p jobs << @num - start_times.size + 1

  loop do
    # スタートの配列を終了時間に合わせる
    p start_times = start_times.select { |time| time > end_times.first }
    p end_times = end_times.last(start_times.size)

    # スタートの位置を終了が一番速い箇所に設定する
    p 'end_times_index'
    p end_times_index = end_times.find_index(end_times.min)
    p 'start_times'
    p start_times = start_times[end_times_index..-1]
    p 'jobs'
    p jobs << @num - start_times.size + 1
    p 'end_times'
    p end_times = end_times.last(start_times.size)
    p '---'
    break if end_times.empty? || start_times.select { |time| time > end_times.first }.empty?
  end

  p "jobs: #{jobs}"
end

# jobs('p43.in')
# jobs('p43_1.in')
jobs('p43_2.in')
