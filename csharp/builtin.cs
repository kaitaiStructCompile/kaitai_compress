        /// <summary>
        /// Performs XOR processing with given data, XORing every byte of the input with a single value.
        /// </summary>
        /// <param name="value">The data toe process</param>
        /// <param name="key">The key value to XOR with</param>
        /// <returns>Processed data</returns>
        public byte[] ProcessXor(byte[] value, int key)
        {
            byte[] result = new byte[value.Length];
            for (int i = 0; i < value.Length; i++)
            {
                result[i] = (byte)(value[i] ^ key);
            }
            return result;
        }

        /// <summary>
        /// Performs XOR processing with given data, XORing every byte of the input with a key
        /// array, repeating from the beginning of the key array if necessary
        /// </summary>
        /// <param name="value">The data toe process</param>
        /// <param name="key">The key array to XOR with</param>
        /// <returns>Processed data</returns>
        public byte[] ProcessXor(byte[] value, byte[] key)
        {
            int keyLen = key.Length;
            byte[] result = new byte[value.Length];
            for (int i = 0, j = 0; i < value.Length; i++, j = (j + 1) % keyLen)
            {
                result[i] = (byte)(value[i] ^ key[j]);
            }
            return result;
        }

        /// <summary>
        /// Performs a circular left rotation shift for a given buffer by a given amount of bits.
        /// Pass a negative amount to rotate right.
        /// </summary>
        /// <param name="data">The data to rotate</param>
        /// <param name="amount">The number of bytes to rotate by</param>
        /// <param name="groupSize"></param>
        /// <returns></returns>
        public byte[] ProcessRotateLeft(byte[] data, int amount, int groupSize)
        {
            if (amount > 7 || amount < -7) throw new ArgumentException("Rotation of more than 7 cannot be performed.", "amount");
            if (amount < 0) amount += 8; // Rotation of -2 is the same as rotation of +6

            byte[] r = new byte[data.Length];
            switch (groupSize)
            {
                case 1:
                    for (int i = 0; i < data.Length; i++)
                    {
                        byte bits = data[i];
                        // http://stackoverflow.com/a/812039
                        r[i] = (byte) ((bits << amount) | (bits >> (8 - amount)));
                    }
                    break;
                default:
                    throw new NotImplementedException(string.Format("Unable to rotate a group of {0} bytes yet", groupSize));
            }
            return r;
}
