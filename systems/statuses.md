# Inflicted status effects

The following status effects are infliced on your character by various actions or events. These remain on the character until explicitly cleared. This will be described either in the status, or in the rule that applied the status.

## Grappled

A grappled character has been grabbed by a foe or magical effect. They cannot move without first escaping, and it is difficult to  

 - A grappled character may not move using their [move](actions.md#Move) or [manoeuvre](actions.md#Manoeuvre) actions.
 - [Attacks](rolls.md#Attack) made against a grappled target are made with an [advantage](rolls.md#Advantage).

The grappled character may use its action to attempt to escape the grapple using a strength test against the grappler.


## Restrained
Restrained is an advanced form of [grappled](#grappled). You may not be both grapped and restrained.

 - A restrained character may not move using their [move](actions.md#Move) or [manoeuvre](actions.md#Manoeuvre) actions.
 - The restrained character may not use any actions that require their hands, such as [attacking](rolls.md#Attack), or casting [spells](spells.md) with a [somatic component](spells.md#Somatic).
 - [Attacks](rolls.md#Attack) made against a restrained target are made with a `2x` [advantage](rolls.md#Advantage).

The restrained character may use its action to attempt to escape being restrained using a strength test against the restrainer.

## Prone
A prone character is lying on the ground. Their ability to move is reduced, and it is difficult to use weapons. Your character may willingly become prone by using their [manoeuvre](actions.md#Manoeuvre) action to lie down.

 - A prone character has its move actions modified. They may instead:
    - [Move](actions.md#Move) action to move up to half their speed
    - [Manoeuvre](actions.md#Manoeuvre) action to stand up

 - Any [melee attacks](rolls.md#Melee-attack) against a prone character are made with an [advantage](rolls.md#Advantage).
 - Any [ranged attacks](rolls.md#Ranged-attack) against a prone character are made with a [disadvantage](rolls.md#Disadvantage).

## Marked
A marked character has been specially marked by some effect that makes them makes them easier to spot and hit.

 - A marked character may not become [hidden](#Hidden).
 - All [attacks](rolls.md#Attack) against a marked character are made with an [advantage](rolls.md#Advantage).

## Blinded
A blinded foe has lost the ability to see their foes.

 - All foes are considered [hidden](#Hidden).

Note that some foes may have access to other forms of locating targets. This will be mentioned in their stat sheet, and renders them functionally immune to being blinded.

## Bleeding
[This section is a stub. Submit a Pull Request to edit it](https://github.com/Lambosaurus/hives-and-torches/edit/main/systems/statuses.md)

## Crippled
This foe has been hamstrung, or is pinned by arrows or magic. Movement is extremely difficult.

When a character is crippled:
 - Their movement using the [Move](actions.md#Move) action is halved
 - May not take the [manoeuvre](actions.md#Manoeuvre) action

## Unconscious 
A character may be unconcious because they are asleep, under the effect of a [spell](spells.md#Spell), or have subcumb to their [wounds](stats.md#Wounds).

When a character is unconscious:
 - They may take no [actions](actions.md#Actions)
 - They will fall [prone](#Prone) unless explicitly prevented
 - Attacks against them are made with `2x` [advantage](rolls.md#Advantage). This may **not** stack with the bonuses from [hidden](#Hidden).

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
 - [Attacks](rolls.md#Attack) against them are made with a [disadvantage](rolls.md#Disadvantage).

## High ground
If a character is elevated `10 feet` or higher above his foe, it is easier to aim and fire missiles.

When a character has high ground:
 - [Ranged attacks](rolls.md#Ranged-attack) against the foe are made with with an [advantage](rolls.md#Advantage)

A character with high ground is likely to also be [in cover](#in-cover) from their foe. This is to be determined by the DM.

## Hidden
A character is considered hidden if they are unable to be detected by a foe. This may be due to the following reasons:
 - The foes senses are unable to detect the character.
 - The foe is unaware that the characters may be nearby.

Some [feats](feats.md#feats) and [spells](spells.md#Spells) will confer hidden to a character, but it is up to the DM's discretion whether the foes other senses can bypass this.

A foe is not able to properly defend against a hidden character, and cannot normally [attack](rolls.md#Attack) them.

A foe may attempt to guess the location of a hidden character and attack anyway. This may automatically fail at the DM's discretion.

When a character is hidden from a foe:
 - [Attacking](rolls.md#Attack) the foe is made with [advantage](rolls.md#Advantage).
 - [Attacks](rolls.md#Attack) aginst the character are made with `2x` [disadvantage](rolls.md#Disadvantage).

 ## Shooting into melee
A character is considered shooting into melee when making a [ranged attack](rolls.md#Ranged-attack) against a foe and there are allies within `5 feet` of the foe.

 - You take a [disadvantage](rolls.md#Disadvantage) **per friendly character** within `5 feet` of your target.
 - On a [critical failure](#Critical-failure), your attack instead hits one of the friendly characters. The hit character is selected at the DM's discretion. The [damage](stats.md#Damage) dealt is your rolled damage **excluding your disadvantage dice**.

## Flanking
A character is considered flanking if there is another friendly character who meets the following criteria:
 1) Is capable of making a [melee attack](rolls.md#Melee-attack) against the foe. This includes:
    - Has a [melee weapon](weapons.md#melee-weapons) in their hands
    - Is within [weapon reach](weapons.md#Weapon-reach)
    - Is willing to make an attack
 2) Is threatening a different face of the enemy as the first character.
    - Corners are only considered a different face if they are **not** adjacent to the threatened face.

When a character is flanking a foe:
 - All [melee attacks](rolls.md#Melee-attack) against the foe are with and [advantage](rolls.md#Advantage)

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
