# Hafta 3: Testleri bu dosyaya SİZ yazacaksınız.
# Çalıştırmak için bu klasörde:  python -m pytest -v

import pytest
from alistirma import kargo_ucreti, bilet_fiyati, ortalama


# --- 1. KARGO ÜCRETİ TESTLERİ ---

def test_kargo_buyuk_sipariste_ucretsiz():
    assert kargo_ucreti(800) == 0

def test_kargo_tam_sinirda_ucretsiz():
    # kargo-1 hatasını yakalar (tutar >= 500 yerine > 500 yapılırsa)
    assert kargo_ucreti(500) == 0

def test_kargo_sinirin_altinda_ucretli():
    assert kargo_ucreti(499) == 50
    assert kargo_ucreti(100) == 50

def test_kargo_sifir_tutar_gecerli():
    # kargo-2 hatasını yakalar (tutar < 0 yerine <= 0 yapılırsa)
    assert kargo_ucreti(0) == 50

def test_kargo_negatif_tutar_hata_firlatir():
    # kargo-3 hatasını yakalar (ValueError fırlatmak yerine değer döndürürse)
    with pytest.raises(ValueError):
        kargo_ucreti(-1)
    with pytest.raises(ValueError):
        kargo_ucreti(-50)


# --- 2. BİLET FİYATI TESTLERİ ---

def test_bilet_ucretsiz_yas_grubu():
    assert bilet_fiyati(0) == 0
    assert bilet_fiyati(3) == 0
    # bilet-1 hatasını yakalar (yas <= 6 yerine < 6 yapılırsa)
    assert bilet_fiyati(6) == 0

def test_bilet_ogrenci_yas_grubu():
    assert bilet_fiyati(7) == 50
    assert bilet_fiyati(12) == 50
    assert bilet_fiyati(17) == 50

def test_bilet_tam_yas_grubu():
    # bilet-2 hatasını yakalar (yas <= 17 yerine <= 18 yapılırsa)
    assert bilet_fiyati(18) == 100
    assert bilet_fiyati(30) == 100
    assert bilet_fiyati(64) == 100

def test_bilet_yasli_yas_grubu():
    # bilet-3 hatasını yakalar (yas >= 65 yerine > 65 yapılırsa)
    assert bilet_fiyati(65) == 60
    assert bilet_fiyati(80) == 60

def test_bilet_negatif_yas_hata_firlatir():
    with pytest.raises(ValueError):
        bilet_fiyati(-1)
    with pytest.raises(ValueError):
        bilet_fiyati(-10)


# --- 3. ORTALAMA TESTLERİ ---

def test_ortalama_normal_ve_kesirli_sonuc():
    assert ortalama([10, 20, 30]) == 20.0
    # ortalama-1 hatasını yakalar (/ yerine // tam sayı bölmesi yapılırsa)
    assert ortalama([70, 85]) == 77.5
    assert ortalama([1, 2]) == 1.5

def test_ortalama_tek_elemanli_liste():
    assert ortalama([100]) == 100.0

def test_ortalama_bos_liste_hata_firlatir():
    # ortalama-2 hatasını yakalar (boş listede ValueError yerine 0 döndürürse)
    with pytest.raises(ValueError):
        ortalama([])
        
