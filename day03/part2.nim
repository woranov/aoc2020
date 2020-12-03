import os
import sequtils
import strutils


proc compute(data: seq[string]): int =
  const slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

  let
    width = len data[0]
    height = len data
  var
    product = 1

  for dy, dx in slopes.items:
    proc check(y: int): bool =
      data[y][(y div dy) * dx mod width] == '#'

    product *= max(
      1,
      toSeq(countUp(0, height - 1, dy))
      .filter(check)
      .len()
    )

  product


proc main() =
  let data = readFile(os.joinPath(os.getAppDir(), "input.txt"))
  echo compute(data.strip().splitLines(false))


if isMainModule:
  main()
