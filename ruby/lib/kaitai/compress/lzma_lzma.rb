# RubyGems: ruby-xz >= 1
require 'xz'

module Kaitai
  module Compress
    class LzmaLzma
      def decode(data)
        XZ::decompress(data)
      end
    end
  end
end
