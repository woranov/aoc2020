import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Stream;


public class part2 {

  static record Entry(int lo, int hi, char chr, String password) {

    boolean check() {
      return (
          this.password.charAt(this.lo - 1) == this.chr
      ) ^ (
          this.password.charAt(this.hi - 1) == this.chr
      );
    }
  }

  private static final Pattern LINE_PATTERN = Pattern.compile(
      "(?<lo>\\d+)-(?<hi>\\d+) (?<chr>\\w): (?<pass>\\w+)"
  );

  long compute(Stream<String> lines) {
    //noinspection ResultOfMethodCallIgnored
    return lines
        .map(LINE_PATTERN::matcher)
        .peek(Matcher::find)
        .map(m -> new Entry(
            Integer.parseInt(m.group("lo")),
            Integer.parseInt(m.group("hi")),
            m.group("chr").charAt(0),
            m.group("pass"))
        ).filter(Entry::check)
        .count();
  }

  public static void main(String[] args) throws FileNotFoundException {
    var p2 = new part2();
    var reader = new BufferedReader(
        new FileReader(p2.getClass().getResource("./input.txt").getPath())
    );

    System.out.println(p2.compute(reader.lines()));
  }
}
