#!/usr/bin/ruby

@lookup_table = {}

def enumerate_num(current_prefix)
  if current_prefix.length >= 20
    return 1
  end
  total = 0
  if current_prefix.length == 0
    for i in 1..9
      total += enumerate_num(current_prefix + i.to_s)
    end
  elsif current_prefix.length == 1
    for i in 0..9
      if current_prefix[0].to_i + i < 10
        total += enumerate_num(current_prefix + i.to_s)
      end
    end
  else
    for i in 0..9
      if current_prefix[current_prefix.length-1].to_i + current_prefix[current_prefix.length-2].to_i + i < 10
        cache_lookup = @lookup_table[(current_prefix.length + 1).to_s + current_prefix[-1] + i.to_s]
        if !cache_lookup.nil?
          total = cache_lookup
        else
          total += enumerate_num(current_prefix + i.to_s)
          @lookup_table[(current_prefix.length + 1).to_s + current_prefix[-1] + i.to_s] = total
        end
      end
    end
  end
  return total
end

puts enumerate_num("")
