reverse_auction_simulator:

About:
  This is a simulator for a reverse auction game given as a final project for my multivariable calculus class at UWT, winter 2017.
  
  The Original presentation slides can be viewed via this link, (although a improved version is included in this repo):
    https://docs.google.com/presentation/d/1KGYFGrlyrJpKpclDZX-Xrx-ttvs0ZhfU2wkSvF9oISc/edit?usp=sharing

Original problem and solution:
  rules:
    3 players each simulataniously pick a integer in the inclusive range [1, 3]. 
    The winner gets 1$ by having the lowest, unique number among the players.
    Nobody gets anything if there is no lowest, unique integer amongst the picked options.
    
  The problem:
    Give a mixed strategy, or a 3-tuple, that gives the probablity that each player picks each integer that maximizes each players payoff.
    
  The Solution:
    1): The players win 28.719% of the time, and thus gain $0.28719 on average each.
      This is for the mixed point (0.464, 0.268, 0.268), if shared by all three players.
        (x = 2√(3)-3~~ 0.464102, y =2-√(3)~~ 0.267949, 1-x-y= 2-√(3)) ==> (2√(3)-3, 2-√(3), 2-√(3)) ~~~ (0.464,0.268,0.268)
      (see linked presentation slide-set above for more detailed explaination.)

    2): This is nominally a zero-sum game in the sense that no player can have a non-worse case payoff 
      without every other player having a non-best case payoff. Dispite this, the players forced shared payoff causes them
      to have "work together" in merely minimizing the chances that they pick the same integer (13.843% of the time).
      
    3): Extending the problem was done in two ways:
      1): fixing 2 players mixed strategys to (1/3, 1/3, 1/3) and solving for the third players mixed strategy. This gave 
    
The presentation slides my group and I created and used for our presentation along with our sources:
  https://docs.google.com/presentation/d/1KGYFGrlyrJpKpclDZX-Xrx-ttvs0ZhfU2wkSvF9oISc/edit?usp=sharing

Help and Assistence:
  I did most of the research for the problem itself for finding and understanding the solution (from online sources) and understanding it.
  Alexander created the original python simulation (which this is a from-scratch recreation of).
  Damian Kim helped create much of the slides and graphs along with helping me digest the math and theory.
    
Citations and Readings:
  Xin Jiang, & Leyton-Brown, K. (2017). A Tutorial on the Proof of the Existence of Nash Equilibria. 
    (pp. 1-10, Tech. No. TR-2007-25 Albert Xin Jiang). Cambridge: Cambridge University Press.

  Costa-Gomes, M. A., & Shimoji, M. (2014). Theoretical approaches to lowest unique bid auctions. 
    Journal of Mathematical Economics, 52, 16-24. doi:10.1016/j.jmateco.2014.02.011

  Dionysius Glycopantis, “Nash Equilibria in Large Games,” 
    Game Theory, vol. 2014, Article ID 617596, 4 pages, 2014. doi:10.1155/2014/617596

  Talwalkar, Presh. 2012. “A unique lowest bid game.” 
    Mind Your Decisions. Retrieved December 6, 2017 (https://mindyourdecisions.com/blog/2012/05/29/a-unique-lowest-bid-game/).



