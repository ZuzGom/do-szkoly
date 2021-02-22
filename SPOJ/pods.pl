$b =<>;
$wynik = 0;
 
my @a = (1..$b);
for(@a){
    $line =<>;
	@spl = split(' ', $line);
	$wynik += (@spl[2]*1.0)/$b;
}

print $wynik;
