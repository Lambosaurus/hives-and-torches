
## Defence
Defence represents how capable a character is at protecting themselves from foes. This might be using quick footwork or heavy armor plating.

Base defence is [finesse](#Finesse) plus the bonuses of any worn [armor](items.md#Armor).
- Wearing [heavy armor](items.md#Heavy-armor) removes your [finesse](#Finesse) bonus.
- Defence may never be negative.

## Fatigue
Fatigue represents the wear and tear your character takes over the course of their adventure. Scrapes, bruises, aching muscles, and general exhaustion: these build up until the character is too tired to protect themselves from foes and the environment.

Your maximum fatigue is based on [strength](#Strength). If this characters strength modifier is negative, do **not** add strength.

 - At [level](#Level) `1`, the base fatigue is `4 + 1d4` plus [strength](#Strength)
 - Maximum fatigue increases by `1d4` plus [strength](#Strength) on each subsequent level.

The DM may choose to allow players to reroll `1`'s when rolling to add maximum fatigue.

# Health and wounds 
 
## Damage 
Damage is the number dealt to a character due to an [attack](rolls.md#Attack) or other effect after [defence](#Defence) is considered. 
 
Damage is dealt to a character in the following order:
 1. The damage is subtracted from your [fatigue](#Fatigue). If there is any remaining damage, it overflows to step 2.
 2. Damage dealt at `0` fatigue is dealt as a single [wound](#Wounds).

## Wounds

Characters have a set number of wound slots. For [medium](#Size) players this number is `3`. These wounds can individually be in one of three states.
 - Free
 - Wounded
 - Mortally wounded

When you take a wound, one of your free slots becomes wounded. Wounds are difficult to remove - and require special magics or healing items.

When a character has no free wounds remaining, they will [black out](#Black-out).

If additional wounds are dealt when no free wounds remain, then a wound is instead upgraded to a [mortal wound](#Mortal-wound). When all wound slots are filled with [mortal wounds](#Mortal-wounds), then the character is [dead](statuses.md#Dead).

## Black out

When no wounds are available, a character will become [unconscious](statuses.md#unconscious). Unconsciousness persists until a point of [fatigue](statuses.md#Fatigue) is restored.

A player character may choose press on and stay concious instead of blacking out. If they do so, they will not be able to black out until they take another would.

## Mortal wound
 
A mortal wound reflects a life threatening wound to the character. This cannot be easily treated, and will negatively affect the character.

When a mortal wound is gained, they recieve an effect from the [wound table](#Wound-table). This may be selected by rolling, or at the DM's discretion.

A mortal wound cannot be removed trivially. They DM may select some of these options for removing wounds:
 - Days or weeks of care in town to let your wounds heal
 - Paying for the services of an expert healer
 - Requiring the player to go on a small side quest
 - Making it a permenant wound as a reminder of the players hubris

# Size

