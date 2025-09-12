# Realizing-Groups
This is a repository for the research project Structures of Groups of order 2^n Realized by Groups of Units.

For this project, we created an algorithm that used the programming language Python to compute our data. 

The Python algorithm used the user-input variables
  groupOrder = 2^n and modBase = m.

The algorithm is as follows:

Generate a list of group elements. The group elements are the numbers that
range from 1 to n − 1 that are relatively prime to n. We generated the list of group
elements using a function that calculated greatest common divisor.

Identify group elements that correspond to the order given in the classi-
fication of U (m). We found group elements with orders equal to the values a_i for
1 ≤ i ≤ n in U (m) ∼= Z_2^(a1) × Z_2^(a2) × · · · × Z_2^(an). To obtain group elements of these
orders, we raised a groups element to successive powers mod m until we obtained 1
mod m. This process also generated the cyclic subgroup of the group element.

Multiply the cyclic subgroups with each another to generate all possible
group elements. To multiply cyclic subgroups by each other, we multiplied all
elements of the cyclic subgroups with each other. After performing the multipli-
cation between all elements of the cyclic subgroups, if these elements were indeed
generators of the group, then there were 2^n unique values that corresponded to the
group elements identified when generating the list fo group elements.
