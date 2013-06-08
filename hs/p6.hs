-- Finds the difference between the sum of the squares of the first one hundred
-- numbers and the square of the sum.
--
-- (c) 2013 Matthew Rheaume

module Main where

squareSumDiff :: Int -> Int
squareSumDiff n = foldr sumProd 0 [1..n] where
	sumToN = sum [1..n]
	sumProd x = (x * (sumToN - x) +)

solve :: Int
solve = squareSumDiff 100

main :: IO ()
main = putStrLn $ show $ solve
