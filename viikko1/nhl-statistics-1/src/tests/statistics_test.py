import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_number_of_players_team(self):
        self.assertEqual(len(self.statistics.team("EDM")), 3)

    def test_search_name_none(self):
        self.assertEqual(str(self.statistics.search("Semi")), "None")
    
    def test_searc_name(self):
        self.assertEqual(str(self.statistics.search("Semenko")), "Semenko EDM 4 + 12 = 16")

    def test_search_team(self):
        self.assertEqual(str(self.statistics.team('EDM')[0]),'Semenko EDM 4 + 12 = 16')

    def test_search_top_player(self):
        self.assertEqual(str(self.statistics.top_scorers(1)[0]), 'Gretzky EDM 35 + 89 = 124')

