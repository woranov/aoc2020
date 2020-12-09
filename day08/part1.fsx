open System.IO

type OpCode = Acc | Jmp | Nop
type Op = OpCode * int

let parseInstructions (lines: string seq) =
    lines
    |> Seq.map (fun line -> line.Split " ")
    |> Seq.map (fun op ->
        match op with
        | [| "acc"; n |] -> (Acc, int n)
        | [| "jmp"; n |] -> (Jmp, int n)
        | [| "nop"; n |] -> (Nop, int n)
        | illegalOp      -> failwith $"illegal op {invalidOp}"
    )
    |> Seq.toArray

let rec interpret acc row visited (ops: Op array) =
    if Set.contains row visited then
        acc
    else
        match ops.[row] with
        | Acc, n -> interpret (acc + n) (row + 1) (Set.add row visited) ops
        | Jmp, n -> interpret acc (row + n) (Set.add row visited) ops
        | Nop, _ -> interpret acc (row + 1) (Set.add row visited) ops

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
