Feature: Different Configurations
    Different Configurations should result in different hosts.

    Scenario: Basic Host
        Given Klaus configured a basic Host
        When the host is provisioned
        Then all basic services are running