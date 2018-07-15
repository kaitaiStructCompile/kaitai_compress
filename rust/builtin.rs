    fn process_xor_one(&mut self, value: Vec<u8>, key: u8) -> Vec<u8> {
        let mut result = vec![0; value.len()];
        for i in 0..value.len() {
            result[i] = (value[i] ^ key) as u8;
        }
        return result;
    }

    fn process_xor_many(&mut self, value: Vec<u8>, key: Vec<u8>) -> Vec<u8> {
        let mut result = vec![0; value.len()];
        let mut j = 0;
        for i in 0..value.len() {
            result[i] = (value[i] ^ key[j]) as u8;
            j = (j + 1) % key.len();
        }
        return result;
    }

    fn process_rotate_left(&mut self, data: Vec<u8>, amount: i32, group_size: i32) -> Vec<u8> {
        if amount < -7 || amount > 7 {
            panic!("Rotation of more than 7 cannot be performed.");
        }

        let mut rot_amount = amount;
        if rot_amount < 0 {
            rot_amount += 8;
        }

        let mut result = vec![0; data.len()];
        match group_size {
            1 => {
                for i in 0..data.len() {
                    result[i] = data[i].rotate_left(rot_amount as u32);
                }
            }
            _ => panic!("Unable to rotate a group of {} bytes yet", group_size),
        }
        return result;
    }

