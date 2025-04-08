def hash_personalizado(cadena):
    valor = 0
    for i, c in enumerate(cadena):
        valor += (i + 1) * ord(c)
    return valor % 101

class BloomFilter:
    def __init__(self, size=1000, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item):
        return [(hash_personalizado(item + str(i)) % self.size) for i in range(self.hash_count)]

    def add(self, item):
        for i in self._hashes(item):
            self.bit_array[i] = 1

    def __contains__(self, item):
        return all(self.bit_array[i] for i in self._hashes(item))

def crear_tabla_bloom(n_gramas):
    bf = BloomFilter()
    for ng in n_gramas:
        bf.add(ng)
    return bf
