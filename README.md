# Realizing-Groups

## Project Overview
This is a repository for the research project "A Study on the Variety of Structures of Groups of Units of Order 2^n," 
with code dedicated to compute examples of generators for the groups U(m) with order up to 2^15.

## Example of use with Python Algorithm:
### Step 1
Install Python and your chosen IDE. Follow the documentation found in these links *insert links for installation*. 
### Step 2
Import the `main.py` code into your chosen IDE. The Python algorithm uses the user-input variables `groupOrder`, `modBase`, `base`, and `coefficient`.
### Step 3
Generate a list of group elements.
The group elements generated are the numbers that range from 1 to n-1 that are relatively prime to n.
This is stored in `elementList`.
### Step 4
Identify group elements that correspond to the order given in the classification of U(m) given the structure of U(m) as defined by the Fundamental Theorem of Finite Abelian Groups. 
In `main.py`, we give an example generating elements of order 2, stored in `order2Elements`. This can be edited for orders 4, 8, etc. as needed. 
### Step 5
Generate cyclic subgroups.
`modList` will generate the cyclic subgroup for the value set as base. Take the element of the desired order and set it equal to base. 
The cyclic subgroup is stored in `modList`.
### Step 6
Multiply all elements of the cyclic subgroups with each other. 
To multiply cyclic subgroups by each other, we set `base` to be the generator with the highest order. We set `coefficient` to be the elements of the cyclic subgroup of the next highest order to multiply these two cyclic subgroups together. After completing this multiplication, if there were 2^n unique values that corresponded to the group elements identified in part 1, then these elements were indeed generators of the group.
