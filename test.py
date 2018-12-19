from unittest import TestCase
from genetic import DNA

class TestDna(TestCase):
    def setUp(self):
        pass

    def test_fitnesse(self):
        dna = DNA()
        dna.word = "cccccccc"
        dna.count_fitness("unicorn")
        assert dna.score == 1

    def test_mutation(self):
        dna = DNA()
        dna.word = "cccccccc"
        dna.count_fitness("unicorn")
        dna.mutate(0.3)
        print(dna.word)