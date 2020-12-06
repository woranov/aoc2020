defmodule Day05.Part2 do
  def compute(data) do
    data
    |> String.trim()
    |> String.split("\n")
    |> Enum.map(fn code ->
      code
      |> String.replace(["F", "B", "L", "R"], fn
        "F" -> "0"
        "B" -> "1"
        "L" -> "0"
        "R" -> "1"
      end)
      |> String.to_integer(2)
    end)
    |> Enum.sort()
    |> Enum.chunk_every(2, 1, :discard)
    |> Enum.find(fn [left_id, right_id] ->
      left_id == right_id - 2
    end)
    |> Enum.at(0)
    |> Kernel.+(1)
  end

  def main do
    File.read!(Path.join(__DIR__, "input.txt"))
    |> compute
    |> IO.inspect()
  end
end

Day05.Part2.main()
