package kaitai

import (
	"bytes"
	"compress/zlib"
	"io/ioutil"
	"math/bits"

	"golang.org/x/text/encoding"
	"golang.org/x/text/transform"
)

// ProcessXOR returns data xored with the key.
func ProcessXOR(data []byte, key []byte) []byte {
	out := make([]byte, len(data))
	for i := range data {
		out[i] = data[i] ^ key[i%len(key)]
	}
	return out
}

// ProcessRotateLeft returns the single bytes in data rotated left by
// amount bits.
func ProcessRotateLeft(data []byte, amount int) []byte {
	out := make([]byte, len(data))
	for i := range data {
		out[i] = bits.RotateLeft8(data[i], amount)
	}
	return out
}

// ProcessRotateRight returns the single bytes in data rotated right by
// amount bits.
func ProcessRotateRight(data []byte, amount int) []byte {
	return ProcessRotateLeft(data, -amount)
}
