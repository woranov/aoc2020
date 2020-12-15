# Advent of Code 2020

## Python

```console
python -m dayXX.part1
python -m dayXX.part2
```

### Test case
```console
pytest dayXX
```

## Elixir
```console
elixir ./dayXX/part1.exs
elixir ./dayXX/part2.exs
```

## Powershell
```console
pwsh ./dayXX/part1.ps1
pwsh ./dayXX/part2.ps1
```

## Java
```console
javac --enable-preview --release 15 -cp ./dayXX/ ./dayXX/*.java
java --enable-preview -cp ./dayXX/ part1
java --enable-preview -cp ./dayXX/ part2
rm ./dayXX/*.class
```

## Nim
```console
nim c --hints:off -o:./dayXX/ -r ./dayXX/part1.nim
nim c --hints:off -o:./dayXX/ -r ./dayXX/part2.nim
rm ./dayXX/*.exe
```

## Haskell
```console
ghc -v0 ./dayXX/part1.hs && ./dayXX/part1
ghc -v0 ./dayXX/part2.hs && ./dayXX/part2
rm ./dayXX/* -Include *.exe,*.hi,*.o
```

## TypeScript
```console
tsc
node ./dayXX/part1.js
node ./dayXX/part2.js
```

## Kotlin
```console
kotlinc -cp ./dayXX/ -script ./dayXX/part1.kts 2>$null
kotlinc -cp ./dayXX/ -script ./dayXX/part2.kts 2>$null
```
(`2>$null` hides `stderr` in powershell)

## F#
```console
dotnet fsi ./dayXX/part1.fsx
dotnet fsi ./dayXX/part2.fsx
```

## Rust
```console
cargo run -q -p dayXX --bin part1
cargo run -q -p dayXX --bin part2
```

## Crystal
```console
crystal dayXX/part1.cr
crystal dayXX/part2.cr
```
