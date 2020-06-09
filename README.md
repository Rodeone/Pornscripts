# Pornscripts

This script should check the deviation from the delta increment and predict the amount of iteration of incremental backup.
For example:
Data is written to the database in a stream
The size of the backup increment is conditionally constant
If the new increment deviates too much from the average value
We take the new increment as a delta and make a forecast of the backup iteration size using the formula:
F (x) = V (full backup) + n (number of increment removal points) * delta_increment
