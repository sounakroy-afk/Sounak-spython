import numpy as np

rng = np.random.default_rng(seed=1)
dice_rolls = rng.integers(low=1, high=7, size=(3, 3))
print(dice_rolls)
print(dice_rolls.shape)
print(dice_rolls.ndim)
print(np.sum(dice_rolls, axis=1))
print(np.where(dice_rolls == 6, 0, dice_rolls))
print(dice_rolls == 6)
items = ["Coins", "Gems", "Shield", "Sword", "Potion"]
rng.shuffle(items)
print(items)
