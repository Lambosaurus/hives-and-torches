# Actions

A turn represents a six second period of time

In a characters turn they may use the following:
 * One primary action
 * One secondary action
 * One reaction

You may downgrade a primary action to a secondary action, and a secondary action to a reaction.

# Primary action:
The primary action represents the action that is the characters focus for this turn. This action usually takes:
 * The characters full attention
 * The use of both hands

Examples of primary actions include:
 * Attacking with a weapon
 * Casting a spell
 * Using a skill
 * Using an item

A primary action may always be dowgraded to a fast action.

# Secondary action:
The secondary action is something that can be completed either:
 * In less than a second
 * Without the use of the hands

Examples of secondary actions include:
 * Movement
 * Manouvering
 * Using an off hand weapon
 * Drawing or sheathing a weapon
 * Some fast skills or spells.

 A secondary action may always be downgraded to a reaction.

# Reactions:
Reactions are very fast actions that are used to counter an action. It is possible for a character to have multiple reactions per turn - however these may not be used to counter the same action.

# Basic actions:
The following is a list of basic actions available to all characters.

## Melee Attack: `primary`
Your character makes an attack with their primary weapon. TODO

## Ranged Attack: `primary`, `unsafe`
Your character makes an attack with their ranged weapon. TODO

## Cast a spell: `primary`, `unsafe`
Spellcasting characters may use their turn to cast a spell.
See [Spells](spells.md) for more information.

## Use an item: `primary`, `unsafe`
A character may use a special item from their inventory. A typical example of this is drinking a potion.

## Grapple `primary`
A character may try to grapple a foe within natural reach. To grapple a foe, you must have at least one completely free hand. You must roll a strength test against their dexterity. On success, the foe is [grappled](statuses.md#grappled), and may not move. Once a foe is grappled, you may use your movement to move up to half your speed, taking your foe with you.

The grappled foe may use its primary action to make a strength test against you to escape.

## Off hand attack: `secondary`
If your character has a weapon in their off hand, and has already attacked with their primary action, they may make a second attack. This follows the rules of a melee attack, but has the following restrictions:
 * Both weapons must be `light`
 * Both attacks will be at [disadvantage](rolls.md#Disadvantage).

## Push: `secondary`
If your character has a free hand or shield, they may make a strength test against the foe to push them back 5 feet.

## Move: `secondary`, `unsafe`
Your character moves at a comfortable pace, moving up to their normal movement. This may be interleaved with your other actions.

## Manouvering: `secondary`
Your character makes a careful 5 foot step. This does **not** trigger an attack of opportunity.

## Draw a weapon: `secondary`
Your character draws a weapon.

## Attack of opportunity: `reaction`
An attack of opportunity is be triggered by a foe performing an unsafe action while within your weapon reach.

Unsafe actions include:
 * Moving (excluding manouvering)
 * Casting a spell with a primary action
 * Using an item (and the DM's discretion)

The basic attack of opportunity enabled you to perform a melee attack against the foe.
