import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_positiivisen_varaston(self):
        self.neg = Varasto(5, 6)
        self.assertAlmostEqual(self.neg.saldo, 5)
        self.assertAlmostEqual(self.neg.tilavuus, 5)

    def test_konstruktori_luo_tyhjan_negatiivisen_varaston(self):
        self.neg = Varasto(-1, -1)
        self.assertAlmostEqual(self.neg.saldo, 0)
        self.assertAlmostEqual(self.neg.tilavuus, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_saldo_ei_mene_yli_tilavuuden(self):
        self.varasto.lisaa_varastoon(self.varasto.tilavuus + 50)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_negatiivinen_maara_ei_lisaa_varastoa(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivinen_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(saatu_maara, 0.0)

    def test_positiivinen_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_positiivinen_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_saldo_ei_saa_olla_yli_tilavuuden(self):
        maara = self.varasto.ota_varastosta(self.varasto.saldo + 2)
        self.assertAlmostEqual(maara, self.varasto.saldo)

    def test_str(self):
        self.assertEqual(self.varasto.__str__(), f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}")