import random

class DNA:

    def __init__(self):
        self.word = ''
        self.score = 0

    def randomize(self, basic_word):
        """
        creates random words
        """
        random.seed()
        length = len(basic_word)
        for l in range(0,length):
            numb = random.randrange(65, 90)
            self.word += chr(numb)
        assert len(self.word) == len(basic_word)
        self.word = self.word.lower()

    def count_fitness(self, basic_word):
        used_letters = []
        for b in basic_word:
            for p in self.word:
                if p not in used_letters:
                    if p == b:
                        used_letters.append(p)
                        if basic_word.find(b) == self.word.find(p):
                            self.score += 1
                            self.score = self.score*100/len(basic_word)
            else:
                pass

    def crossover(self, second_word):
        """
        randomly crossover words
        """
        chars = int(len(self.word))
        new_word=""
        for i in range(chars):
            if int(100*random.random())<50:
                new_word +=self.word[i]
            else:
                new_word +=second_word[i]
        assert len(new_word) == len(self.word)
        dna = DNA()
        dna.word = new_word
        return dna

    def mutate(self, mutation_rate):
        random.seed()
        number = int(mutation_rate/7*100)
        for i in range(number):
            index = int(random.random() * len(self.word))
            if index == 0:
                self.word = chr(97 + int(26 * random.random())) + self.word[1:]
            else:
                self.word = self.word[:index - 1] + chr(97 + int(26 * random.random())) + self.word[index:]

    def change_letter(self, l):
        if ord(l) <= 119:
            new_letter = chr(ord(l) + 3)
        else:
            number = 3 - (122 - ord(l))
            new_letter = chr(97+number)
        return new_letter

    def __str__(self):
        return self.word + ' fitnese score:' + str(self.score)