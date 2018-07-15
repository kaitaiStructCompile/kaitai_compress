sub process_xor_one {
    my ($data, $key) = @_;

    $key = pack('C', $key);
    for (my $i = 0; $i < length($data); $i++) {
        substr($data, $i, 1) ^= $key;
    }
    return $data;
}

sub process_xor_many {
    my ($data, $key) = @_;
    my $ki = 0;
    my $kl = length($key);

    for (my $i = 0; $i < length($data); $i++) {
        substr($data, $i, 1) ^= substr($key, $ki, 1);
        $ki += 1;
        $ki = 0 if $ki >= $kl;
    }
    return $data;
}

sub process_rotate_left {
    my ($data, $amount, $group_size) = @_;

    die "Unable to rotate group of $group_size bytes yet" if $group_size != 1;

    my $mask = $group_size * 8 - 1;
    $amount &= $mask;
    my $anti_amount = -$amount & $mask;

    for (my $i = 0; $i < length($data); $i++) {
        my $byte = unpack('C', substr($data, $i, 1));
        substr($data, $i, 1) = pack('C', (($byte << $amount) | ($byte >> $anti_amount)) & 0xFF);
    }
    return $data;
}