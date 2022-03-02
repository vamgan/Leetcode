class Codec:
    def encode(self, strs: [str]) -> str:
        return str(len(strs)) + '\t' + '\t'.join(strs)

    def decode(self, s: str) -> [str]:
        length, *strs = s.split('\t')
        return [] if length == '0' else strs