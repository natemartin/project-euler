#!/usr/bin/ruby
def bouncy?(number)
  num_arr = number.to_s.split(//)
  return !((num_arr == num_arr.sort) || (num_arr == num_arr.sort.reverse))
end

i = 1
bounce_count = 0

loop do
  bounce_count = bounce_count + 1 if bouncy?(i)
  if bounce_count.to_f / i.to_f == 0.99
    puts i
    exit
  end
  i = i + 1
end
