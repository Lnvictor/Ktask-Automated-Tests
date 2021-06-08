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
        Then the "exemplo todo" todo should be exists on "A fazer" session
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

	Scenario: Edit todo
		Then Click to edit todo
        And I edit the "todo" with the following data	
		|Name 				|Value 						| 
		|name				|todo-Updated	    		|
		|desc				|updated					|
		|data				|15082021					|
        Then the "todo-Updated" todo should be exists on " A fazer" session
        Then I logout

    Scenario: Edit todo with past date
        Then CLick to edit todo
        And I edit the "todo" with the following data
        |Name 				|Value 						| 
		|name				|todo-Updated	    		|
		|desc				|updated					|
		|data				|15082020					|
        Then I see a error message with "Coloque uma data válida" on "editTodo" modal
        Then I logout

    Scenario: Changing status
        Then I change status to "Em andamento"
        Then the "todo-Updated" todo should be exists on "Em andamento" session
        Then I change status to "Concluido"
        Then the "todo-Updated" todo should be exists on "Concluido" session
        Then I logout