function get-firstanswer {
    param (
        $numbers
    )
    $answer = @()
    foreach ($number in $numbers) {
        if ($numbers -contains (2020 - $number)) {
            $answer += $number
        }
    }
    return [int]$answer[0] * [int]$answer[1]
}

function get-secondanswer {
    param (
        $numbers
    )
    foreach ($number1 in $numbers) {
        foreach ($number2 in $numbers) {
            foreach ($number3 in $numbers) {
                if ([int]$number1 + [int]$number2 + [int]$number3 -eq 2020) {
                    return [int]$number1 * [int]$number2 * [int]$number3
                }
            }
        }
    }
}

$numbers = Get-Content -Path ".\day1.txt"

get-firstanswer($numbers) | Write-Host 
get-secondanswer($numbers) | Write-Host