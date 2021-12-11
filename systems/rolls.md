# Advantage

Advantage is a an additional `+1d4` that is added to your roll. These are given due to advantageous circumstances that improve your odds of succeeding your task. Advantage may stack indefintely, and is the opposite of [disadvantage](#disadvantage).

Advantage and disadvantage cancel out before rolling. Ie, if you have `1x` advantage and `3x` disadvantage, you would add `-2d4` to your roll.

Advantage and disadvantage can be applied to **any** roll at the DM's discretion.

## Disadvantage

Disadvantage is a `-1d4` that is added to your roll. See [advantage](#advantage) for information on stacking.

# Tests

Tests are a roll that your character makes against a foe to perform some kind of action. This is done by comparing one of your [attributes](stats.md#attributes) against an atribute of your foes.

Your score is formed by rolling `2d6` plus your characters atribute score. Your foes score is `7` plus their attribute score (the average value of their attribute). If your score equals or exceeds your foes score, you succeed the test. [Advantage](#advantage) may also be added to these rolls.

If the foes attribute is unspecified, ie, "A strength test", then the tested attributes are the same, ie, [strength](stats.md#strength) vs strength.

> ### Example: "Strength test against Finesse"
> Your character has a [strength](stats.md#strength) of `+2`, so they roll `2d6 + 2` and get a score of `8`. The foes [finesse](stats.md#finesse) is `+1`, so their score is `7 + 1`. Because these scores are equal, you succeed the test.

# Attacks

Your attack consists of a single roll, your attack score. Your attack score is derived based on your chosen weapon, see the [melee](#melee-attack) and [ranged](#ranged-attack) sections. This will usually be two weapon dice plus an attribute. Any [advantage](#advantage) dice should be rolled together with these.

Once the dice are rolled, these should be checked for [criticals](#criticals). These enable additional modifiers to the attack if present.

If the attack score is greater than the foes [defence](stats.md#defence) score, then the attack is a hit, and the damage dealt is the difference. The DM is not required to reveal the defence score of the foe, or whether an attack did any damage.

> ### Example 1:
> A character with a long sword (`d8`) and +3 [strength](stats.md#strength) makes a melee attack against foe. He rolls `2d8 + 3` and gets a combat score of `13`. The foe has a defence of `4`, so the damage dealt is `13 - 4 = 9`.

> ### Example 2:
> A character with a short bow (`d6`) and +1 [finesse](stats.md#finesse) makes a ranged attack against a foe. He rolls `2d6 + 1` and gets a combat score of `3`. The foe has a defence of `5`, so the attack is inneffective and no damage is dealt.

## Melee attack

A melee attack is an [attack](#attacks) with a [melee weapon](weapons.md#melee-weapons). The target foe must within your [weapon reach](weapons.md#weapon-reach). Weapon reach is `5ft` unless otherwise stated. The attack score of a melee attack is `2x` your weapons dice plus your [strength](stats.md#strength).

## Ranged attack

A ranged attack is an [attack](#attacks) made with a [ranged weapon](weapons.md#ranged-weapons). The target foe must be within your [weapon range](weapons.md#weapon-range). The attack score of a ranged attack is `2x` your weapons dice plus your [finesse](stats.md#finesse). A ranged attack is [unsafe](actions.md#unsafe-action).

## Unarmed attack

It is possible to make an attack without a weapon. This is equivalent to a [melee attack](#melee-attack), however your attack score is only `1d4` plus your [strength](stats.md#strength).


# Criticals

Any dice with a duplicate number are considered a critical. These include any [advantage](#advantage) dice. Notice how a few advantage die significantly increase your odds of achieving critical effects, and many advantage die may even guarantee a critical. Stacking advantage to improve the odds of critical is a core mechanic to this ruleset.

On a critical, the character may select an applicable critical hit effect. All characters have [pierce defence](#pierce-defence) as a critical effect option by default. Multiple critical effects may be selected for each pair of duplicates. Three of a kind count as two criticals, and so on.

If you have a [disadvantage](#disadvantage) (That is, more disadvantages than advantages) you are **not elegable for criticals**. You may instead be elegible for [critical failures](#critical-failure).

## Critical failure

Critical failures occurr when you roll a critical, but have [disadvantage](#disadvantage). This event is usually ignored, but may be mentioned in specific rules or features.

## Pierce defence

This is a [critical](#criticals) effect that all characters have access to by default. This allows you to ignore the foes [defence](stats.md#defence) when calculating damage.

> ### Example 1:
>
> A character performs an attack with a greatsword (`d10`) and `+4` [strength](stats.md#strength). Because he is [flanking](statuses.md#flanking) and the foe is [marked](statuses.md#marked), he also has `2x` [advantage](#advantage).
>
> This means he rolls `2d10 + 4 + 2d4` for his attack score. His die are `8,3,3,2`. Because there are two `3`'s, he has rolled a critical. The character chooses to use this critical to [pierce defence](#pierce-defence), ignoring the foes [defence](stats.md#defence).
>
> The target then takes the entire `20` damage.

> ### Example 2:
>
> A character performs an attack with a hammer `d8`, and a [strength](stats.md#strength) of `+2`.
>
> This means he rolls `2d8 + 2` for his attack score. His die are `2,2`. Because there are two `6`'s, he has rolled a critical.
>
> Because his total damage score of `6`, and his foes [defence](stats.md#defence) is `7`, this is not a hit. Becase his [stunning blow](feats.md#stunning-blow) feat requires a hit, he may **not** use it. Instead, he will [pierce defence](#pierce-defence), and deal `6` damage.

> ### Example 3:
>
> A character performs an attack with a dagger `d4` and a [finesse](stats.md#finesse) of `+3`. Because he is [hidden](statuses.md#hidden) and [flanking](statuses.md#flanking) he has `2x` [advantage](#advantage).
>
> This means he rolls `4d4 + 3` for his attack score. His die are `1,1,1,3`. This is a double critical, and he may have two critical effects. He chooses to both [pierce defence](#pierce-defence) and [twist the knife](feats.md#twist-the-knife) to inflict an additional `4` damage.
>
> `13` damage is dealt in total.

> ### Example 4
>
> A character performs an attack with a shortsword `d6` and a [strength](stats.md#strength) of `+1`. Because his foe is [in cover](statuses.md#in-cover), he is rolling with [disadvantage](#disadvantage).
>
> He rolls `6,6,-2`, for a total of `11` damage. Due to his disadvantage, this is a [critical failure](#critical-failure). Because there are no features active that are triggered from a critical failure, this is ignored.
>
> Once the foes [defence](stats.md#defence) of `3` is accounted for `8` damage is dealt in total.

