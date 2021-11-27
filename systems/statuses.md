# Inflicted status effects

The following status effects are infliced on your character by various actions or events. These remain on the character until explicitly cleared. This will be described either in the status, or in the rule that applied the status.

## Grappled

A grappled character has been grabbed by a foe or magical effect. They cannot move without first escaping, and it is difficult to  

 - A grappled character may not move using their move or manouvering actions.
 - [Attacks](rolls.md#Attack) made against a grappled target are made with an [advantage](rolls.md#Advantage).

The grappled character may use its action to attempt to escape the grapple using a strength test against the grappler.


## Restrained
Restrained is an advanced form of [grappled](#grappled). You may not be both grapped and restrained.

 - A restrained character may not move using their move or manouvering actions.
 - The restrained character may not use any actions that require their hands, such as [attacking](rolls.md#Attack), or casting [spells](spells.md) with a [somatic component](spells.md#Somatic).
 - [Attacks](rolls.md#Attack) made against a restrained target are made with a `2x` [advantage](rolls.md#Advantage).

The restrained character may use its action to attempt to escape being restrained using a strength test against the restrainer.

## Prone
A prone character is lying on the ground. Their ability to move is reduced, and it is difficult to use weapons. Your character may willingly become prone by taking half of their movement during a move action to do so.

 - A prone character has its move actions modified. They may instead:
    - [Move](actions.md#Move) action to move up to half their speed
    - [Manouver](actions.md#Manouvering) action to stand up

 - Any [melee attacks](rolls.md#Melee-attack) against a prone character are made with an [advantage](rolls.md#Advantage).
  - Any [ranged attacks](rolls.md#Ranged-attack) against a prone character are made with a [disadvantage](rolls.md#Disadvantage).

## Marked
A marked character has been specially marked by some effect that makes them easy.

 - A marked character may not become [hidden](#Hidden)
- All [attacks](rolls.md#ttack) against a marked character are made with an [advantage](rolls.md#Advantage).

## Blinded
A blinded foe has lost the ability to see their foes.

 - All foes are considered [hidden](#Hidden).

Note that some foes may have access to other forms of locating targets. This will be mentioned in their stat sheet, and renders them functionally immune to being blinded.

# Conditional status effects

These are conditional status effects that are considered between characters on a turn by turn basis. These should be automatically applied if you or your foe meets the conditions.

For example: a foe may be [in cover](#in-cover) when viewed by one character, but not when viewed by another.

## In cover
If a character is over half obscured by solid terrain, such as walls or trees, then they are considered in cover.

 - [Attacks](rolls.md#Attack) against a foe in cover are made with a [disadvantage](rolls.md#Disadvantage)

## Hidden
A character is considered hidden if they are unable to be detected by a foe. This may be due to the following reasons:
- The foe is [blinded](#Blinded)
- The foe is unaware that the characters may be nearby
- The character is invisible, obscured in smoke, or otherwise cannot be observed by the foes current senses.

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

### Example 1:
```
Case 1            Case 2           Case 3
┌───┬───┬───┐    ┌───┬───┬───┐    ┌───┬───┬───┐
│   │   │   │    │   │   │   │    │   │   │   │
├───┼───┼───┤    ├───┼───┼───┤    ├───┼───┼───┤
│   │ X │   │    │   │ X │   │    │ C │ X │   │
├───┼───┼───┤    ├───┼───┼───┤    ├───┼───┼───┤
│   │ A │ B │    │ A │   │ B │    │   │ A │ B │
└───┴───┴───┘    └───┴───┴───┘    └───┴───┴───┘
```
In *Case 1*, characters A and B are **not** flanking the foe X, because the corner threatened by B is adjacent to the face threatend by A.

In *Case 2* characters A and B **are** flanking, because their corners are not adjacent.

In *Case 3* characters A, B and C are **all** flanking. A and B are both not threatening the same face as C.

### Example 2:
```
┌───┬───┬───┐
│   │ X │ X │
├───┼───┼───┤
│   │ X │ X │ 
├───┼───┼───┤ 
│ A │   │ B │
└───┴───┴───┘
```
The large foe, X, occupies 4 squares. A and B are **not** flanking, because the corner threatened by A is adjacent to the edge threatened by B.

### Cases with high weapon reach
It can be difficult to determine the threatened face or corner when a character with `10 feet` or higher reach are attacking a foe. For now, this shall be left to the discretion of the DM.