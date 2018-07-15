    public func processZlib(bytes:[UInt8]) -> [UInt8]? {
        let inflater = InflateStream()

        var bytes = Array(bytes)
        let (inflated,err) = inflater.write(&bytes, flush: true)

        guard err == nil else {
            return nil
        }

        return inflated
    }
