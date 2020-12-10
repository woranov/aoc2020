use std::fs;

fn compute(lines: Vec<&str>) -> u64 {
    let numbers = lines
        .into_iter()
        .map(|s| s.parse().unwrap())
        .collect::<Vec<u64>>();

    let size = 25;
    let found_window = numbers
        .windows(size + 1)
        .find(|window| {
            let num = window[size];

            for i in 0..size - 1 {
                for j in i..size {
                    if window[i] + window[j] == num {
                        return false;
                    }
                }
            }
            true
        })
        .expect("no solution found");

    return found_window[size];
}

fn main() -> std::io::Result<()> {
    let path = fs::canonicalize(file!())?.with_file_name("input.txt");
    let file_content = fs::read_to_string(path)?;
    let lines: Vec<&str> = file_content.split_whitespace().collect();

    println!("{}", compute(lines));

    Ok(())
}
