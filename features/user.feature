Feature: valid_password method from User class
    this method checks if entered password is strong enough

    Scenario: Check if 'abc' is valid
        Given password parameter equal to abc
        """
        abc
        """
        When checks if abc is valid
        Then password abc should not be valid

    Scenario: Check if 'Abc' is valid
        Given password parameter equal to Abc
        """
        Abc
        """
        When checks if Abc is valid
        Then password Abc should not be valid

    Scenario: Check if 'Abc1' is valid
        Given password parameter equal to Abc1
        """
        Abc1
        """
        When checks if Abc1 is valid
        Then password Abc1 should not be valid

    Scenario: Check if 'Abc1&' is valid
        Given password parameter equal to Abc1&
        """
        Abc1&
        """        
        When checks if Abc1& is valid
        Then password Abc1& should not be valid

    Scenario: Check if 'Abc&' is valid

        Given password parameter equal to Abc&
        """
        Abc&
        """        
        When checks if Abc& is valid
        Then password Abc& should not be valid

    Scenario: Check if 'Abcdebfiewbfi1' is valid
        Given password parameter equal to Abcdebfiewbfi1
        """
        Abcdebfiewbfi1
        """        
        When checks if Abcdebfiewbfi1 is valid
        Then password Abcdebfiewbfi1 should not be valid

    Scenario: Check if 'njenvjewovoew&' is valid
        Given password parameter equal to njenvjewovoew&
        """
        njenvjewovoew&
        """
        When checks if njenvjewovoew& is valid
        Then password njenvjewovoew& should not be valid

    Scenario: Check if 'Abcvewjvewvwevev&1' is valid

        Given password parameter equal to Abcvewjvewvwevev&1
        """
        Abcvewjvewvwevev&1
        """        
        When checks if Abcvewjvewvwevev&1 is valid
        Then password Abcvewjvewvwevev&1 should be valid