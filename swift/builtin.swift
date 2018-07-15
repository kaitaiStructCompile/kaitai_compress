    public func processRotateLeft(bytes:[UInt8],amount:UInt,groupSize:Int=1) -> [UInt8]? {
        var r = [UInt8](count:0, repeatedValue:0)

        switch groupSize {
        case 1:
            for i in 0..<bytes.count {
                let byte = UInt(bytes[i])

                r[i] = UInt8((((byte & 0xff) << amount) | ((byte & 0xff) >> (8 - amount))));
            }
        default:
            return nil
        }

        return r
    }
