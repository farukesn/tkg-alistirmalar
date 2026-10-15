# Lab, Bölüm 2: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum2.py test_hatali_surumler.py -v

import pytest

from bolum2 import sifre_gucu, otopark_ucreti, yuzde_degisim


def test_kisa_sifre_zayif():
    assert sifre_gucu("abc") == "zayıf"
    assert sifre_gucu("yagmur2626")=="orta"
    assert sifre_gucu("yagmurgul")=="orta"
    assert sifre_gucu("yagmurgul2626")=="güçlü"
    assert sifre_gucu("fatmaoguzguneyli07")=="güçlü"
    assert sifre_gucu("yagmur1")=="zayıf"
    assert sifre_gucu("yagmur12")=="orta"
    assert sifre_gucu("yagmur12345")=="orta"
    assert sifre_gucu("yagmur123456") =="güçlü"
    with pytest.raises(ValueError):
        sifre_gucu("")

def test_otopark_ucreti():
    assert otopark_ucreti(14) == 0
    assert otopark_ucreti(15) == 0
    assert otopark_ucreti(59) == 20
    assert otopark_ucreti(60) == 20
    assert otopark_ucreti(179) == 40
    assert otopark_ucreti(180) == 40
    assert otopark_ucreti(181) == 60
    with pytest.raises(ValueError):
        otopark_ucreti(-1) 

def test_yuzde_degisim(): 
    assert yuzde_degisim(50, 100) == 100.0
    assert yuzde_degisim(100, 50) == -50.0
    with pytest.raises(ValueError):
        yuzde_degisim(0, 100)
