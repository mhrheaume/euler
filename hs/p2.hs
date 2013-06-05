-- Finds the sum of the even-valued terms of the Fibonacci sequence not
-- exceeding four million.
--
-- (c) 2013 Matthew Rheaume

module Main where

import Data.Bits

fibSumEven :: Int -> Int -> Int
fibSumEven a b
	| x >= 4000000 = 0
	| testBit x 0 = fibSumEven b x
	| otherwise = x + fibSumEven b x
	where x = a + b

-- Sequence starts with 1 and 2
solve :: Int
solve = 2 + (fibSumEven 1 2)

main :: IO ()
main = putStrLn $ show $ solve
