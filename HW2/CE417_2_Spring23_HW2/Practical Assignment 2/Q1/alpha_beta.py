from Board import BoardUtility
def minimax(board, player_piece, depth, is_maximizing_player, alpha, beta):
    """
    This function run alpha beta puring algorithm and return best next move
    :param board: game board
    :param player_piece: number of player. 1 or 2
    :param depth: depth of tree
    :param is_maximizing_player: True if you are in a max node otherwise False
    :param alpha: value of alpha
    :param beta: value of beta
    :return best_value, best_move: You have to return best next move and its value
    """
    if depth == 0 or BoardUtility.is_terminal_state(board):
        return BoardUtility.score_position(board,player_piece), None

    if is_maximizing_player:
        value = float("-inf")
        best_move = None
        for move in BoardUtility.get_valid_locations(game_board=board):
            BoardUtility.make_move(game_board=board, row = move[0],col = move[1],player = player_piece)
            score, _ = minimax(board = board,player_piece = player_piece, depth = depth - 1, alpha = alpha, beta = beta, is_maximizing_player = False)
            if score > value:
                value = score
                best_move = move
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value, best_move

    else:
        value = float("inf")
        best_move = None
        for move in BoardUtility.get_valid_locations(game_board=board):
            BoardUtility.make_move(game_board=board, row = move[0],col = move[1],player = player_piece)
            score, _ = minimax(board = board, player_piece = player_piece, depth = depth - 1, alpha = alpha, beta = beta,is_maximizing_player = True)
            if score < value:
                value = score
                best_move = move
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value, best_move
    



def minimax_prob(board, our_piece, enemy_piece, depth, is_maximizing_player, alpha, beta, prob):
    """
    This function run alpha beta puring algorithm and return best next move
    :param board: game board
    :param player_piece: number of player. 1 or 2
    :param depth: depth of tree
    :param is_maximizing_player: True if you are in a max node otherwise False
    :param alpha: value of alpha
    :param beta: value of beta
    :param prob: probability of choosing a random action in each max node
    :return best_value, best_move: You have to return best next move and its value
    """
    if depth == 0 or BoardUtility.is_terminal_state(board):
        return BoardUtility.score_position(board,player_piece), None

    if is_maximizing_player:
        value = float("-inf")
        best_move = None
        for move in BoardUtility.get_valid_locations():
            child_node = BoardUtility.make_move(game_board=board, row = move[0],col = move[1],player = player_piece)
            score, _ = minimax(board = board,player_piece = child_node, depth = depth - 1, alpha = alpha, beta = beta, is_maximizing_player = False)
            if score > value:
                value = score
                best_move = move
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value, best_move

    else:
        value = float("inf")
        best_move = None
        for move in BoardUtility.get_valid_locations():
            child_node = BoardUtility.make_move(game_board=board, row = move[0],col = move[1],player = player_piece)
            score, _ = minimax(board = board, player_piece = child_node, depth = depth - 1, alpha = alpha, beta = beta,is_maximizing_player = True)
            if score < value:
                value = score
                best_move = move
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value, best_move
    pass
