-- Finds the largest palindrome made from the project of two 3-digit numbers
--
-- (c) 2013 Matthew Rheaume

module Main where

isPalindrome :: String -> Bool
isPalindrome [] = True
isPalindrome [s] = True
isPalindrome (x:xs)
	| x == (last xs) = isPalindrome $ init xs
	| otherwise = False

solve :: Int
solve = maximum pList where
	pList = [x*y | x <- [100..999], y <- [100..999], isPalindrome(show(x*y))]

main :: IO ()
main = putStrLn $ show $ solve
