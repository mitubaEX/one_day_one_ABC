main = do
  n <- getLine
  ss <- map read . lines <$> getContents :: IO[Int]
  let result = foldl lcm 1 ss
  print result

