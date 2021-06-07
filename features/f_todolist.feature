# encoding: utf-8
# language: en

Feature: Todolists management workflow
	Background:
		Given I access my application on browser
		When I click on Entrar button
		And Log in with "xileyaf341@relumyx.com" account and "Ktask@123" password
		Given I see my homepage
	
	Scenario: Creating a project
		When I create a project with the following data
		|Name 				|Value 						| 
		|nome				|exemplo todolist			|
		|desc				|testando com selenium		|
		|data				|16072021					|

		Then there must be a project called "exemplo todolist"
		Then I logout

	Scenario: Creating a project with error	
		When I create a project with the following data
		|Name 				|Value		| 
		|nome				|			|
		|desc				|			|
		|data				|			|

		Then I see a error message with "Preencha o campo." on "create" modal
		Then I logout

	Scenario: Creating a project with past date
		When I create a project with the following data
		|Name 				|Value		| 
		|nome				|foll		|
		|desc				|fool		|
		|data				|04052021	|
		Then I see a error message with "Preencha todos os campos e coloque uma data válida!" on "create" modal
		Then I logout

	Scenario: Editing a project
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
		Then I click to edit project called "exemplo todolist - Updated"
		And I should see the project edition modal
		And I edit the project with the following data	
		|Name 				|Value 						| 
		|name				|							|
		|desc				|							|
		|data				|15032020					|
		Then I see a error message with "Coloque uma data válida!" on "edit" modal
		Then I logout
	
	Scenario: Managing todolist access
		Then I add user "vh141299@gmail.com" to the project
		Then I logout

	Scenario: Adding a wrong email to the project
		Then I add user "vh141299" to the project
		Then I logout

	Scenario: Removing user from project
		Then I remove user "vh141299@gmail.com" from project"
		Then I logout
