use std::fs;

const SIZE: usize = 25;

fn compute(lines: Vec<&str>) -> i64 {
    let mut running_sum = Vec::new();
    let mut last_sum = 0;

    let numbers = lines
        .into_iter()
        .map(|s| s.parse().unwrap())
        .collect::<Vec<i64>>();

    let number = numbers
        .windows(SIZE + 1)
        .enumerate()
        .find_map(|(idx, window)| {
            let num = window[SIZE];

            if idx == SIZE + 1 {
                for n in &numbers[..=SIZE] {
                    last_sum += n;
                    running_sum.push(last_sum);
                }
            }

            last_sum += num;
            running_sum.push(last_sum);

            for i in 0..SIZE - 1 {
                for j in i + 1..SIZE {
                    if window[i] + window[j] == num {
                        return None;
                    }
                }
            }
            Some(num)
        })
        .expect("number not found");

    return running_sum
        .iter()
        .enumerate()
        .find_map(|(end_idx, cum_sum)| {
            if let Ok(start_idx) = running_sum.binary_search(&(cum_sum - number)) {
                let nums = &numbers[start_idx + 1..end_idx];
                return Some(nums.iter().min().unwrap() + nums.iter().max().unwrap());
            }
            None
        })
        .expect("no span found");
}

fn main() -> std::io::Result<()> {
    let path = fs::canonicalize(file!())?.with_file_name("input.txt");
    let file_content = fs::read_to_string(path)?;
    let lines: Vec<&str> = file_content.split_whitespace().collect();

    println!("{}", compute(lines));

    Ok(())
}
