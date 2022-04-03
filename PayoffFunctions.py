def prisonersDilemma(s1,s2):
	
	# T = Temptation, R = Reward, L = Loner's (only when abstention is an option), P = Punishment, S = Sucker
	T = 2
	R = 1
	L = 0
	P = -1
	S = -2
	
	
	if (s1 == "cooperate") and (s2 == "cooperate"):
		payoff1 = payoff2 = R	
		
	if (s1 == "cooperate") and (s2 == "defect"):
		payoff1 = S
		payoff2 = T
		
	if (s1 == "defect") and (s2 == "cooperate"):
		payoff1 = T
		payoff2 = S
		
	if (s1 == "defect") and (s2 == "defect"):
		payoff1 = payoff2 = P
		
	return payoff1, payoff2