Feature: Comparing words
    We are comparing words or checking if first includes second

    @words
    Scenario: User types in siemanko and siemanko
        Given two words
        """
        siemanko,siemanko
        """
        When they are the same
        Then returns True
        
    @words
    Scenario: User types in siemanko and siema
        Given two words
        """
        siemanko,siema
        """        
        When first includes second
        Then returns True

    @words
    Scenario: User types in siema and siemanko
        Given two words
        """
        siema,siemanko
        """        
        When second includes first
        Then returns False

    @words
    Scenario: User types two totally different words
        Given two words
        """
        siemanko,eluwina
        """
        When they are different
        Then returns False

    @words
    Scenario: User types only one word

        Given one word
        """
        siemanko
        """        
        Then you have to type two words

    @words
    Scenario: User types in witam and witam

        Given two words
        """
        witam,witam
        """        
        When they are the same
        Then returns True

    @words
    Scenario: User types zero words
        Given zero words
        Then you have to type two words

    @words
    Scenario: User types in elopomelo and elo
        Given two words
        """
        elopomelo,elo
        """
        When first includes second
        Then returns True


