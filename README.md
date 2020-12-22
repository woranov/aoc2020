# Advent of Code 2020

## Python
*`all`*
```console
python -m dayXX.part1
python -m dayXX.part2
```

### Test case
```console
pytest dayXX
```

## Elixir
[`day01`](/day01) [`day05`](/day05)
```console
elixir ./dayXX/part1.exs
elixir ./dayXX/part2.exs
```

## Powershell
[`day02`](/day02)
```console
pwsh ./dayXX/part1.ps1
pwsh ./dayXX/part2.ps1
```

## Java
[`day02`](/day02)
```console
javac --enable-preview --release 15 -cp ./dayXX/ ./dayXX/*.java
java --enable-preview -cp ./dayXX/ part1
java --enable-preview -cp ./dayXX/ part2
rm ./dayXX/*.class
```

## Nim
[`day03`](/day03)
```console
nim c --hints:off -o:./dayXX/ -r ./dayXX/part1.nim
nim c --hints:off -o:./dayXX/ -r ./dayXX/part2.nim
rm ./dayXX/*.exe
```

## Haskell
[`day04`](/day04)
```console
ghc -v0 ./dayXX/part1.hs && ./dayXX/part1
ghc -v0 ./dayXX/part2.hs && ./dayXX/part2
rm ./dayXX/* -Include *.exe,*.hi,*.o
```

## Kotlin
[`day04`](/day04)
```console
kotlinc -cp ./dayXX/ -script ./dayXX/part1.kts 2>$null
kotlinc -cp ./dayXX/ -script ./dayXX/part2.kts 2>$null
```
(`2>$null` hides `stderr` in powershell)

## TypeScript
[`day06`](/day06)
```console
tsc
node ./dayXX/part1.js
node ./dayXX/part2.js
```

## F#
[`day08`](/day08)
```console
dotnet fsi ./dayXX/part1.fsx
dotnet fsi ./dayXX/part2.fsx
```

## Rust
[`day09`](/day09)
```console
cargo run -q -p dayXX --bin part1
cargo run -q -p dayXX --bin part2
```

## Crystal
[`day14`](/day14)
```console
crystal dayXX/part1.cr
crystal dayXX/part2.cr
```

## C
[`day17`](/day17)
```console
gcc ./dayXX/part1.c -o ./dayXX/part1 && ./dayXX/part1
gcc ./dayXX/part2.c -o ./dayXX/part2 && ./dayXX/part2
rm ./dayXX/*.exe
```
