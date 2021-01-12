Feature: Comparing words
    We are comparing words or checking if first includes second

    Scenario: User types in siemanko and siemanko

        Given two words
        """
        siemanko,siemanko
        """
        When they are the same
        Then returns True

    Scenario: User types in siemanko and siema

        Given two words
        """
        siemanko,siema
        """        
        When first includes second
        Then returns True

    Scenario: User types in siema and siemanko

        Given two words
        """
        siema,siemanko
        """        
        When second includes first
        Then returns False

    Scenario: User types two totally different words
        Given two words
        """
        siemanko,eluwina
        """
        When they are different
        Then returns False

    Scenario: User types only one word

        Given one word
        """
        siemanko
        """        
        Then you have to type two words

    Scenario: User types in witam and witam

        Given two words
        """
        witam,witam
        """        
        When they are the same
        Then returns True

    Scenario: User types zero words
        Given zero words
        Then you have to type two words

    Scenario: User types in elopomelo and elo
        Given two words
        """
        elopomelo,elo
        """
        When first includes second
        Then returns True


