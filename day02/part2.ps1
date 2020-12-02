Get-Content "$PSScriptRoot/input.txt"
| ForEach-Object {
    $_ -match "(\d+)-(\d+) (\w): (\w+)" | Out-Null
    [int]$idx1, [int]$idx2, $char, $pass = $Matches[1..4]

    if ($pass[$idx1 - 1] -eq $char -xor $pass[$idx2 - 1] -eq $char) {
        $true
    }
}
| Measure-Object -Sum
| Select-Object -ExpandProperty Sum
