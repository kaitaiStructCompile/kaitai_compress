// ProcessZlib decompresses the given bytes as specified in RFC 1950.
func ProcessZlib(in []byte) ([]byte, error) {
	b := bytes.NewReader(in)

	// FIXME zlib.NewReader allocates a bunch of memory.  In the future
	// we could reuse it by using a sync.Pool if this is called in a tight loop.
	r, err := zlib.NewReader(b)
	if err != nil {
		return nil, err
	}

	return ioutil.ReadAll(r)
}