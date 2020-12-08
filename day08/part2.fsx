open System.IO

type Op = string * int

let parseInstructions (lines: seq<string>) =
    lines
    |> Seq.map(fun line -> line.Split " ")
    |> Seq.map(fun op -> (op.[0], int op.[1]))
    |> Seq.toArray

let rec interpret acc row visited switched (ops: array<Op>) =
    if row >= Array.length ops then
        Some acc
    elif Set.contains row visited then
        None
    else
        match ops.[row] with
        | "acc", n ->
            interpret (acc + n) (row + 1) (Set.add row visited) switched ops
        | "jmp", n when switched ->
            interpret acc (row + n) (Set.add row visited) switched ops
        | "nop", n when switched ->
            interpret acc (row + 1) (Set.add row visited) switched ops
        | "jmp", n ->
            interpret acc (row + n) (Set.add row visited) switched ops
            |> Option.orElse
                   (interpret acc (row + 1) (Set.add row visited) true ops)
        | "nop", n ->
            interpret acc (row + 1) (Set.add row visited) switched ops
            |> Option.orElse
                   (interpret acc (row + n) (Set.add row visited) true ops)
        | illegalOp -> failwith $"illegal op {invalidOp}"

let compute lines =
    lines
    |> parseInstructions
    |> interpret 0 0 Set.empty false

let main =
    let inputPath = Path.Combine(__SOURCE_DIRECTORY__, "input.txt")
    inputPath
    |> File.ReadLines
    |> compute
    |> Option.get
    |> printfn "%A"

main
