function KaitaiStream.process_xor_one(data, key)
    local r = ""

    for i = 1, #data do
        local c = data:byte(i) ~ key
        r = r .. string.char(c)
    end

    return r
end

function KaitaiStream.process_xor_many(data, key)
    local r = ""
    local kl = key:len()
    local ki = 1

    for i = 1, #data do
        local c = data:byte(i) ~ key:byte(ki)
        r = r .. string.char(c)
        ki = ki + 1
        if ki > kl then
            ki = 1
        end
    end

    return r
end

function KaitaiStream.process_rotate_left(data, amount, group_size)
    if group_size ~= 1 then
        error("unable to rotate group of " .. group_size .. " bytes yet")
    end

    local result = ""
    local mask = group_size * 8 - 1
    local anti_amount = -amount & mask

    for i = 1, #data  do
        local c = data:byte(i)
        c = ((c << amount) & 0xFF) | (c >> anti_amount)
        result = result .. string.char(c)
    end

    return result
end