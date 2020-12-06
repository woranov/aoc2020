import java.io.File

class Part1 {
    private val requiredKeys = setOf("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

    fun compute(passports: List<String>): Int =
        passports.map { passport ->
            passport.trim()
                .split("\n")
                .map { it.split(" ") }.flatten()
                .map {
                    it.split(":").let { kv -> Pair(kv[0], kv[1]) }
                }.toMap()
        }.filter {
            it.keys.containsAll(requiredKeys)
        }.count()
}

fun main() {
    val part1 = Part1()
    val input = File(
        part1.javaClass.classLoader.getResource("input.txt")!!.path
    ).readText().split("\n\n")

    println(part1.compute(input))
}

main()
