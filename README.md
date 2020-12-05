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
