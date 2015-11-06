def read_file(file_name)
  array = []
  File.open("p43/#{file_name}") do |file|
    file.each_line do |line|
      array << line.chomp.to_i
    end
  end

  @num = array[0]
  p @start_times = array[1..5]
  p @end_times = array[6..10]
end

read_file('p43.in')

jobs = []

# スタートが[0]の場合
first_start_time = @start_times.first
first_end_time = @end_times.first
jobs << 1

p next_start_times = @start_times.select { |time| time > first_end_time }
p jobs << @num - next_start_times.size + 1
p next_end_times = next_start_times.select { |time| time > next_start_times.first }

p next_start_times = next_start_times.select { |time| time > next_end_times.first }
p jobs << @num - next_start_times.size + 1
p next_end_times = next_start_times.select { |time| time > next_start_times.first }

p "jobs: #{jobs}"
