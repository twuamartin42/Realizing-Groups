# Realizing-Groups

## Project Overview
This is a repository for the research project Structures of Groups of order 2^n Realized by Groups of Units 
with code is dedicated to compute examples of generators for the groups U(m) with order up to 2^15.

## Example of use with Python Algorithm:
### Step 1
Install Python and Apache NetBeans 18. Follow the documentation found in these links *insert links for installation*. 
### Step 2
Fetch required files. One can clone the repository via git:
`git clone https://github.com/twuamartin42/Realizing-Groups.git`
Alternatively, one can download a given file manually from the repository. 
All of the generator data is stored in the directory named `Data`.
A given .csv file in that directory has filename of the form:
`n.csv`, according to the order of 2^n. 
### Step 3
Import the main.py code into ApacheNetBeans18. In a group order of 2^n, we initialize a group of that group order:

The Python algorithm used the user-input variables `groupOrder = 2^n and modBase = m.`

Generate a list of group elements.
`groupOrder = 2^n and modBase = m.`
The group elements generated are the numbers that range from `1` to `n-1` that are relatively prime to n. A list of group
elements were genereated using a function that calculated greatest common divisor.

Identify group elements that correspond to the order given in the classification of U (m). 
Find group elements with orders equal to the values a_i for
`1 ≤ i ≤ n in U (m) ∼= Z_2^(a1) × Z_2^(a2) × · · · × Z_2^(an)`. 
To obtain group elements of these orders, raise groups element to successive powers `mod m` until `1 mod m` is obtained. 
This process will generate the cyclic subgroup of the group element.

Multiply the cyclic subgroups with each another to generate all possible group elements. 
Multiply all elements of the cyclic subgroups with each other. After performing the multiplication between all elements of the cyclic subgroups,
if these elements were indeed generators of the group, then there were `2^n` unique values that corresponded to the
group elements identified when generating the list fo group elements.
