defmodule Day01.Part2 do
  def find_pair(nums, total) do
    nums
    |> Enum.map(&[&1, total - &1])
    |> Enum.find(fn [_, b] -> b in nums end)
  end

  def compute(data) do
    nums =
      data
      |> String.trim()
      |> String.split()
      |> Enum.map(&String.to_integer/1)

    nums
    |> Enum.map(fn a -> [a | find_pair(nums, 2020 - a)] end)
    |> Enum.find(fn [_ | b] -> b != nil end)
    |> Enum.reduce(&(&1 * &2))
  end

  def main do
    File.read!(Path.join(__DIR__, "input.txt"))
    |> compute
    |> IO.inspect()
  end
end

Day01.Part2.main()
