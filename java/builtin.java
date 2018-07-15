/**
     * Performs a XOR processing with given data, XORing every byte of input with a single
     * given value.
     * @param data data to process
     * @param key value to XOR with
     * @return processed data
     */
    public static byte[] processXor(byte[] data, int key) {
        int dataLen = data.length;
        byte[] r = new byte[dataLen];
        for (int i = 0; i < dataLen; i++)
            r[i] = (byte) (data[i] ^ key);
        return r;
    }

    /**
     * Performs a XOR processing with given data, XORing every byte of input with a key
     * array, repeating key array many times, if necessary (i.e. if data array is longer
     * than key array).
     * @param data data to process
     * @param key array of bytes to XOR with
     * @return processed data
     */
    public static byte[] processXor(byte[] data, byte[] key) {
        int dataLen = data.length;
        int valueLen = key.length;

        byte[] r = new byte[dataLen];
        int j = 0;
        for (int i = 0; i < dataLen; i++) {
            r[i] = (byte) (data[i] ^ key[j]);
            j = (j + 1) % valueLen;
        }
        return r;
    }

    /**
     * Performs a circular left rotation shift for a given buffer by a given amount of bits,
     * using groups of groupSize bytes each time. Right circular rotation should be performed
     * using this procedure with corrected amount.
     * @param data source data to process
     * @param amount number of bits to shift by
     * @param groupSize number of bytes per group to shift
     * @return copy of source array with requested shift applied
     */
    public static byte[] processRotateLeft(byte[] data, int amount, int groupSize) {
        byte[] r = new byte[data.length];
        switch (groupSize) {
            case 1:
                for (int i = 0; i < data.length; i++) {
                    byte bits = data[i];
                    // http://stackoverflow.com/a/19181827/487064
                    r[i] = (byte) (((bits & 0xff) << amount) | ((bits & 0xff) >>> (8 - amount)));
                }
                break;
            default:
                throw new UnsupportedOperationException("unable to rotate group of " + groupSize + " bytes yet");
        }
        return r;
    }
