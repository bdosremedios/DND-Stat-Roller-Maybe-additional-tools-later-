# coding: utf-8

"""

Created on Sat Mar 16 20:24:30 2019

@author: bdosremedios

"""

import matplotlib.pyplot as plt
import numpy as np


def rollmesomestats(nrolls=4, ndrops=1, dice_sides=6):
    """
    Rolls 6 stats for character creation in RPG. Defaults set at standard roll
    for DND 5th edition.

    Parameters
    ---

    nrolls : int
        Number of dice to roll per stat.

    ndrops : int
        Number of rolls to drop before determining stat score.

    dice_sides : int
        Number of sides of dice that is to be rolled.

    Raises
    ---

    AssertException
        If nrolls > ndrops stops, as can not drop more rolls than there are
        rolls.

    """

    # Check to make sure not dropping more than can be dropped
    assert nrolls >= ndrops, "Can not drop more than nrolls rolls"

    fig, loax = plt.subplots(6, nrolls+2, figsize=(6, nrolls+2))
    aoax = np.reshape(loax, (6, nrolls+2))

    # Rolls dice nrolls times for each row tracking ndrops lowest rolls
    rows_rolltup = []
    for i in range(6):  # 6 stats in dnd 5e
        rolls = [rolldice(dice_sides) for j in range(nrolls)]
        # Store ndrops lowest rolls in rolls
        lo_min_ind = []  # Stores all minimum indices
        temp = rolls[:]
        for i in range(ndrops):
            min_ind = np.argmin(temp)
            lo_min_ind.append(min_ind)
            temp[min_ind] = np.inf
        # Calculate total value with lowest ndrops rolls removed
        temp = np.array(rolls)
        temp[np.array([lo_min_ind])] = 0
        total = np.sum(temp)
        rows_rolltup.append((rolls, lo_min_ind, total))

    # Plot down each row, nroll roll numbers, an equals sign, the
    # resulting total stat number
    for i in range(6):
        loax = aoax[i]
        for ax in loax:
            ax.tick_params(axis="both", labelleft=False, labelbottom=False,
                           left=False, bottom=False)
        rolls, lo_min_ind, total = rows_rolltup[i]
        for ax, roll in zip(loax[0:nrolls], rolls):
            ax.text(0.5, 0.5, str(roll), va="center", ha="center", fontsize=20)
        for min_ind in lo_min_ind:
            loax[min_ind].plot(0.5, 0.5, "rx", markersize=60, mew=5)
        loax[nrolls].text(0.5, 0.5, "=", va="center", ha="center", fontsize=20)
        loax[nrolls+1].text(0.5, 0.5, str(total), va="center", ha="center",
                            fontsize=20)

    fig.suptitle("Pray to DND RNGesus", fontsize=20)
    plt.show()


def rolldice(sides):
    """
    Generates a random integer between 1 and sides inclusive.

    Parameters
    ---

    sides : int
        Number of sides for pseudo dice to have.

    Returns
    ---
    int
        Generated random int.

    """
    return int(np.random.random()*sides+1)
