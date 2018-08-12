Team name: Bamboo

Working hours:
	son	10		actual: 22
	truc	10 		actual: 16

Check-in(= how often you update each other on your progress): Every 1-hour

Strengths and weaknesses: 
	son	
		Strength	Logic, bug fix, code
		Weakness	Stamina		
	truc	
		Strength	case study, logic, problem solving
		Weakness	
Workload:
	son	50%
	truc	50%

Strategy:
	Find Othello code
	Try to understand 
	Make our code
	Explan codebase every check-in
	Updating progress every check-in
	Updating prgress at the end of day
	


Task: (OK, NOK)
	Team agreement + check tasks				OK
	Display board 						OK
		create board					OK
		print board 					OK
	Possible moves algorithm 				OK
	Player move			 			OK
		input handling					OK
		is player move valid?				OK
		place token on that move			OK
		flip						OK
	Error handling 						OK
		Invalid choice: exit game			OK
	When a player cannot play 				OK
		is player has valid move?			OK
		Pass to other player 				OK
		is other has valid move?			OK
		print valid move				OK
			sort alphabet				OK
	End condition: both players cannot play anymore 	OK
	Count score						OK
	Loop the game						OK
	Odd case						OK
	Fix bug							NOK
		EOF						OK
		print valid choice				OK
		\n						NOK
		...
	Sentinal						NOK
	
	

Progress:
Begin:
	son	display board, team agreement
	truc	algorithm for possible moves

1st check-in
	son	count score
	truc 	algorithm for possible moves

2nd check-in
	son	algorithm -> code + update progress
	truc	input handling + isValidmove

Stop check-in -> work together
		Loop the game
		input handling		
			Odd case: input is > 2, input != format		
		is player move valid?				
		place token on that move			
		flip
		has valid move
		Pass
		print current board + valid move
		end condition
		add 'alphabet' + 'num' to table	
		Fix bug: EOF, \n, call func to print(func), validchoice, fix input,...
		End project	


