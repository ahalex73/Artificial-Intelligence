
Alexander Holmes
4/5/2024
AI research - How Ai's play chess

Creating Chess AI using chess python library


REFERENCES: 
    https://www.freecodecamp.org/news/simple-chess-ai-step-by-step-1d55a9266977/ 
    https://en.wikipedia.org/wiki/Minimax

The basis of every chess ai:
    - move-generation
        - gathering a list of all possible moves of all pieces present

    - board evaluation
        - evaluation the value of each piece granted its position and moveset

    - minimax - algorithm for searching the tree of possibilities
          "Minmax (sometimes Minimax, MM[1] or saddle point[2]) is a decision rule used in artificial intelligence, 
          decision theory, game theory, statistics, and philosophy for minimizing the possible loss for a worst case (maximum loss) scenario " - wikipedia
        
        In this algorithm, the recursive tree of all possible moves is explored to a given depth, and the position is evaluated
         at the ending “leaves” of the tree.

        After that, we return either the smallest or the largest value of the child to the parent node, 
        depending on whether it’s a white or black to move. (That is, we try to either minimize or maximize the outcome at each level.)


    - alpha beta pruning - Optimization method
        - Alpha-beta pruning is an optimization method to the minimax algorithm that allows us to disregard some branches in the search tree. 
        This helps us evaluate the minimax search tree much deeper, while using the same resources.

        - The alpha-beta pruning is based on the situation where we can stop evaluating a part of the search tree if we find a move that leads to a 
        worse situation than a previously discovered move.

        - The alpha-beta pruning does not influence the outcome of the minimax algorithm — it only makes it faster.

        - The alpha-beta algorithm also is more efficient if we happen to visit first those paths that lead to good moves.


Forsyth-Edwards-Notation (FEN)
“p" - pawn "r" for rook, "n" for knight, "b" for bishop, "q" for queen, and "k" for king. 
The same letters are used for the white pieces, but they appear in uppercase.

Algebraic Notation (SAN) - https://en.wikipedia.org/wiki/Algebraic_notation_(chess)
For most moves the SAN consists of 
    the letter abbreviation for the piece
    an x if there is a capture
    and the two-character algebraic name of the final square the piece moved to

    Example:
    1. e4 e5    
    2. Nf3 Nc6 
    3. Bb5 {This opening is called the Ruy Lopez.} 3... a6
    4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3 O-O 9. h3 Nb8 10. d4 Nbd7
    11. c4 c6 12. cxb5 axb5 13. Nc3 Bb7 14. Bg5 b4 15. Nb1 h6 16. Bh4 c5 17. dxe5
    Nxe4 18. Bxe7 Qxe7 19. exd6 Qf6 20. Nbd2 Nxd6 21. Nc4 Nxc4 22. Bxc4 Nb6
    23. Ne5 Rae8 24. Bxf7+ Rxf7 25. Nxf7 Rxe1+ 26. Qxe1 Kxf7 27. Qe3 Qg5 28. Qxg5
    hxg5 29. b3 Ke6 30. a3 Kd6 31. axb4 cxb4 32. Ra5 Nd5 33. f3 Bc8 34. Kf2 Bf5
    35. Ra7 g6 36. Ra6+ Kc5 37. Ke1 Nf4 38. g3 Nxh3 39. Kd2 Kb5 40. Rd6 Kc5 41. Ra6
    Nf2 42. g4 Bd3 43. Re6 1/2-1/2
    

    SAN kingside castling is indicated by the sequence O-O
    queenside castling is indicated by the sequence O-O-O

    Pawn promotions are notated by appending = to the destination square, followed by the piece the pawn is promoted to. 
    For example: e8=Q. If the move is a checking move, + is also appended
    if the move is a checkmating move, # is appended instead. For example: e8=Q# 

    
Other chess engines use different methods of hashing out the board. Here is a
wiki page on Zobrist Hashing - https://en.wikipedia.org/wiki/Zobrist_hashing