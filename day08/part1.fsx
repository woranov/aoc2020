open System.IO

type Op = string * int

let parseInstructions (lines: seq<string>) =
    lines
    |> Seq.map (fun line -> line.Split " ")
    |> Seq.map (fun op -> (op.[0], int op.[1]))
    |> Seq.toArray

let rec interpret acc row visited (ops: array<Op>) =
    if Set.contains row visited then
        acc
    else
        match ops.[row] with
        | "acc", n -> interpret (acc + n) (row + 1) (Set.add row visited) ops
        | "jmp", n -> interpret acc (row + n) (Set.add row visited) ops
        | "nop", _ -> interpret acc (row + 1) (Set.add row visited) ops
        | illegalOp -> failwith $"illegal op {illegalOp}"

let compute lines =
    lines
    |> parseInstructions
    |> interpret 0 0 Set.empty

let main =
    let inputPath = Path.Combine(__SOURCE_DIRECTORY__, "input.txt")

    inputPath
    |> File.ReadLines
    |> compute
    |> printfn "%A"

main
