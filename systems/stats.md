
# Level
[This section is a stub. Submit a Pull Request to edit it](https://github.com/Lambosaurus/hives-and-torches/edit/main/systems/stats.md)

# Attributes
These attributes are intrinsic to your character. They represent the base capabilities of your body and mind. These will only change rarely throughout a characters journey.

These are all recorded as a numeric modifier. An attribute of `0` represents an unexceptional value that a non-adventuring citizen might have.

There are four attributes:
 - [Strength](#strength)
 - [Finesse](#finesse)
 - [Intellect](#intellect)
 - [Will](#will)

## Strength
Strength is sum of a characters physique and size.
Strength represents a characters capacity to perform physical activities including fighting in melee, moving heavy objects, breaking stuff etc.  Strength is the primary stat for melee combat

Strength is primarially used for [melee attacks](rolls.md#melee-attack) and [encumbrance](#encumbrance).

## Finesse
A character with finesse is capable of both quick and precice actions.
Finesse represents a characters level of poise, balance and coordination and is used for ranged attacks and acrobatic type non combat activities.  Finesse is the primary stat for Ranged combat

Finesse is used for primarially [ranged attacks](rolls.md#ranged-attack), [defence](#defence), and stealth.

## Intellect
The ability to problem solve, and accurately percieve the world around them.
Intelligence represents a characters knowledge and wisdom into a particular subject and will be used for inspection tests, investigation tests and as a primary stat for arcane magic

Intellect is primarially used for [arcane magic](spells.md#arcane-magic) 

## Will
Will represents the determination and personal confidence a character possesses, and is used for protecting against morale checks, contesting willpower and mind altering abilities.  Will is the primary stat for Miracle casting

Will is primarially used for [divine magic](spells.md#divine-magic)

# Properties

## Defence
Defence represents how capable a character is at protecting themselves from foes. This might be using quick footwork or heavy armor plating.

Base defence is [finesse](#finesse) plus the bonuses of any worn [armor](items.md#armor).
- Wearing [heavy armor](items.md#armor) removes your [finesse](#finesse) bonus.
- Defence may never be negative.

## Fatigue
Fatigue represents the wear and tear your character takes over the course of their adventure. Scrapes, bruises, aching muscles, and general exhaustion: these build up until the character is too tired to protect themselves from foes and the environment.

Your maximum fatigue is based on [strength](#strength). If this characters strength modifier is negative, do **not** add strength.

 - At [level](#level) `1`, the base fatigue is `4 + 1d4` plus [strength](#strength)
 - Maximum fatigue increases by `1d4` plus [strength](#strength) on each subsequent level.

The DM may choose to allow players to reroll `1`'s when rolling to add maximum fatigue.

## Speed
[This section is a stub. Submit a Pull Request to edit it](https://github.com/Lambosaurus/hives-and-torches/edit/main/systems/stats.md)

## Encumbrance
[This section is a stub. Submit a Pull Request to edit it](https://github.com/Lambosaurus/hives-and-torches/edit/main/systems/stats.md)

## Size
[This section is a stub. Submit a Pull Request to edit it](https://github.com/Lambosaurus/hives-and-torches/edit/main/systems/stats.md)


# Health and wounds 
 
## Damage 
Damage is the number dealt to a character due to an [attack](rolls.md#attacks) or other effect after [defence](#defence) is considered. 
 
Damage is dealt to a character in the following order:
 1. The damage is subtracted from your [fatigue](#fatigue). If there is any remaining damage, it overflows to step 2.
 2. Damage dealt at `0` fatigue is dealt as a single [wound](#wounds).

> ### Example 1
> A character with `11` [fatigue](#fatigue) recieves `4` damage, leaving him on `7` fatigue.
> All the damage is dealt to his fatigue, so he does not take a [wound](#wounds).

> ### Example 2
> A character with `3` [fatigue](#fatigue) recieves `6` damage. This leaves him with `0` fatigue and still with damage remaining. This causes him to take a [wound](#wounds). Because he still has `2` wounds remaining, he continues fighting.

## Wounds

Characters have a set number of wound slots. For [medium](#size) players this number is `3`. These wounds can individually be in one of three states.
 - Free
 - Wounded
 - Mortally wounded

When you take a wound, one of your free slots becomes wounded. Wounds are difficult to remove - and require special magics or healing items.

When a character has no free wounds remaining, they will [black out](#black-out).

If additional wounds are dealt when no free wounds remain, then a wound is instead upgraded to a [mortal wound](#mortal-wounds). When all wound slots are filled with [mortal wounds](#mortal-wounds), then the character is [dead](statuses.md#dead).

## Black out

When no wounds are available, a character will become [unconscious](statuses.md#unconscious). Unconsciousness persists until a point of [fatigue](stats.md#fatigue) is restored. Once blacked out, a player character is likely to be ignored by foes while other targets remain.

A player character may choose to [press on](#press-on) and stay conscious instead of blacking out.

## Press on

Instead of blacking out, a character may press on. Gritting their teeth to ignore the pain and hold their focus, they make a final stand against their foes.

When a character chooses to press on:
 - They be given the opportunity to [black out](#black-out) only when they take another wound.
 - They will remain a priority target for foes.

> ### Example 1
> A character with `0` [fatigue](#fatigue) and `2` wounds takes [damage](#damage). This causes the `3`rd [wound](#wounds), leaving `0` free wounds remaining. The character [blacks out](#black-out) and remains [unconscious](statuses.md#unconscious).
>
> In the following turn, this character recovers `3` points of [fatigue](#fatigue) due to a [spell](spells.md). On his next turn, he stands up and takes his turn as normal. He remains on `3` wounds however.

> ### Example 2
> A character with `2` wounds takes his `3`rd. The player chooses to [press on](#press-on), and remains standing.
>
> In a following turn, a foe deals an additional [wound](#wounds).
> Because the character has no free wounds, one wound becomes a [mortal wound](#mortal-wounds). The character has another opportunity to [black out](#black-out), and chooses to do so.

## Mortal wounds
 
A mortal wound reflects a life threatening wound to the character. This cannot be easily treated, and will negatively affect the character.

When a mortal wound is gained, they recieve an effect from the [wound table](#wound-table). This may be selected by rolling, or at the DM's discretion.

A mortal wound cannot be removed trivially. They DM may select some of these options for removing wounds:
 - Days or weeks of care in town to let your wounds heal
 - Paying for the services of an expert healer
 - Requiring the player to go on a small side quest
 - Making it a permanent wound as a reminder of the players hubris

When a mortal wound is healed, it may not be 'good as new'. Scar tissue or missing digits could still remain. The worst of the trauma has healed, and the character has learned to make do with the body they have.

> ### Example
> Upon taking a [wound](#wounds) while already on `3` wounds, and character is given a mortal wound from the [wound table](#wound-table). The DM elects to give him the "fractured bone" wound, causing the player be to permanently [crippled](statuses.md#crippled).
> 
> This condition remains with the character for the remainder of the quest until they return to their hometown. After several days of expert care in the towns temple, the mortal wound is eventually cured.

## Wound Table

| Number | Name           |Effect                                                                                                 |
|--------|----------------|-------------------------------------------------------------------------------------------------------|
|      1 | Fracture       | The character is permanently [crippled](statuses.md#crippled).|
|      2 | Concussed      | The character is permanently [dazed](statuses.md#dazed) and [stunned](statuses.md#stunned).|
|      3 | Infected       | The character is permanently [blighted](statuses.md#blighted).|
|      4 | Internal bleeding | The character is permanently [weakened](statuses.md#weakened).|
|      5 | The shakes     | The character is permanently [vulnerable](statuses.md#vulnerable)|
|      6 | Ruined hand    | Loose the use of one hand.|
|      7 | Disfigured     | [Disadvantage](rolls.md#disadvantage) on [diplomacy](skills.md#diplomacy) tests (At the DM's discretion).|
|      8 | Weeping wounds | When [resting](#resting), make a [medicine](skills.md#medicine) test. On a failure, you may not recover the usual [fatigue](stats.md#fatigue).|
|      9 | The stare      | On combat initiative, make a [will](stats.md#will). On a failure, you make not make any [action](actions.md#actions) on the first round. You may still hold 1 [reaction](actions.md#reactions). |
|     10 | Blurred vision | [Disadvantage](rolls.md#disadvantage) when [attacking](rolls.md#attacks) foes further than `5ft`. [Disadvantage](rolls.md#disadvantage) on [observation](skills.md#observation). |
|     12 | Frostbite      | [Movement](stats.md#speed) is reduced by `10ft`. `-1` on all [attack](rolls.md#attacks) rolls.|
|     12 | Broken rib     | Max [fatigue](stats.md#fatigue) is reduced by `1d4` + your [level](stats.md#level).|
|     13 | Bloody cough   | [Disadvantage](rolls.md#disadvantage) on [stealth](skills.md#stealth) and [strength](stats.md#strength) tests.|
|     14 | Large burns    | Foes gain [advantage](rolls.md#advantage) when attacking in melee.|


# Resting
[This section is a stub. Submit a Pull Request to edit it.](https://github.com/Lambosaurus/hives-and-torches/edit/main/systems/stats.md)

# Camping