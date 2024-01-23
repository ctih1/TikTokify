

def hard_round(number: float) -> int:
    """_summary_

    Args:
        number (float): the number to process

    Returns:
        int: number without decimals.
    """
    return int(str(number).split(".")[0])