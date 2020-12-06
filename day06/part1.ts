import * as path from "path";
import { readFileSync } from "fs";

function compute(groups: String[]): number {
  return groups
    .map((group) => new Set(group.replace(/\n/g, "")).size)
    .reduce((a, b) => a + b);
}

function main() {
  const inputPath = path.resolve(__dirname, "input.txt");
  const input = readFileSync(inputPath, "utf-8");
  console.log(compute(input.split("\n\n")));
}

main();
