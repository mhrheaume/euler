-- Finds the largest prime factor of the number 600851475143
--
-- (c) 2013 Matthew Rheaume

module Main where

largestPrimeFactor :: Int -> Int
largestPrimeFactor 1 = 1
largestPrimeFactor n = max factor (largestPrimeFactor $ n `div` factor) where
	factor = factorize 2 n
	factorize m n
		| n `mod` m == 0 = m
		| otherwise = factorize (m + 1) n

solve :: Int
solve = largestPrimeFactor 600851475143

main :: IO ()
main = putStrLn $ show $ solve
