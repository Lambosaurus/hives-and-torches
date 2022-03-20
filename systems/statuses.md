# Inflicted status effects

The following status effects are infliced on your character by various actions or events. These remain on the character until explicitly cleared. This will be described either in the status, or in the rule that applied the status.

## Grappled

A grappled character has been grabbed by a foe or magical effect. They cannot move without first escaping, and it is difficult to  

 - A grappled character may not move using their [move](actions.md#move) or [manoeuvre](actions.md#manoeuvre) actions.
 - [Attacks](rolls.md#attacks) made against a grappled target are made with an [advantage](rolls.md#advantage).

The grappled character may use its action to attempt to escape the grapple using a strength test against the grappler.


## Restrained
Restrained is an advanced form of [grappled](#grappled). You may not be both grapped and restrained.

 - A restrained character may not move using their [move](actions.md#move) or [manoeuvre](actions.md#manoeuvre) actions.
 - The restrained character may not use any actions that require their hands, such as [attacking](rolls.md#attacks), or casting [spells](spells.md) with a [somatic component](spells.md#somatic).
 - [Attacks](rolls.md#attacks) made against a restrained target are made with a `2x` [advantage](rolls.md#advantage).

The restrained character may use its action to attempt to escape being restrained using a strength test against the restrainer.

## Prone
A prone character is lying on the ground. Their ability to move is reduced, and it is difficult to use weapons. Your character may willingly become prone by using their [manoeuvre](actions.md#manoeuvre) action to lie down.

 - A prone character has its move actions modified. They may instead:
    - [Move](actions.md#move) action to move up to half their speed
    - [Manoeuvre](actions.md#manoeuvre) action to stand up

 - Any [melee attacks](rolls.md#melee-attack) against a prone character are made with an [advantage](rolls.md#advantage).
 - Any [ranged attacks](rolls.md#ranged-attack) against a prone character are made with a [disadvantage](rolls.md#disadvantage).

## Marked
A marked character has been specially marked by some effect that makes them makes them easier to spot and hit.

 - A marked character may not become [hidden](#hidden).
 - All [attacks](rolls.md#attacks) against a marked character are made with an [advantage](rolls.md#advantage).

This may stack with vulnerable.

## Vulnerable
A vulnerable character has lost the ability to properly defend themselves.

 - All [attacks](rolls.md#attacks) against a vulnerable character are made with an [advantage](rolls.md#advantage).

This may stack with marked.

## Blinded
A blinded character has lost the ability to see their foes.

 - All foes are considered [hidden](#hidden).

Note that some foes may have access to other forms of locating targets. This will be mentioned in their stat sheet, and renders them functionally immune to being blinded.

## Bleeding
Cuts on this character cause blood to run freely unless staunched.

A bleeding character takes `1d4` damage before making any [primary action](actions.md#primary-action). This damage ignores [defence](stats.md#defence).

A character may use their [primary action](actions.md#primary-action) to staunch the bleeding in combat.
This action is [unsafe](actions.md#unsafe-action), and is successful on a simple [medicine](skills.md#medicine) [test](rolls.md#tests). Using the staunch action does not the bleeding damage.

> Note: This should not be inflicted on players casually in combat - it is intended to be very dangerous.

## Weakened
This character is physically weakened. Simple tests of strength and control seem difficult.

 - All [tests](rolls.md#tests) and [attacks](rolls.md#attacks) based on [strength](stats.md#strength) or [finesse](stats.md#finesse) are done with [disadvantage](rolls.md#disadvantage).

## Dazed
By fever or headwound, this character has trouble focusing on mental tasks.

When a character is dazed:
 - All [tests](rolls.md#tests) and [spells](spells.md) based on [intellect](stats.md#intellect) or [will](stats.md#will) are done with [disadvantage](rolls.md#disadvantage).

## Stunned
A stunned character's mind and senses are pushed to the limit - and cannot react normally.

 - They may **not** take [reactions](actions.md#reactions).

## Blighted
A blighted character is is being weaked by an infection, toxins, or parasites.

 - [fatige](stats.md#fatigue) resoration is reduced by half.
 - TODO. Something needs to be added to this.

## Crippled
This foe has been hamstrung, or is pinned by arrows or magic. Movement is extremely difficult.

When a character is crippled:
 - Their movement using the [move](actions.md#move) action is halved
 - May not take the [manoeuvre](actions.md#manoeuvre) action

## Supressed
This foe is incapable of focusing on attacking, as they are are under other attacks.

When a character is supressed:
 - All [attacks](rolls.md#attacks) are made with [disadvantage](rolls.md#disadvantage)

## Unconscious 
A character may be unconcious because they are asleep, under the effect of a [spell](spells.md), or have subcumb to their [wounds](stats.md#wounds).

When a character is unconscious:
 - They may take no [actions](actions.md#actions)
 - They will fall [prone](#prone) unless explicitly prevented
 - Attacks against them are made with `2x` [advantage](rolls.md#advantage).

> Note: The additional advantage does not stack with hidden.

## Dead
This character is dead. This is final.
 - This character is removed from the turn order.
 - It is time to roll a new character.

# Conditional status effects

These are conditional status effects that are considered between characters on a turn by turn basis. These should be automatically applied if you or your foe meets the conditions.

For example: a foe may be [in cover](#in-cover) when viewed by one character, but not when viewed by another.

## In cover
If a character is half obscured by solid terrain, they are considered to be in cover.

Examples of cover include:
 - Tree cover.
 - Behind windows, low walls, or crenellations.
 - On top of a cliff or rampart.

When a character is in cover:
 - [Attacks](rolls.md#attacks) against them are made with a [disadvantage](rolls.md#disadvantage).

## High ground
If a character is elevated `10 feet` or higher above his foe, it is easier to aim and fire missiles.

When a character has high ground:
 - [Ranged attacks](rolls.md#ranged-attack) against the foe are made with with an [advantage](rolls.md#advantage)

A character with high ground is likely to also be [in cover](#in-cover) from their foe. This is to be determined by the DM.

## Hidden
A character is considered hidden if they are unable to be detected by a foe. This may be due to the following reasons:
 - The foes senses are unable to detect the character.
 - The foe is unaware that the characters may be nearby.

Some [feats](feats.md#feats) and [spells](spells.md) will confer hidden to a character, but it is up to the DM's discretion whether the foes other senses can bypass this.

A foe is not able to properly defend against a hidden character, and cannot normally [attack](rolls.md#attacks) them.

A foe may attempt to guess the location of a hidden character and attack anyway. This may automatically fail at the DM's discretion.

When a character is hidden from a foe:
 - [Attacking](rolls.md#attacks) the foe is made with [advantage](rolls.md#advantage).
 - [Attacks](rolls.md#attacks) aginst the character are made with `2x` [disadvantage](rolls.md#disadvantage).

 ## Shooting into melee
A character is considered shooting into melee when making a [ranged attack](rolls.md#ranged-attack) against a foe and there are allies within `5 feet` of the foe.

 - You take a [disadvantage](rolls.md#disadvantage) **per friendly character** within `5 feet` of your target.
 - On a [critical failure](rolls.md#critical-failure), your attack instead hits one of the friendly characters. The hit character is selected at the DM's discretion. The [damage](stats.md#damage) dealt is your rolled damage **excluding your disadvantage dice**.

## Flanking
A character is considered flanking if there is another friendly character who meets the following criteria:
 1) Is capable of making a [melee attack](rolls.md#melee-attack) against the foe. This includes:
    - Has a [melee weapon](weapons.md#melee-weapons) in their hands
    - Is within [weapon reach](weapons.md#weapon-reach)
    - Is willing to make an attack
 2) Is threatening a different face of the enemy as the first character.
    - Corners are only considered a different face if they are **not** adjacent to the threatened face.

When a character is flanking a foe:
 - All [melee attacks](rolls.md#melee-attack) against the foe are with and [advantage](rolls.md#advantage)

> ### Example 1:
> ```
> Case 1            Case 2           Case 3
> ┌───┬───┬───┐    ┌───┬───┬───┐    ┌───┬───┬───┐
> │   │   │   │    │   │   │   │    │   │   │   │
> ├───┼───┼───┤    ├───┼───┼───┤    ├───┼───┼───┤
> │   │ X │   │    │   │ X │   │    │ C │ X │   │
> ├───┼───┼───┤    ├───┼───┼───┤    ├───┼───┼───┤
> │   │ A │ B │    │ A │   │ B │    │   │ A │ B │
> └───┴───┴───┘    └───┴───┴───┘    └───┴───┴───┘
> ```
> In *Case 1*, characters A and B are **not** flanking the foe X, because the corner threatened  by B is adjacent to the face threatend by A.
>
> In *Case 2* characters A and B **are** flanking, because their corners are not adjacent.
>
> In *Case 3* characters A, B and C are **all** flanking. A and B are both not threatening the same face as C.

> ### Example 2:
> ```
> ┌───┬───┬───┐
> │   │ X │ X │
> ├───┼───┼───┤
> │   │ X │ X │ 
> ├───┼───┼───┤ 
> │ A │   │ B │
> └───┴───┴───┘
> ```
> The large foe, X, occupies 4 squares. A and B are **not** flanking, because the corner threatened by A is adjacent to the edge threatened by B.
>
### Cases with high weapon reach
It can be difficult to determine the threatened face or corner when a character with `10 feet` or higher reach are attacking a foe. For now, this shall be left to the discretion of the DM.
