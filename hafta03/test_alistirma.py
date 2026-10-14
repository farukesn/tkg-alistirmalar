# Hafta 3: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest -v

import pytest
from alistirma import kargo_ucreti, bilet_fiyati, ortalama

def test_kargo_ucreti():
    assert kargo_ucreti(500) == 0
    assert kargo_ucreti(499) == 50
    assert kargo_ucreti(0) == 50
    with pytest.raises(ValueError):
        kargo_ucreti(-1)

def test_bilet_fiyati():
    assert bilet_fiyati(6) == 0
    assert bilet_fiyati(17) == 50
    assert bilet_fiyati(18) == 100
    assert bilet_fiyati(65) == 60
    with pytest.raises(ValueError):
        bilet_fiyati(-1)

def test_ortalama():
    assert ortalama([70, 85]) == 77.5
    with pytest.raises(ValueError):
        ortalama([])
