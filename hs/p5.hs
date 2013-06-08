-- Finds the smallest positive number that is evenly divisible by all of the
-- numbers from 1 to 20.
--
-- (c) 2013 Matthew Rheaume

module Main where

minus :: (Ord a) => [a] -> [a] -> [a]
minus = loop where
	loop [] _ = []
	loop xs [] = xs
	loop (x:xs) (y:ys) = case compare x y of
		LT -> x : loop xs (y:ys)
		EQ -> loop xs ys
		GT -> loop (x:xs) ys

sieve :: Int -> [Int]
sieve n = sieveList [2..n] where
	sieveList [] = []
	sieveList (x:xs) = [x] ++ (sieveList $ xs `minus` (map (*x) (x:xs)))

smallestMultiple :: Int -> Int
smallestMultiple n = foldr prodLargestPowers 1 primes where
	primes = sieve n
	largestPower = truncate $ logBase (fromIntegral 2) (fromIntegral n)
	prodLargestPowers x = (x ^ (maximum [i | i <- [1..largestPower], x^i <= n]) *)

solve :: Int
solve = smallestMultiple 20

main :: IO ()
main = putStrLn $ show $ solve
