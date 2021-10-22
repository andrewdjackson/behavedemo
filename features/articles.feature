@api
Feature: User can manage articles

        Scenario: List all articles
            Given the article service
             When a list of all articles is requested
             Then the list of articles is returned

        Scenario Outline: List single article
            Given the article id is "<article_id>"
             When a single article is requested
             Then the requested article is returned

        Examples:
                  | article_id |
                  | 1          |
                  | 2          |

        Scenario: Invalid single article request
            Given the article service
              And the article id is "900"
             When a single article is requested
             Then the status code "404" returned

        Scenario: Create a new article
            Given the article service
             When the user creates a new article with the id "3"
              And a single article is requested
             Then the requested article is returned

        Scenario: Delete an article
            Given the article service
              And the user creates a new article with the id "3"
             When the user deletes the article with the id "3"
             Then the requested article is not found
