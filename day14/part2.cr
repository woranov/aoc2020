def compute(lines)
  mem = {} of UInt64 => UInt64
  mask_passthrough : UInt64 = 0
  mask_overwrites = [] of UInt64

  lines.each { |line|
    var, val = line.split(" = ")
    case var
    when "mask"
      mask_passthrough = val.gsub('X', '1').to_u64(2)
      mask_overwrites = ['0', '1']
        .repeated_permutations(val.count('X'))
        .map { |perm|
          bits = perm.each
          val.gsub('0', '1').gsub(/X/) { |_| bits.next }
        }
        .map(&.to_u64(2))
        .to_a
    when .starts_with?("mem")
      _, addr, _ = var.split(/[\[\]]/)

      addr = addr.to_u64 | mask_passthrough
      val = val.to_u64

      mask_overwrites.each { |mask_overwrite|
        mem[addr & mask_overwrite] = val
      }
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
