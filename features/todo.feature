# encoding: utf-8
# language: en

Feature: Todo management workflow

    Background: 
        Given I access my application on browser
		When I click on Entrar button
		And Log in with "xileyaf341@relumyx.com" account and "Ktask@123" password
		Given I see my homepage
        And I click on viewTodos

    Scenario: Create todo
        Then Click on create todo button
        And I create a todo with the following data
        |Name 				|Value 						| 
        |nome				|exemplo todo   			|
		|desc				|testando com selenium		|
		|data				|16072021					|
        Then the "exemplo todo" todo should be exists on " A fazer" session
        Then I logout

    Scenario: Create Todo with error
        Then Click on create todo button
        And I create a todo with the following data
        |Name 				|Value 						| 
        |nome				|  			                |
		|desc				|                    		|
		|data				|       					|
        Then I see a error message with "Preencha o campo." on "createTodo" modal
        Then I logout

