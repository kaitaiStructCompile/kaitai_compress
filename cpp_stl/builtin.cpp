std::string kaitai::kstream::process_xor_one(std::string data, uint8_t key) {
    size_t len = data.length();
    std::string result(len, ' ');

    for (size_t i = 0; i < len; i++)
        result[i] = data[i] ^ key;

    return result;
}

std::string kaitai::kstream::process_xor_many(std::string data, std::string key) {
    size_t len = data.length();
    size_t kl = key.length();
    std::string result(len, ' ');

    size_t ki = 0;
    for (size_t i = 0; i < len; i++) {
        result[i] = data[i] ^ key[ki];
        ki++;
        if (ki >= kl)
            ki = 0;
    }

    return result;
}

std::string kaitai::kstream::process_rotate_left(std::string data, int amount) {
    size_t len = data.length();
    std::string result(len, ' ');

    for (size_t i = 0; i < len; i++) {
        uint8_t bits = data[i];
        result[i] = (bits << amount) | (bits >> (8 - amount));
    }

    return result;
}