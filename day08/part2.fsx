open System.IO

type OpCode = Acc | Jmp | Nop
type Op = OpCode * int
type Program =
    {
        Ops: Op array
        Acc: int
        Row: int
        Visited: int Set
        Switched: bool
    }

    static member Empty = {
        Ops = Array.empty; Acc = 0; Row = 0; Visited = Set.empty; Switched = false
    }

    member this.CurrentOp =
        this.Ops.[this.Row]

    member this.Next =
        { this with Row = this.Row + 1; Visited = Set.add this.Row this.Visited }

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

let rec interpret (program: Program) =
    if program.Row >= Array.length program.Ops then
        Some program.Acc
    elif Set.contains program.Row program.Visited then
        None
    else
        match program.CurrentOp with
        | Acc, n ->
            interpret { program.Next with Acc = program.Acc + n }
        | Jmp, n when program.Switched ->
            interpret { program.Next with Row = program.Row + n }
        | Nop, _ when program.Switched ->
            interpret program.Next
        | Jmp, n ->
            interpret { program.Next with Row = program.Row + n }
            |> Option.orElse
                (interpret { program.Next with Switched = true })
        | Nop, n ->
            interpret program.Next
            |> Option.orElse
                (interpret { program.Next with Row = program.Row + n; Switched = true })

let compute lines =
    interpret { Program.Empty with Ops = parseInstructions lines }

let main =
    let inputPath = Path.Combine(__SOURCE_DIRECTORY__, "input.txt")
    inputPath
    |> File.ReadLines
    |> compute
    |> Option.get
    |> printfn "%A"

main
