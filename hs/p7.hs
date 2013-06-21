-- Finds the 10,001st prime number.
--
-- (c) 2013 Matthew Rheaume

module Main where

intSqrt :: Int -> Int
intSqrt = ceiling . sqrt . fromIntegral

isPrime :: Int -> Bool
isPrime 2 = True
isPrime n = foldr checkDivisor True [2..(intSqrt n)] where
	checkDivisor k = (n `mod` k /= 0 &&)

findPrime :: Int -> Int
findPrime count = checkPrimes count 2 where
	checkPrimes 0 n = n - 1
	checkPrimes k n =
		if (isPrime n) then
			checkPrimes (k - 1) (n + 1)
		else
			checkPrimes k (n + 1)

solve :: Int
solve = findPrime 10001

main :: IO ()
main = putStrLn $ show $ solve
