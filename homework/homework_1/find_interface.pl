#!/usr/bin/perl

if (@ARGV<1) {
    print STDERR "USAGE: $0 pdb\n\n";
    print STDERR "Find the residues at the interface\n";
    print STDERR "defined as atoms within 4A\n";
    exit;
}

$pdbfile = shift @ARGV;

open (PDB, $pdbfile);


# first partner atoms
while (<PDB>) {
    last if (/^TER/);
    next if (! /^ATOM/);
    push(@p1,$_);
    $x = substr ($_, 30, 8);
    $y = substr ($_, 38, 8);
    $z = substr ($_, 46, 8);
    push(@p1x,$x);
    push(@p1y,$y);
    push(@p1z,$z);
}
#print STDERR "partner 1 $#p1x atoms\n";


# second partner atoms
while (<PDB>) {
    last if (/^TER/);
    next if (! /^ATOM/);
    push(@p2,$_);
    $x = substr ($_, 30, 8);
    $y = substr ($_, 38, 8);
    $z = substr ($_, 46, 8);
    push(@p2x,$x);
    push(@p2y,$y);
    push(@p2z,$z);
}
#print STDERR "partner 2 $#p2x atoms\n";

# look for close atoms
for ($i=0; $i<$#p1x; $i++) {
#    print $i;
    for ($j=0; $j<$#p2x; $j++) {
	if ((( $p1x[$i] - $p2x[$j] )**2 +
	     ( $p1y[$i] - $p2y[$j] )**2 +
	     ( $p1z[$i] - $p2z[$j] )**2) < 16.0) {
	    $p1res = substr($p1[$i],21,6) . substr($p1[$i],5,15);
	    $p1int{$p1res}++;
	    $p2res = substr($p2[$j],21,6) . substr($p2[$j],5,15);
	    $p2int{$p2res}++;
	    print "$p1res $p2res\n";
	}
    }
}
       
@keys = keys %p1int; 
@skeys = sort { substr($a,0,1) <=> substr($b,0,1) | 
                substr($a,1,4) <=> substr($b,1,4) } @keys;
print "Partner 1:\n";
foreach $k (@skeys) { print "$k\n"; }

@keys = keys %p2int; 
@skeys = sort { substr($a,0,1) <=> substr($b,0,1) | 
                substr($a,1,4) <=> substr($b,1,4) } @keys;
print "Partner 2:\n";
foreach $k (@skeys) { print "$k\n"; }

#  # print the hash
#  while ( ($k,$n) = each %p1int ) { print "$k ==> $n\n"; }
#  while ( ($k,$n) = each %p2int ) { print "$k ==> $n\n"; }
