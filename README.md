# Let's Play: Russian Roulette

## Main Idea
A friend of mine encountered a problem on an exam regarding Russian roulette, which lead him to a theory.

His hypothesis: **If the bullet cylinder of the revolver is not respun after each person shoots, then the odds are 50/50. If the bullet cylinder is respun, then the odds are in favor of the person who shoots second.**

Naturally, this is something that can be easily simulated using programming, so I did just that.

## Running the simulation
This game can be simulated by running `game.py` either with an argument representing the number of simulations, or as an input as prompted by the program.

## Results
The results of the test can be seen below. These numbers came from a single run of 10,000,000 simulations, but all other simulation runs of the same quantity gave similar results (within a few hundredths of a percent).

<table>
    <tr>
        <th colspan="3">Results - No Respin</th>
    </tr>
    <tr>
        <th>Person</th>
        <th>Chance</th>
    </tr>
    <tr>
        <td>1</td>
        <td>50.00%</td>
    </tr>
    <tr>
        <td>2</td>
        <td>50.00%</td>
    </tr>
</table>

<br>

<table>
    <tr>
        <th colspan="3">Results - Respin</th>
    </tr>
    <tr>
        <th>Person</th>
        <th>Chance</th>
    </tr>
    <tr>
        <td>1</td>
        <td>53.02%</td>
    </tr>
    <tr>
        <td>2</td>
        <td>46.97%</td>
    </tr>
</table>

## Conclusion
With these results, it can be concluded that the hypothesis is correct. Playing Russian roulette without respinning the cylinder between shots results in a 50% (±.01%) chance of either person being killed. However, the probability changes if the cylinder is respun between each persons turn, with slightly more variance. The odds come out slightly in favor of the second person, who only has an approxiamtely 46.97% (±.02%) chance of being killed, while the first person has a 53.02 (±.02%) chance of being killed.

## Final Thoughts
This was a fun exercise. In the midst of school finals and project deadlines, it was nice to set aside an hour or two and write a short program like this for fun. In the future I would like to clean up some of the code, and maybe do other simulations of a similar kind.
