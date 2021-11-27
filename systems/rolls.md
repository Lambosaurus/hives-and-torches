## Advantage

Advantage is a an additional `+1d4` that is added to your roll. These are given due to advantageous circumstances that improve your odds of succeeding your task. Advantage may stack indefintely, and is the opposite of [disadvantage](#Disadvantage).

Advantage and disadvantage cancel out before rolling. Ie, if you have 1x advantage and 3x disadvantage, you would add `-2d4` to your roll.

Advantage and disadvantage can be applied to **any** roll, at the DM's discretion.

## Disadvantage

Disadvantage is a `-1d4` that is added to your roll. See [advantage](#Advantage) for information on stacking.

## Tests

Tests are a roll that your character makes against a foe to perform some kind of action. This is done by comparing one of your [attributes](stats.md#Attributes) against an atribute of your foes.

Your score is formed by rolling `2d6` plus your characters atribute score. Your foes score is '7' plus their attribute score (the average value of their attribute). If your score equals or exceeds your foes score, you succeed the test. [Advantage](#Advantage) may also be added to these rolls.

If the foes attribute is unspecified, ie, "A strength test", then the tested attributes are the same, ie, strength vs strength.

### Example: "Strength test against Agility"

Your character has a strength of `+2`, so they roll `2d6 + 2` and get a score of `8`. The foes agility is `+1`, so their score is `7 + 1`. Because these scores are equal, you succeed the test.


# Attacks

Your attack consists of a single roll, your attack score. Your attack score is derived based on your chosen weapon, see the [melee](#Melee-attack) and [ranged](#Ranged-attack) sections. This will usually be two weapon dice plus an attribute. Any [advantage](#Advantage) dice should be rolled together with these.

Once the dice are rolled, these should be checked for [criticals](rolls#Crititals). These enable additional modifiers to the attack if present.

If the attack score is greater than the foes [defence](stats.md#Defence) score, then the attack is a hit, and the damage dealt is the difference. The DM is not required to reveal the defence score of the foe, or whether an attack did any damage.

### Example 1:
A character with a long sword (`d8`) and +3 strength makes a melee attack against foe. He rolls `2d8 + 3` and gets a combat score of `13`. The foe has a defence of `4`, so the damage dealt is `13 - 4 = 9`. This 

### Example 2:
A character with a short bow (`d6`) and +1 agility makes a ranged attack against a foe. He rolls `2d6 + 1` and gets a combat score of `3`. The foe has a defence of `5`, so the attack is inneffective and no damage is dealt.

## Melee attack

A melee attack is an attack with a [melee weapon](weapons.md#Melee-weapons). The target foe must within your weapon reach. Weapon reach is `5ft` unless otherwise stated. The attack score of a melee attack is `2x` your weapons dice plus your [strength](attributes.md#Strength).

## Ranged attack

A ranged attack is an attack made with a [ranged weapon](weapons.md#Ranged-weapons). The attack score of a ranged attack is `2x` your weapons dice plus your [agility](attributes.md#Agility). A ranged attack is [unsafe](actions.md#Unsafe).

## Unarmed attack

It is possible to make an attack without a weapon. This is equivalent to a [melee attack](#Melee-attack), however your attack score is only `1d4` plus your [strength](attributes.md#Strength).


# Criticals

Any dice with a duplicate number are considered a critical. These include any [advantage](#Advantage) dice. Notice how a few advantage die significantly increase your odds of achieving critical effects, and many advantage die may even guarantee a critical. Stacking advantage to improve the odds of critical is a core mechanic to this ruleset.

On a critical, the character may select an applicable critical hit effect. All characters have [pierce defence](#Pierce-defence) as a critical effect option by default. Multiple critical effects may be selected for each pair of duplicates. Three of a kind count as two criticals, and so on.

If you have a [disadvantage](#Disadvantage) (That is, more disadvantages than advantages) you are **not elegable for criticals**. You may instead be elegible for [critical failures](#Critical-failure).

## Critical failure

Critical failures occurr when you roll a critical, but have [disadvantage](#Disadvantage). This event is usually ignored, but may be mentioned in specific rules or features.

## Pierce defence

This is a [critical](#Criticals) effect that all characters have access to by default. This allows you to ignore the foes [defence](stats.md#Defence) when calculating damage.

### Example 1:

A character performs an attack with a greatsword (`d10`) and `+4` strength. Because he is [flanking](statuses.md#Flanking) and the foe is [marked](statuses.md#Marked), he also has `2x` [advantage](#Advantage).

This means he rolls `2d10 + 4 + 2d4` for his attack score. His die are `8,3,3,2`. Because there are two `3`'s, he has rolled a critical. The character chooses to use this critical to [pierce defence](#Pierce-defence), ignoring the foes [defence](stats.md#Defence).

The target then takes the entire `20` damage.

### Example 2:

A character performs an attack with a hammer `d8`, and a strength of `+2`.

This means he rolls `2d8 + 2` for his attack score. His die are `2,2`. Because there are two `6`'s, he has rolled a critical.

Because his total damage score of `6`, and his foes [defence](stats.md#Defence) is `7`, this is not a hit. Becase his [stunning blow](feats.md#Stunning-blow) feat requires a hit, he may **not** use it. Instead, he will [pierce defence](#Pierce-defence), and deal `6` damage.

### Example 3:

A character performs an attack with a dagger `d4` and a agility of `+3`. Because he is [hidden](statuses.md#Hidden) and [flanking](statuses.md#Flanking) he as `2x` [advantage](#Advantage).

This means he rolls `4d4 + 3` for his attack score. His die are `1,1,1,3`. This is a double critical, and he may have two critical effects. He chooses to both [pierce defence](#Pierce-defence) and [twist the knife](feats.md#Twist-the-knife) for a bonus `1d8`.

Rolling `6` for twist the knife, `15` damage is dealt in total.

### Example 4

A character performs an attack with a shortsword `d6` and a strength of `+1`. Because his foe is [in cover](statuses.md#In-cover), he is rolling with [disadvantage](#Disadvantage).

He rolls `6,6,-2`, for a total of `11` damage. Due to his disadvantage, this is not a [critical failure](#Critical-failure). Because there are no features active that are triggered from a critical falure, this is ignored.

Once the foes [defence](stats.md#Defence) of `3` is accounted for `9` damage is dealt in total.