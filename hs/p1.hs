-- Finds the sum of all the multiples of 3 or 5 below 1000.
-- (c) 2013 Matthew Rheaume

module Main where

solve :: Int
solve = sum [i | i <- [1..999], mod i 3 == 0 || mod i 5 == 0]

main :: IO ()
main = putStrLn $ show $ solve
