1. Describe the algorithm you will use to find the room. Assume all the information you have is the one given by the sign; you have no knowledge of the floor plan.

    As the sign does not provide much information, such as the number of rooms with a number greater than 130, a linear search of the rooms starting at the left at room EY100 and checking each incrementing room until EY128 is found. I would avoid using a divide and conquer approach such as binary search, as we are unsure of where the midpoint may be. The sign only mentions there are rooms EY 100-130 one direction and all other rooms for the other direction. With only this information it is not possible to find a midpoint, so we cannot use binary search. So instead we use linear search.

2. How many "steps" it will take to find room EY128? And what is a "step" in this case?
    
    The rooms are organized in ascending order starting from EY100 with the room number incrementing by 2 for each room over you go. Starting at room EY100 and checking each ascending room, you would have to check 15 rooms or have 15 steps. In this case, a step refers to checking a room. So when using linear search to check for room EY128, you would have 15 steps or a time complexity of O(15).

3. Is this a best-case scenario, worst-case scenario, or neither?

    The best-case scenario in this example would be if the first room we checked was the room we were looking for, only having 1 step or O(1). Since we only know of there being rooms EY 100-130, the worst case would be checking room EY130 which takes 16 steps or O(n). Since we found EY128 before the worst-case, it is neither the worst-case or the best-case.

4. With this particular sign and floor layout, explain what a worst-case or best-case scenario would look like

    With knowledge of the sign and floor layout, a best-case scenario would be if we were looking for room EY100, as it would take 1 step or O(1). A worst-case scenario would be if we were looking for room EY138 or a room that was not in the floor layout, as it would take 20 steps or O(n) to search each room.

5. Suppose after a few weeks in the term you memorize the layout of the floor. How would you improve the algorithm  to make it more efficient?

    With knowledge of the floor plan, and knowing the rooms are sorted in ascending order by increments of 2 from EY 100-138, I would change my search algorithm to an interpolation search. I would choose an interpolation search rather than a binary search, as I know there are 20 rooms and 128 is halfway from the midpoint of 118 and 138. So rather than using a midpoint, I would set my "midpoint" to 3/4 of the rooms so room 15, as that is where the desired room is more likely to appear.
    