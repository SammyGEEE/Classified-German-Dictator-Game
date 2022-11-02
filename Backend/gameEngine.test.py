
import gameEngine
import unittest

class TestGameCreation(unittest.TestCase):

    def test_DeckShuffle(self):
        #Arange
        self.testDeck1 = gameEngine.gameDeck()
        #Act and Assert
        self.assertNotEqual(self.testDeck1, ['liberal' * 6, 'fascist' * 11])
        self.assertEqual(len(self.testDeck1.deck), 17)

    def test_DeckDraw(self):
        #Arrange
        self.testDeck2 = gameEngine.gameDeck()
        #Act
        testDraw = self.testDeck2.draw()
        #Assert
        self.assertTrue(testDraw in ["liberal", "fascist"])


    def test_prepareRoles_5Players(self):
        #Arrange
        self.game1 = gameEngine.game()
        self.roleComp1 = ['H', 'F', 'L', 'L', 'L']
        #Act
        self.roleDeck1 = self.game1.prepareRoles(5)
        #Assert
        self.assertTrue(set(self.roleDeck1) == set(self.roleComp1))

    


if __name__ == "__main__":
    unittest.main()

