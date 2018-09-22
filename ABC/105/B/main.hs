check :: Integer -> String
check a
  | (a `mod` 4) == 0 = "Yes"
  | (a `mod` 7) == 0 = "Yes"
  | (a `mod` 7) `mod` 4 == 0 = "Yes"
  | (a `mod` 4) `mod` 7 == 0 = "Yes"
  | otherwise = "No"

main = do
  -- a <- getLine
  -- let a' = read a :: Integer
  -- putStrLn $ check a'
  print $ take 100 $ fmap (\x -> (check x, x)) [1..]
