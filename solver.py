class PrioQueue:
    #ctor
    def __init__(self):
	    self.prioqueue = []

    #buat print prioqueue
    def __str__(self):
        return ','.join([str(i) for i in self.prioqueue])

	# cek kosong
    def isEmpty(self):
        return len(self.prioqueue) == 0

	# enqueue elemen, prionya ada di dequeue jadi ga usah diurutin di enqueue
    def enqueue(self, data):
        self.prioqueue.append(data)

	# dequeue dari yg terkecil
    def dequeue(self):
        min = 0
        for i in range(len(self.prioqueue)):
            if self.prioqueue[i][0] < self.prioqueue[min][0]:
                min = i
        pilihmin = self.prioqueue[min]
        del self.prioqueue[min]
        return pilihmin


def kurang(p):
    arsir = [0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0]
    total = 0
    for i in range(len(p)):
        totangka = 0
        for j in range(i+1, len(p)):
            if p[j] < p[i] and p[j] != 16:
                totangka +=1
        total += totangka
    indekskosong = p.index(16)
    #print(indekskosong)
    if arsir[indekskosong]:
        total+=1
    #print(total)
    if total % 2 == 0: 
        return True
    else:
        return False

def ketemu(p):
    previous = p[0]
    for number in p:
        if number < previous:
            return False
        previous = number
    return True

def g(p):
    count = 0
    for i in range(len(p)):
        if p[i] != 16 and p[i] != i+1:
            count+=1
    return count

def buatanak(p, jarak, path):
    #isinya puzzle habis digerakin
    sofar = jarak + 1
    estimasi = sofar + g(p)
    pathnow = path[:]
    pathnow.append(p)
    return [estimasi, sofar, pathnow, p]

def gerakatas(p):
    #p = [1,2,3,4
    #     5,6,7,8
    #     9,10,11,12
    #     13,14,15,16]
    idx= p.index(16)
    if idx < 4:
        atas = False
    else:
        atas = p[:]
        temp = idx-4
        atas[idx] = atas[temp]
        atas[temp] = 16
    return atas

def gerakbawah(p):
    #p = [1,2,3,4
    #     5,6,7,8
    #     9,10,11,12
    #     13,14,15,16]
    idx= p.index(16)
    if idx > 11:
        bawah = False
    else:
        bawah = p[:]
        temp = idx+4
        bawah[idx] = bawah[temp]
        bawah[temp] = 16
    return bawah

def gerakkiri(p):
    #p = [1,2,3,4
    #     5,6,7,8
    #     9,10,11,12
    #     13,14,15,16]
    idx= p.index(16)
    if idx == 0 or idx == 4 or idx == 8 or idx == 12:
        kiri = False
    else:
        kiri = p[:]
        temp = idx-1
        kiri[idx] = kiri[temp]
        kiri[temp] = 16
    return kiri

def gerakkanan(p):
    #p = [1,2,3,4
    #     5,6,7,8
    #     9,10,11,12
    #     13,14,15,16]
    idx= p.index(16)
    if idx == 3 or idx == 7 or idx == 11 or idx == 15:
        kanan = False
    else:
        kanan = p[:]
        temp = idx+1
        kanan[idx] = kanan[temp]
        kanan[temp] = 16
    return kanan

def output(p):
    for i in range(len(p)):
        if p[i] == 16:
            print("-", end=" ")
        else:
            print(p[i], end=" ")
        if i == 3 or i == 7 or i == 11 or i == 15:
            print()

def astar(entry):
    #Mulai algo A*

    #list awal
    #list[estimasi, sejauhini, path, current, langkah]
    awal = [0 ,0, [entry], entry, []]

    #prioqueue untuk A*, prioritas dari estimasi
    listjalan = PrioQueue()
    listjalan.enqueue(awal) #prioqueue dari list
    found = False
    listvisited = []
    while not listjalan.isEmpty():
        popped = listjalan.dequeue() #dequeue dari list
        listvisited.append(popped[3])
        if (ketemu(popped[3])): #kalau sudah ketemu target di end
            found = True
            break

        jarak = popped[1]
        path = popped[2] #ambil path sejauh ini
        langkah = popped[4]
        now = popped[3]
        #gerak atas
        atas = gerakatas(now)
        #gerak bawah
        bawah = gerakbawah(now)
        #gerak kanan
        kanan = gerakkanan(now)
        #gerak kiri
        kiri = gerakkiri(now)
        
        if atas != False and atas not in listvisited:
            anakatas = buatanak(atas, jarak, path)
            l = langkah[:]
            l.append("Atas")
            anakatas.append(l)
            listjalan.enqueue(anakatas)
        if bawah != False and bawah not in listvisited:
            anakbawah = buatanak(bawah, jarak, path)
            l = langkah[:]
            l.append("Bawah")
            anakbawah.append(l)
            listjalan.enqueue(anakbawah)
        if kiri != False and kiri not in listvisited:
            anakkiri = buatanak(kiri, jarak, path)
            l = langkah[:]
            l.append("Kiri")
            anakkiri.append(l)
            listjalan.enqueue(anakkiri)
        if kanan != False and kanan not in listvisited:
            anakkanan = buatanak(kanan, jarak, path)
            l = langkah[:]
            l.append("Kanan")
            anakkanan.append(l)
            listjalan.enqueue(anakkanan)

    return popped, found

def solve(p):
    if kurang(p):
        print("Puzzle solvable")
        res, found = astar(p)
        path = res[2]
        for i in range (len(path)):
            output(path[i])
            print()
        print(res[4])
    else:
        print("Puzzle unsolvable")


if __name__ == '__main__':
    #Indeks = posisi, nilai indeks = angka
    #1 2 3 4
    #5 6 7 8
    #9 10 11 12
    #13 14 15 16
    #16 = kosong
    p = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    tes = [1,3,4,15,2,16,5,12,7,6,11,14,8,9,10,13]
    tes2 = [1,2,3,4,5,6,16,8,9,10,7,11,13,14,15,12]
    tes3 = [1,2,3,4,5,6,16,8,11,10,7,12,13,15,9,14] #
    tes4 = [16,2,3,4,1,5,6,8,9,11,7,12,13,10,14,15]
    tes5 = [2,3,6,4,9,1,15,7,5,10,11,8,13,12,16,14] #
    solve(tes4)