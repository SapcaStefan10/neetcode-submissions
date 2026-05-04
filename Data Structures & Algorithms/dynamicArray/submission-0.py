class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity  # Câte locuri avem în total
        self.length = 0           # Câte locuri sunt ocupate acum
        self.arr = [0] * capacity # Creăm "cutia" goală

    def get(self, i: int) -> int:
        # Mergem direct la indexul i
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # Schimbăm valoarea de la indexul i
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # Dacă s-a umplut cutia, luăm una dublă
        if self.length == self.capacity:
            self.resize()
        
        # Punem elementul la prima poziție liberă
        self.arr[self.length] = n
        # Creștem numărul de elemente ocupate
        self.length += 1

    def popback(self) -> int:
        # "Ștergem" ultimul element (scăzând lungimea) și îl returnăm
        # Practic, elementul rămâne în memorie, dar noi îl ignorăm de acum
        self.length -= 1
        return self.arr[self.length]

    def resize(self) -> None:
        # Dublăm capacitatea
        self.capacity = self.capacity * 2
        # Creăm o cutie nouă, mai mare
        new_arr = [0] * self.capacity
        
        # Mutăm toate obiectele din cutia veche în cea nouă
        for i in range(self.length):
            new_arr[i] = self.arr[i]
            
        # Spunem că de acum "cutia noastră" este cea nouă
        self.arr = new_arr

    def getSize(self) -> int:
        # Câte elemente avem puse efectiv
        return self.length

    def getCapacity(self) -> int:
        # Cât spațiu total avem rezervat
        return self.capacity