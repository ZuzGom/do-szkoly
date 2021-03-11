print "Podaj liczbę (ale dobrą): ";
$liczba = <>;

print "Podaj liczbę bitów (ale dobrą): ";
$b =<>;
while (2**($b/2 - 1)<=$liczba){
    print "Podaj liczbę bitów (ale dobrą): ";
    $b =<>;
}
$wynik = 0;
my @a = (1..$b);


my @wg = (1..$b);
my @wg2 = (1..$b/2);

$p = $b/2 - 1;

for $i (1..$b){
    $wg[$i-1] = 2**$p;
    $p -= 1;
}
#print "@wg\n";

$zer = "0";
$jed ="1";

$wynik = "";
$suma = 0;

for $x (@wg){
    if ($suma + $x <= $liczba){
        $suma += $x;
        $wynik = $wynik.$jed;
    }
    else{
        $wynik = $wynik.$zer; 
    }
    
}
print $wynik;
