main = do
  [a, b] <- words <$> getLine
  let a' = read a :: Int
  let b' = read b :: Int
  print $ a' `mod` b'
