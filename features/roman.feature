Feature: Roman Numbers
    This project converts arabic/decimal numbers to roman numbers.

    Scenario: Convert 1 to I
        Given decimal number equal to 1
        When roman symbol I is taken from set
        Then roman number should be I

    Scenario: Convert 4 to IV
        Given decimal number equal to 4
        When roman symbols I and V are taken from set
        Then roman number should be IV

    Scenario: Convert 29 to XXIX
        Given decimal number equal to 29
        When roman symbols three X and I are taken from set
        Then roman number should be XXIX

    Scenario: Convert 233 to CCXXXIII
        Given decimal number equal to 233
        When roman symbols two C three X and three I are taken from set
        Then roman number should be CCXXXIII
    
    Scenario: Convert 959 to CMLIX
        Given decimal number equal to 959
        When roman symbols C, M, L, I and X are taken from set
        Then roman number should be CMLIX

    Scenario: Convert 1527 to MDXXVII
        Given decimal number equal to 1527
        When roman symbols M, D, two X, V and two I are taken from set
        Then roman number should be MDXXVII

    Scenario: Convert 999 to CMXCIX
        Given decimal number equal to 999
        When roman symbols two C, M, two X and I are taken from set
        Then roman number should be CMXCIX
    