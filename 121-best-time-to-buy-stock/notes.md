

## Follow-ups / gotchas

brute force: O(N^2) solution set each i as buy time and iterate for each sell time

use the kadane algorithm

have a profit =0 and buy=prices[0] to start. update the buy prices if the new price is lower
then if the prices is higher, check if the profit needs to be updated

