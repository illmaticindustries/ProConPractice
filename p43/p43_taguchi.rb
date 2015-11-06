def read_file(file_name)
  array = []
  File.open("p43/#{file_name}") do |file|
    file.each_line do |line|
      array << line.chomp.to_i
    end
  end

  @num = array[0]
  @start_times = array[1..5]
  @end_times = array[6..10]
end

read_file('p43.in')
# read_file('p43_1.in')
# read_file('p43_2.in')

jobs = []

# スタートの位置を終了が一番速い箇所に設定する
first_end_time_index = @end_times.find_index(@end_times.min)
start_times = @start_times[first_end_time_index..-1]
end_times = @end_times.last(start_times.size)
jobs << @num - start_times.size + 1

loop do
  p 'start_times'
  p start_times = start_times.select { |time| time > end_times.first }
  p 'jobs'
  p jobs << @num - start_times.size + 1
  p 'end_times'
  p end_times = end_times.last(start_times.size)
  p '---'
  break if end_times.empty? || start_times.select { |time| time > end_times.first }.empty?
end

p "jobs: #{jobs}"
