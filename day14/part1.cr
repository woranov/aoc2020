def compute(lines)
  mem = {} of UInt64 => UInt64
  mask_passthrough : UInt64 = 0
  mask_overwrite : UInt64 = 0

  lines.each { |line|
    var, val = line.split(" = ")
    case var
    when "mask"
      mask_passthrough = val.gsub('X', '0').to_u64(2)
      mask_overwrite = val.gsub('X', '1').to_u64(2)
    when .starts_with?("mem")
      _, addr, _ = var.split(/[\[\]]/)
      mem[addr.to_u64] = (val.to_u64 | mask_passthrough) & mask_overwrite
    else
      raise "invalid target #{var}"
    end
  }

  mem.values.sum
end

def main
  puts compute(File.read_lines("#{__DIR__}/input.txt"))
end

main()
