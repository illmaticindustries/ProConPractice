def read_file(file_name)
  array = []
  File.open("p52/#{file_name}") do |file|
    file.each_line do |line|
      array << line.chomp
    end
  end
  p '@element_count='
  p @element_count = array[0].to_i
  p 'max_weight='
  p @max_weight = array[1].to_i
  p 'array='
  @array = []
  p @array = array[2..-1].map { |pair| pair.split(',').map { |a| a.to_i } }
end

# 現在の価値
# @param 現在の要素の番号, 重さの許容量
def value(n, max_weight_now)

  @value ||= []
  @value[n] ||= []
  # メモに存在する場合はメモの内容を返す
  return @value[n][max_weight_now] unless @value[n].nil? || @value[n][max_weight_now].nil?

  # 現在のnが要素数を超える場合は終わり
  if n == @element_count
    value = 0
  else
    # p "#{n}番目"
    # p "重さ:"
    # p n_weight = @array[n][0]
    # p '価値:'
    # p n_value = @array[n][1]

    # 現在の要素の重さが重さの許容量を超える場合は、自分自身は入れないで次の要素に行く
    if n_weight > max_weight_now
      value = value(n + 1, max_weight_now)

    # 自分自身を入れる場合と入れない場合の最大値を比較する
    else
      value = [
        # 自分自身を入れない場合
        value(n + 1, max_weight_now),
        # 自分自身を入れる場合
        value(n + 1, max_weight_now - n_weight) + n_value
      ].max
    end
  end

  # メモに値を代入する
  return @value[n][max_weight_now] = value
end

# 実行メソッド
def execute(file_name)
  read_file(file_name)
  # 価値を求める
  # 0番目の要素の場合、重さの許容量は@max_weightになる
  p '合計値: ' + value(0, @max_weight).to_s
end

# execute('p52.in')
execute('p52_1.in')
# execute('p52_2.in')
# execute('p52_3.in')
