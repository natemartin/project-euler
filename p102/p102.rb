#!/usr/bin/ruby

def get_triangle_area(x1, y1, x2, y2, x3, y3)
  (( x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0).abs
end

triangle_data = []
count = 0
f = File.open("p102_triangles.txt", "r")
f.each_line do |line|
    triangle_data << line
end
f.close

triangle_data.each do |triangle|
  vals = triangle.split(',').map(&:to_i)
  sub_sum = get_triangle_area(0,0,vals[2],vals[3],vals[4],vals[5]) + get_triangle_area(vals[0],vals[1],0,0,vals[4],vals[5]) + get_triangle_area(vals[0],vals[1],vals[2],vals[3],0,0)
  area = get_triangle_area(vals[0],vals[1],vals[2],vals[3],vals[4],vals[5])
  count = count + 1 if (area - sub_sum).abs < 0.1
end

puts count

