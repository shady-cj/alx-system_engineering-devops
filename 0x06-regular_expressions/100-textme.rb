#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(\+?\d+|\w+)?\]\s*\[to:(\+?\d+|\w+)?\]\s*\[flags:((?:-?\d\:?){5})?\]/).join(",")
