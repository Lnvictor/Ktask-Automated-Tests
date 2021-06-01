# encoding: utf-8
#language: en

Feature: Testing Feature configuration
	Background:
		Given I access my application on browser
		When I click on Entrar button
		And Log in with "xileyaf341@relumyx.com" account and "Ktask@123" password
	
	Scenario: Verifying Homepage
		Then devo estar logado
		And crio um todolist com os dados
		|Name 				|Value 					| 
		|nome				|exemplo todolist			|
		|desc				|testando com selenium		|
		|data				|16032021					|
