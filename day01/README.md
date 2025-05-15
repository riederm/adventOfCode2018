# How to run the example
Make sure you navigate into this folder!
```
cd day01
````

Execute the example using node (Node is a java-script runtime).

```
@riederm ➜ /workspaces/adventOfCode2018/day01 (py) $ python day01.py 
read 958 lines
```
It should have printed "read 958 lines"
[Advent of Code 2018 - Day 1](https://adventofcode.com/2018/day/1)

# Task 1: Resulting Frequency

After feeling like you've been falling for a few minutes, you look at the device's tiny screen:

> "Error: Device must be calibrated before first use. Frequency drift detected. Cannot maintain destination lock."

Below the message, the device shows a sequence of changes in frequency (your puzzle input). A value like `+6` means the current frequency increases by 6; a value like `-3` means the current frequency decreases by 3.

### Example Walkthrough

If the device displays frequency changes of `+1, -2, +3, +1`, then starting from a frequency of zero, the following changes would occur:

- Current frequency `0`, change of `+1`; resulting frequency `1`.
- Current frequency `1`, change of `-2`; resulting frequency `-1`.
- Current frequency `-1`, change of `+3`; resulting frequency `2`.
- Current frequency `2`, change of `+1`; resulting frequency `3`.

In this example, the resulting frequency is **3**.

### Additional Examples

- `+1, +1, +1` results in **3**
- `+1, +1, -2` results in **0**
- `-1, -2, -3` results in **-6**

**Question:** Starting with a frequency of zero, what is the resulting frequency after all of the changes in frequency have been applied?

---

# Task 2: First Repeated Frequency

You notice that the device repeats the same frequency change list over and over. To calibrate the device, you need to find the first frequency it reaches twice.

### Example Walkthrough

Using the same list of changes as above, the device would loop as follows:

- Current frequency `0`, change of `+1`; resulting frequency `1`.
- Current frequency `1`, change of `-2`; resulting frequency `-1`.
- Current frequency `-1`, change of `+3`; resulting frequency `2`.
- Current frequency `2`, change of `+1`; resulting frequency `3`.
  *(At this point, the device continues from the start of the list.)*
- Current frequency `3`, change of `+1`; resulting frequency `4`.
- Current frequency `4`, change of `-2`; resulting frequency `2`, which has already been seen.

In this example, the first frequency reached twice is **2**.

### Additional Examples

- `+1, -1` first reaches **0** twice.
- `+3, +3, +4, -2, -4` first reaches **10** twice.
- `-6, +3, +8, +5, -6` first reaches **5** twice.
- `+7, +7, -2, -7, -4` first reaches **14** twice.

**Question:** What is the first frequency your device reaches twice?
