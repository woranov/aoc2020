import os
import sequtils
import strutils
import sugar


proc compute(data: seq[string]): int =
  let
    width = len data[0]
    height = len data

  (0..<height)
    .toSeq()
    .filter(i => data[i][i * 3 mod width] == '#')
    .len()


proc main() =
  let data = readFile(os.joinPath(os.getAppDir(), "input.txt"))
  echo compute(data.strip().splitLines(false))


if isMainModule:
  main()
