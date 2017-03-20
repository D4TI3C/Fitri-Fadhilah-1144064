graph = {
             'Mekarwangi': ['Buniwangi'],
             'Buniwangi': ['Pasir Muncang'],
             'Pasir Muncang': ['PPR ITB'],
             'PPR ITB': ['Bengkok'],
             'Bengkok': ['Stamplat'],
             'Stamplat': ['Terminal Dago'],
             'Terminal Dago': ['Coblong'],
             'Coblong': ['Simpang Dago'],        
        }

def ruteterpendek(graph, lokasi_awal, lokasi_tujuan, rute=[]):
        rute = rute + [lokasi_awal]
        if lokasi_awal == lokasi_tujuan:
            return rute
            if not graph.has_key(lokasi_awal):
                    return None
        rutependek = None
        for node in graph[lokasi_awal]:
            if node not in rute:
                rutebaru = ruteterpendek(graph, node, lokasi_tujuan, rute)
                if rutebaru:
                    if not rutependek or len(rutebaru) < len(rutependek):
                        rutependek = rutebaru
        return rutependek
print("Rute Jalan Raya Mekarwangi Sampai Coblong")
print("(Mekarwangi-Buniwangi-Pasir Muncang-PPR ITB-Bengkok-Stamplat-Terminal Dago-Coblong-Simpang Dago)")
print("1144064 Fitri Fadhilah")
print("\n")
lokasi_awal = raw_input("Masukan Lokasi Awal : ")
lokasi_tujuan = raw_input("Masukan Lokasi Tujuan : ")
hasilnya = ruteterpendek(graph, lokasi_awal, lokasi_tujuan, rute=[])
print "Rute Terpendek", hasilnya ,".",