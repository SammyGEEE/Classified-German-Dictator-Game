import gameEngine

import unittest

class TestGameCreation(unittest.TestCase):

    def test_DeckShuffle(self):
        #Arange
        testDeck = gameEngine.gameDeck()
        #Act and Assert
        self.assertNotEqual(testDeck, ['liberal' * 6, 'fascist' * 11])
        self.assertEqual(len(testDeck.deck), 17)

    def test_DeckDraw(self):
        #Arrange
        testDeck = gameEngine.gameDeck()
        #Act
        testDraw = testDeck.draw()
        #Assert
        self.assertTrue(testDraw in ["liberal", "fascist"])


    def test_prepareRoles_5Players(self):
        #Arrange
        game = gameEngine.game()
        roleComp = ['H', 'F', 'L', 'L', 'L']
        #Act
        roleDeck = game.prepareRoles(5)
        #Assert
        self.assertTrue(set(roleDeck) == set(roleComp))

    
    def test_prepareRoles_10Players(self):
        #Arrange
        game = gameEngine.game()
        roleComp = ['H', 'F', 'F', 'F', 'L', 'L', 'L', 'L', 'L', 'L']
        #Act
        roleDeck = game.prepareRoles(10)
        #Assert
        self.assertTrue(set(roleDeck) == set(roleComp))
    
    def test_giveRole_Liberal(self):
        #Arrange
        game = gameEngine.game()
        testName = 'Sam'
        testRole = 'L'
        #Act
        game.giveRole(testName, testRole)
        #Assert
        self.assertTrue(type(game.players[0]) == gameEngine.liberal)
        self.assertEqual(game.players[0].name, testName)

    


if __name__ == "__main__":
    unittest.main()

