# Actions

A turn represents a six second period of time

In a characters turn they may use the following:
 * One primary action
 * One secondary action
 * One reaction

You may downgrade a primary action to a secondary action, and a secondary action to a reaction.

## Unsafe action
Some actions are unsafe, and leave you vulnerable to an attack from an elegible foe. These actions may provoke an [Attack of opportunity](#attack-of-opportunity).

# Primary action
The primary action represents the action that is the characters focus for this turn. This action usually takes:
 * The characters full attention
 * The use of both hands

Examples of primary actions include:
 * Attacking with a weapon
 * Casting a spell
 * Using a skill
 * Using an item

A primary action may always be dowgraded to a fast action.

# Secondary action
The secondary action is something that can be completed either:
 * In less than a second
 * Without the use of the hands

Examples of secondary actions include:
 * Movement
 * Manoeuvring
 * Using an off hand weapon
 * Drawing or sheathing a weapon
 * Some fast skills or spells.

 A secondary action may always be downgraded to a reaction.

# Reactions
Reactions are very fast actions that are used to counter an action. It is possible for a character to have multiple reactions per turn - however these may not be used to counter the same action.

# Basic actions
The following is a list of basic actions available to all characters.

## Melee Attack
`primary`
The character makes an attack with their primary weapon. See [melee attack](rolls.md#melee-attack) for more information.

## Ranged Attack
`primary`, `unsafe`
The character makes an attack with their ranged weapon. See [ranged attack](rolls.md#ranged-attack) for more information.

## Cast a spell
`primary`, `unsafe`
Spellcasting characters may use their turn to cast a spell.
See [Spells](spells.md) for more information.

## Use an item
`primary`, `unsafe`
A character may use a special item from their inventory. A typical example of this is drinking a potion.

## Grapple
`primary`
A character may try to grapple a foe within natural reach. To grapple a foe, you must have at least one completely free hand. You must roll a [strength](stats.md#strength) [test](rolls.md#tests) against their [finesse](stats.md#finesse). On success, the foe is [grappled](statuses.md#grappled), and may not move. When a foe is grappled, you may use your [movement](#move) to move up to half your [speed](stats.md#speed), taking the foe with you.

The grappled foe may use its [primary action](#primary-action) to make a strength test against you to escape.

## Restrain
`primary`
A character may try to restrain a foe within natural reach that is already [grappled](statuses.md#grappled). To restrain a foe, you must have two completely free hands. You must roll a [strength](stats.md#strength) [test](rolls.md#tests) against the foe. On success, the foe is [restrained](statuses.md#restrained), and may not use any actions that require hands.

The restrained foe may use its [primary action](#primary-action) to make a strength test against you to escape.

## Trip
`secondary`
This allows the character to attempt to trip a foe in natural reach. Make a [finesse](stats.md#finesse) [test](rolls.md#tests) against the foe.
 - On success, the foe is [prone](statuses.md#prone).
 - On a failure this action becomes [unsafe](#unsafe-action).

## Push
`secondary`
If the character has a free hand or shield, they may make a [strength](stats.md#strength) [test](rolls.md#tests) against the foe to push them back 5 feet.

## Move
`secondary`, `unsafe`
The character moves at a comfortable pace, moving up to their [normal movement](stats.md#speed). This may be interleaved with your other actions.

## Manoeuvre
`secondary`
The character makes a careful 5 foot step. This does **not** trigger an [attack of opportunity](#attack-of-opportunity).

## Draw a weapon
`secondary`
The character draws a weapon.

## Attack of opportunity
`reaction`
An attack of opportunity is triggered by a foe performing an [unsafe action](#unsafe-action) while within your weapon reach.

Unsafe actions include:
 * Taking the [move](#move) action
 * Casting a [spell](spells.md) with a primary action
 * Using an item (and the DM's discretion)

The basic attack of opportunity enables you to perform a [melee attack](rolls.md#melee-attack) against the foe. You must have a [melee weapon](weapons.md#melee-weapons) in your hand to be eligible for this action.
