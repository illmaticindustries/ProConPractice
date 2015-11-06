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

jobs = []

# スタートが[0]の場合
start_times = @start_times
end_times = @end_times
jobs << 1

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
