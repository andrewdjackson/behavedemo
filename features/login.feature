Feature: User can login via the website

        @selenium
        Scenario Outline: User can login to the website with valid credentials
            Given the user is on the login page
              And the username "<username>"
              And the password "<password>"
             When the user logs in
             Then the user has logged in with "<result>"

        Examples:
                  | username | password | result  |
                  | user1    | pass1    | success |
                  | user1    | invalid  | failed  |
                  | user2    | pass2    | success |
                  | user3    | pass3    | failed  |


        @headless
        Scenario Outline: User can login to the website with valid credentials
            Given the username "<username>"
              And the password "<password>"
             When the login form is submitted
             Then the user has logged in with the status code "<status_code>"

        Examples:
                  | username | password | status_code |
                  | user1    | pass1    | 200         |
                  | user2    | pass2    | 200         |