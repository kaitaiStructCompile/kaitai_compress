
    use flate2::read::ZlibDecoder;
    fn process_zlib(&mut self, data: Vec<u8>) -> Result<Vec<u8>> {
        let mut decoder = ZlibDecoder::new(Cursor::new(data));
        let mut result = Vec::new();
        match decoder.read_to_end(&mut result) {
            Ok(_) => Ok(result),
            Err(e) => Err(e),
        }
    }

