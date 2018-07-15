KaitaiStream.processZlib = function(buf) {
  if (typeof require !== 'undefined')  {
    // require is available - we're running under node
    if (typeof KaitaiStream.zlib === 'undefined')
      KaitaiStream.zlib = require('zlib');
    if (buf instanceof Uint8Array) {
      var b = new Buffer(buf.buffer);
    } else {
      var b = buf;
    }
    // use node's zlib module API
    var r = KaitaiStream.zlib.inflateSync(b);
    return r;
  } else {
    // no require() - assume we're running as a web worker in browser.
    // user should have configured KaitaiStream.depUrls.zlib, if not
    // we'll throw.
    if (typeof KaitaiStream.zlib === 'undefined'
      && typeof KaitaiStream.depUrls.zlib !== 'undefined') {
      importScripts(KaitaiStream.depUrls.zlib);
      KaitaiStream.zlib = pako;
    }
    // use pako API
    r = KaitaiStream.zlib.inflate(buf);
    return r;
  }
}