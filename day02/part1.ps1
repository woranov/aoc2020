Get-Content "$PSScriptRoot/input.txt"
| ForEach-Object {
    $_ -match "(\d+)-(\d+) (\w): (\w+)" | Out-Null
    [int]$lo, [int]$hi, $char, $pass = $Matches[1..4]

    $occurrences = ($pass | Select-String $char -AllMatches).Matches.Count
    if ($occurrences -ge $lo -and $occurrences -le $hi) {
        $true
    }
}
| Measure-Object -Sum
| Select-Object -ExpandProperty Sum
