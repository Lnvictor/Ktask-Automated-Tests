# encoding: utf-8
# language: en

Feature: Testing Feature configuration
	Background:
		Given I access my application on browser
		When I click on Entrar button
		And Log in with "xileyaf341@relumyx.com" account and "Ktask@123" password
	
	Scenario: Creating a project
		Given I see my homepage
		And I create a project with the following data
		|Name 				|Value 						| 
		|nome				|exemplo todolist			|
		|desc				|testando com selenium		|
		|data				|16032021					|

		Then there must be a project called "exemplo todolist"
		Then I logout

	Scenario: Creating a project with error	
		Given I see my homepage
		And I create a project with the following data
		|Name 				|Value		| 
		|nome				|			|
		|desc				|			|
		|data				|			|

		Then I see a error message with "Preencha o campo."
		Then I logout

	Scenario: Editing a project
		Given I see my homepage
		Then I click to edit project called "exemplo todolist"
		And I should see the project edition modal
		And I edit the project with the following data
		|Name 				|Value 						| 
		|name				|exemplo todolist - Updated	|
		|desc				|testando com selenium 		|
		|data				|18032021					|
		Then there must be a project called "exemplo todolist - Updated"
		Then I logout

	Scenario: Editing a project with error
		Given I see my homepage
		Then I click to edit project called "exemplo todolist - Updated"
		And I should see the project edition modal
		And I edit the project with the following data
		|Name 				|Value 						| 
		|name				|							|
		|desc				|							|
		|data				|							|
		Then I see a error message with "Você não alterou nenhum campo, altere pelo menos 1 campo!"
		Then I logout
