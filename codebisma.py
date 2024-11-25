 # Kelas untuk mendefinisikan objek Negara
class Country:
    def __init__(self, name, capital, language, population):
        self.name = name            # Nama negara
        self.capital = capital      # Ibu kota negara
        self.language = language    # Bahasa utama negara
        self.population = population  # Populasi negara
    
    def __str__(self):
        # Mengembalikan representasi string dari negara
        return f"Negara: {self.name}, Ibu Kota: {self.capital}, Bahasa: {self.language}, Populasi: {self.population}"

# Kelas untuk mengelola koleksi negara-negara di Asia
class AsiaCountries:
    def __init__(self):
        self.countries = []  # Daftar negara di Asia
    
    def add_country(self, country):
        """Menambahkan negara ke dalam daftar"""
        self.countries.append(country)
    
    def remove_country(self, name):
        """Menghapus negara berdasarkan nama dari daftar"""
        for country in self.countries:
            if country.name.lower() == name.lower():
                self.countries.remove(country)
                print(f'Negara {name} telah dihapus.')
                return
        print(f'Negara {name} tidak ditemukan.')
    
    def search_country(self, name):
        """Mencari negara berdasarkan nama"""
        for country in self.countries:
            if country.name.lower() == name.lower():
                return country
        return None
    
    def display_all_countries(self):
        """Menampilkan semua negara di Asia"""
        if self.countries:
            print("Daftar Negara di Asia:")
            for country in self.countries:
                print(country)
        else:
            print("Tidak ada data negara.")
    
    def display_country_by_population(self):
        """Menampilkan negara dengan populasi terbesar ke terkecil"""
        if self.countries:
            sorted_countries = sorted(self.countries, key=lambda x: x.population, reverse=True)
            print("Negara dengan populasi terbesar di Asia:")
            for country in sorted_countries:
                print(country)
        else:
            print("Tidak ada data negara.")

# Membuat beberapa objek Negara
india = Country("India", "New Delhi", "Hindi", 1393409038)
china = Country("China", "Beijing", "Mandarin", 1444216107)
japan = Country("Japan", "Tokyo", "Japanese", 125584838)
indonesia = Country("Indonesia", "Jakarta", "Indonesian", 276361783)

# Membuat objek AsiaCountries
asia = AsiaCountries()

# Menambahkan negara ke dalam database
asia.add_country(india)
asia.add_country(china)
asia.add_country(japan)
asia.add_country(indonesia)

# Menampilkan semua negara di Asia
asia.display_all_countries()

# Mencari negara berdasarkan nama
country = asia.search_country("Japan")
if country:
    print(f"\nNegara yang ditemukan: {country}")
else:
    print("\nNegara tidak ditemukan.")

# Menampilkan negara berdasarkan populasi terbesar
asia.display_country_by_population()

# Menghapus negara dari daftar
asia.remove_country("Japan")

# Menampilkan daftar negara setelah penghapusan
asia.display_all_countries()