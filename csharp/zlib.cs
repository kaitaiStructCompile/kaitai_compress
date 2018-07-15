        /// <summary>
        /// Inflates a deflated zlib byte stream
        /// </summary>
        /// <param name="data">The data to deflate</param>
        /// <returns>The deflated result</returns>
        public byte[] ProcessZlib(byte[] data)
        {
            // See RFC 1950 (https://tools.ietf.org/html/rfc1950)
            // zlib adds a header to DEFLATE streams - usually 2 bytes,
            // but can be 6 bytes if FDICT is set.
            // There's also 4 checksum bytes at the end of the stream.

            byte zlibCmf = data[0];
            if ((zlibCmf & 0x0F) != 0x08) throw new NotSupportedException("Only the DEFLATE algorithm is supported for zlib data.");

            const int zlibFooter = 4;
            int zlibHeader = 2;

            // If the FDICT bit (0x20) is 1, then the 4-byte dictionary is included in the header, we need to skip it
            byte zlibFlg = data[1];
            if ((zlibFlg & 0x20) == 0x20) zlibHeader += 4;

            using (MemoryStream ms = new MemoryStream(data, zlibHeader, data.Length - (zlibHeader + zlibFooter)))
            {
                using (DeflateStream ds = new DeflateStream(ms, CompressionMode.Decompress))
                {
                    using (MemoryStream target = new MemoryStream())
                    {
                        ds.CopyTo(target);
                        return target.ToArray();
                    }
                }
            }
}
