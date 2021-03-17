print "Podaj liczbę (ale dobrą): ";
$liczba = <>;

print "Podaj liczbę bitów (ale dobrą): ";
$b =<>;
while (2**($b/2 - 1)<=$liczba or $b%2 == 1){
    print "Podaj liczbę bitów (ale dobrą): ";
    $b =<>;
}
$wynik = 0;

my @wg = (1..$b);

$p = $b/2 - 1;

for $i (1..$b){
    $wg[$i-1] = 2**$p;
    $p -= 1;
}
#print "@wg\n";

$wynik = "";
$suma = 0;

for $x (@wg){
    if ($suma + $x <= $liczba){
        $suma += $x;
        $wynik = $wynik."1";
    }
    else{
        $wynik = $wynik."0"; 
    }
    
}
print $wynik;
