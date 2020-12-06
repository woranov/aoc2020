import * as path from "path";
import { readFileSync } from "fs";

function compute(groups: String[]): number {
  return groups
    .map(
      (group) =>
        group
          .split("\n")
          .map((answers) => new Set(answers))
          .reduce(
            (answersLeft, answersRight) =>
              new Set([...answersLeft].filter((a) => answersRight.has(a)))
          ).size
    )
    .reduce((a, b) => a + b);
}

function main() {
  const inputPath = path.resolve(__dirname, "input.txt");
  const input = readFileSync(inputPath, "utf-8");
  console.log(compute(input.trim().split("\n\n")));
}

main();
