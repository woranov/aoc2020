defmodule Day01.Part1 do
  def compute(data) do
    nums =
      data
      |> String.trim()
      |> String.split()
      |> Enum.map(&String.to_integer/1)

    nums
    |> Enum.map(&[&1, 2020 - &1])
    |> Enum.find(fn [_, b] -> b in nums end)
    |> Enum.reduce(&(&1 * &2))
  end

  def main do
    File.read!("input.txt")
    |> compute
    |> IO.inspect()
  end
end

Day01.Part1.main()
