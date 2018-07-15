KaitaiStream.processXorOne = function(data, key) {
  var r = new Uint8Array(data.length);
  var dl = data.length;
  for (var i = 0; i < dl; i++)
    r[i] = data[i] ^ key;
  return r;
}

KaitaiStream.processXorMany = function(data, key) {
  var r = new Uint8Array(data.length);
  var dl = data.length;
  var kl = key.length;
  var ki = 0;
  for (var i = 0; i < data.length; i++) {
    r[i] = data[i] ^ key[ki];
    ki++;
    if (ki >= kl)
      ki = 0;
  }
  return r;
}

KaitaiStream.processRotateLeft = function(data, amount, groupSize) {
  if (groupSize != 1)
    throw("unable to rotate group of " + groupSize + " bytes yet");

  var mask = groupSize * 8 - 1;
  var antiAmount = -amount & mask;

  var r = new Uint8Array(data.length);
  for (var i = 0; i < data.length; i++)
    r[i] = (data[i] << amount) & 0xff | (data[i] >> antiAmount);

  return r;
}
