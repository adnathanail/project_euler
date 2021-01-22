-- Problem 1 - Multiples of 3 and 5
problem_1 = sum [x | x <- [0..999], x `mod` 3 == 0 || x `mod` 5 == 0]

-- Problem 2 - Even Fibonacci numbers
{-
    Initial naive implmentation
    Fantastically slow - O(fib n)

    fib n
        | n == 0 = 1
        | n == 1 = 1
        | otherwise = (fib (n - 1)) + (fib (n - 2))
-}
fibs = 0:1:zipWith (+) fibs (tail fibs)
fib n = fibs!!n
problem_2 = sum $ filter even [fib x | x <- takeWhile (\x -> (fib x) < 4000000) [1..]]

-- Problem 3 - Largest prime factor
{-
    Accidentally implemented factor function, not PRIME factor function
    Keeping for posterity

    factors n = (unique . flatten) $ factors_part n
        where
            unique_part l e
                | e `elem` l = l
                | otherwise = e:l
            unique = foldl unique_part []
            flatten = foldl (\l (a, b) -> a:b:l) []
            factors_part n = [(x, n `div` x) | x <- [1..(ceiling $ sqrt $ fromIntegral n)], n `rem` x == 0 ]
-}

-- problem_3 = maximum $ factors 600851475143

main = do
    print 1