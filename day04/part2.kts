import java.io.File
import java.lang.AssertionError

class Part2 {
    private val requiredKeys = setOf("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    private val validEyeColors = setOf("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

    private fun checkFields(fields: Map<String, String>): Boolean {
        return requiredKeys.all { key ->
            fields.containsKey(key) && when (key) {
                "byr" -> Integer.parseInt(fields[key]) in 1920..2002
                "iyr" -> Integer.parseInt(fields[key]) in 2010..2020
                "eyr" -> Integer.parseInt(fields[key]) in 2020..2030
                "hgt" -> fields[key]!!.let { hairColor ->
                    val unit = hairColor.takeLast(2)
                    val value = hairColor.dropLast(2)
                    when (unit) {
                        "cm" -> Integer.parseInt(value) in 150..193
                        "in" -> Integer.parseInt(value) in 59..76
                        else -> false
                    }
                }
                "hcl" -> fields[key]!!.let { eyeColor ->
                    eyeColor[0] == '#'
                        && eyeColor.length == 7
                        && eyeColor.substring(1).all { digit ->
                        digit in "0123456789abcdef"
                    }
                }
                "ecl" -> fields[key] in validEyeColors
                "pid" -> fields[key]!!.length == 9
                else -> throw AssertionError()
            }
        }
    }

    fun compute(passports: List<String>): Int =
        passports
            .map { passport ->
                passport.trim()
                    .split("\n")
                    .map { it.split(" ") }.flatten()
                    .map {
                        it.split(":").let { kv -> Pair(kv[0], kv[1]) }
                    }.toMap()
            }.filter(::checkFields)
            .count()
}

fun main() {
    val part2 = Part2()
    val input = File(
        part2.javaClass.classLoader.getResource("input.txt")!!.path
    ).readText().split("\n\n")

    println(part2.compute(input))
}

main()
