# Realizing-Groups

## Project Overview
This is a repository for the research project "A Study on the Variety of Structures of Groups of Units of Order 2^n," 
with code dedicated to compute examples of generators for the groups U(m) with order up to 2^15.

## Example of use with Python Algorithm:
### Step 1
Install Python and your chosen IDE. Follow the documentation found in these links *insert links for installation*. 
### Step 2
Fetch required files. One can clone the repository via git:
`git clone https://github.com/twuamartin42/Realizing-Groups.git`
Alternatively, one can download a given file manually from the repository. 
All of the generator data is stored in the directory named `Data`.
A given .csv file in that directory has filename of the form:
`n.csv`, according to the order of 2^n. 
### Step 3
Import the `main.py` code into your chosen IDE. The Python algorithm uses the user-input variables `groupOrder and modBase `.

Generate a list of group elements.
The group elements generated are the numbers that range from `1` to `n-1` that are relatively prime to n.
This is stored `elementList`.

Identify group elements that correspond to the order given in the classification of U(m) given the structure of U(m) as defined by the Fundamental Theorem of Finite Abelian Groups. 
In `main.py`, we give an example generating elements of order 2, stored in `order2Elements`. You can edit the code for orders 4, 8, etc. that are needed. 

Generate cyclic subgroups.
`modList` will generate the cyclic subgroup for what is set for base. Take the element of the desired order and set it equal to base. 
The cyclic subgroup is store in `modList`.

Multiply the cyclic subgroups with each another to generate all possible group elements. 
Multiply all elements of the cyclic subgroups with each other. After performing the multiplication between all elements of the cyclic subgroups,
if these elements were indeed generators of the group, then there were `2^n` unique values that corresponded to the
group elements identified when generating the list fo group elements.
