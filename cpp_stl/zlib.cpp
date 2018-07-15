#ifdef KS_ZLIB
#include <zlib.h>

std::string kaitai::kstream::process_zlib(std::string data) {
    int ret;

    unsigned char *src_ptr = reinterpret_cast<unsigned char*>(&data[0]);
    std::stringstream dst_strm;

    z_stream strm;
    strm.zalloc = Z_NULL;
    strm.zfree = Z_NULL;
    strm.opaque = Z_NULL;

    ret = inflateInit(&strm);
    if (ret != Z_OK)
        throw std::runtime_error("process_zlib: inflateInit error");

    strm.next_in = src_ptr;
    strm.avail_in = data.length();

    unsigned char outbuffer[ZLIB_BUF_SIZE];
    std::string outstring;

    // get the decompressed bytes blockwise using repeated calls to inflate
    do {
        strm.next_out = reinterpret_cast<Bytef*>(outbuffer);
        strm.avail_out = sizeof(outbuffer);

        ret = inflate(&strm, 0);

        if (outstring.size() < strm.total_out)
            outstring.append(reinterpret_cast<char*>(outbuffer), strm.total_out - outstring.size());
    } while (ret == Z_OK);

    if (ret != Z_STREAM_END) {          // an error occurred that was not EOF
        std::ostringstream exc_msg;
        exc_msg << "process_zlib: error #" << ret << "): " << strm.msg;
        throw std::runtime_error(exc_msg.str());
    }

    if (inflateEnd(&strm) != Z_OK)
        throw std::runtime_error("process_zlib: inflateEnd error");

    return outstring;
}
#endif