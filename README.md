# AI-Bottle-Distribution
This program implements an AI Production System (AIPS) for simulated water jug deliveries. 

**AI Production System Specifications**

1. The system shall support up to 8 different customers and a dispatcher. <br />
2. The dispatcher shall compute an optimized path to deliver water to the customers. <br />
3. Each customer shall have a name, a location, a water column, an empty, a full shelf, a robot and a consumption rate.<br />
4. Each water column shall be either regular or chilled.<br />
5. The full shelf shall have space for storing 3 full bottles that stack on top of each other. <br />
6. The empty shelf shall have space for 3 empty bottles that stack on top of each other. <br />
7. The system shall have an AIPS that will automatically monitor and control the system. <br />
8. The AIPS uses a robot that shall move bottles from the full shelf, water column, and empty shelf. <br />
9. The AIPS shall detect leaks and send an alarm to the dispatcher. <br />
10. The AIPS shall replenish the full shelf if there is one bottle left in the full shelf and the bottle in the column is less than ¼ of a gallon. <br />
11. The AIPS shall call the robot to replace a bottle if the water on the stand is empty. <br />
12. The AIPS shall control the water temperature for a chilled water stand to have operating temperatures of 42F +/- 2F. <br />
